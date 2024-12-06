cmake_minimum_required(VERSION 3.15...3.29)
project(curseforge-bindings LANGUAGES CXX)

set(PYBIND11_FINDPYTHON ON)
add_subdirectory(extern/pybind11)

pybind11_add_module(curseforge-bindings src/bindings.cpp)
# target_link_libraries(curseforge-bindings PRIVATE curseforge::static)
install(TARGETS curseforge-bindings DESTINATION .)
