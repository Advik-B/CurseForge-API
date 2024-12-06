from setuptools import setup
from skbuild import setup as sk_setup
from glob import glob
from pybind11.setup_helpers import Pybind11Extension
import subprocess, os


# This class defines how CMake will be used to build the extension
class CMakeExtension(Pybind11Extension):
    def __init__(self, name, sources, **kwargs):
        super().__init__(name, sources, **kwargs)

    def finalize_options(self):
        super().finalize_options()
        # Specify CMake source and build directories
        self.build_temp = self.build_temp or self._get_build_temp()
        self.build_lib = self.build_lib or self._get_build_lib()

    def _get_build_temp(self):
        return "build/temp"

    def _get_build_lib(self):
        return "build/lib"

ext_modules = [
    CMakeExtension(
        "curseforge",
        sorted(glob("src/*.cpp")),  # Sort source files for reproducibility
        # cxx_std=17,
    ),
]

# Ensure CMake can find your headers
cmake_args = [
    "-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={}".format(os.path.join(os.path.abspath("."), "build")),
    "-DCMAKE_BUILD_TYPE=Release",
    "-DHEADER_PATH={}".format(os.path.abspath("extern/curseforge/include")),
]

# Use scikit-build to invoke CMake
sk_setup(
    name="curseforge",
    version="2.0.0",
    author="Advik",
    description="Python bindings for the CurseForge API C++ library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
    python_requires=">=3.9",
    ext_modules=ext_modules,
    cmake_args=cmake_args,
)
