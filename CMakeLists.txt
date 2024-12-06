cmake_minimum_required(VERSION 3.15...3.29)
project(curseforge-bindings LANGUAGES CXX)

set(PYBIND11_FINDPYTHON ON)
set(CMAKE_CXX_STANDARD 20)

add_subdirectory(extern/pybind11)
add_subdirectory(extern/curseforge)

include_directories(${CMAKE_SOURCE_DIR}/extern/curseforge/include)

pybind11_add_module(curseforge-bindings src/bindings.cpp)
target_link_libraries(curseforge-bindings PUBLIC curseforge::shared)
install(TARGETS curseforge-bindings DESTINATION .)
