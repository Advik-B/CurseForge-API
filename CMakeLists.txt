cmake_minimum_required(VERSION 3.4...3.30)
project(PyCurseForge LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
add_subdirectory(pybind11)
add_subdirectory(CurseForge-API-CPP)
pybind11_add_module(curseforge_bindings src/binder.cpp)
# Rename the output to curseforge so that it can be imported as curseforge
set_target_properties(curseforge_bindings PROPERTIES OUTPUT_NAME "curseforge")
target_link_libraries(curseforge_bindings PRIVATE curseforge::static)
target_include_directories(curseforge_bindings PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/CurseForge-API-CPP/include)