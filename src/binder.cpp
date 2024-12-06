#include <pybind11/pybind11.h>
#include <CurseForgeAPI.hpp>

const auto version = "2.0.0";

namespace py = pybind11;


PYBIND11_MODULE(curseforge, m) {
    m.doc() = "Python bindings for the CurseForge API Wrapper";
    m.attr("__version__") = version;
    
}
