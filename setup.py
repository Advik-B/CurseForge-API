import os
import subprocess
from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
from sys import executable

class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=''):
        super().__init__(name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)

class CMakeBuild(build_ext):
    def run(self):
        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        cmake_args = [
            f'-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}',
            f'-DPYTHON_EXECUTABLE={executable}',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DEXAMPLE_VERSION_INFO=' + self.distribution.get_version(),
            '-GNinja'
        ]
        build_args = ['--config', 'Release']
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        subprocess.check_call(['cmake', ext.sourcedir] + cmake_args, cwd=self.build_temp)
        subprocess.check_call(['cmake', '--build', '.'] + build_args, cwd=self.build_temp)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="curseforge",
    version="2.0.0",
    author="Advik",
    author_email="advik.b@gmail.com",
    description="The python binding for the no-compromise CurseForge API wrapper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    ext_modules=[CMakeExtension("curseforge_bindings", sourcedir=os.path.dirname(__file__))],
    cmdclass={"build_ext": CMakeBuild},
    packages="curseforge",
    package_data={"curseforge": ["py.typed"]},
    zip_safe=False,
    python_requires=">=3.7",
)