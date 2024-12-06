from setuptools import setup
from glob import glob
from pybind11.setup_helpers import Pybind11Extension
from setuptools.command.build_ext import build_ext
import subprocess

class BuildExt(build_ext):
    def build_extensions(self):
        # Detect GCC version
        gcc_version = subprocess.run(["g++", "--version"], capture_output=True, text=True)
        if "GCC" in gcc_version.stdout:
            version = int(gcc_version.stdout.split()[3].split(".")[0])
            if version < 11:
                for ext in self.extensions:
                    ext.extra_compile_args = ["-std=c++2a"]
            else:
                for ext in self.extensions:
                    ext.extra_compile_args = ["-std=c++20"]
        super().build_extensions()

ext_modules = [
    Pybind11Extension(
        "curseforge",
        sorted(glob("src/*.cpp")),  # Sort source files for reproducibility
        cxx_std=17,
    ),
]

setup(
    name="curseforge",
    version="2.1.0",
    author="Your Name",
    description="Python bindings for the CurseForge API C++ library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
    python_requires=">=3.9",
    ext_modules=ext_modules,
)
