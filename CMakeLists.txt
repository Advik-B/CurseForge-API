cmake_minimum_required(VERSION 3.4...3.18)
project(PyCurseForge)

add_subdirectory(pybind11)
pybind11_add_module(curseforge_bindings src/binder.cpp)
# Rename the output to curseforge so that it can be imported as curseforge
set_target_properties(curseforge_bindings PROPERTIES OUTPUT_NAME "curseforge")
