cmake_minimum_required(VERSION 3.15...3.29)
project(curseforge-bindings LANGUAGES CXX)

set(PYBIND11_FINDPYTHON ON)
add_subdirectory(extern/pybind11)

include(FetchContent)
FetchContent_Declare(
    cfapi
    GIT_REPOSITORY https://github.com/Advik-B/CurseForge-API-CPP.git
    GIT_TAG        v1.0.0
)
FetchContent_MakeAvailable(cfapi)

pybind11_add_module(curseforge-bindings src/bindings.cpp)
target_link_libraries(curseforge-bindings PRIVATE curseforge::static)
install(TARGETS curseforge-bindings DESTINATION .)
