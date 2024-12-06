#include <pybind11/pybind11.h>
#include <CurseForgeAPI.hpp>

namespace py = pybind11;
using namespace py::literals;


int add(int i, int j) {
    return i + j;
}

PYBIND11_MODULE(curseforge, m) {
    m.doc() = "CurseForge API bindings for Python";
    py::class_<cf::CurseForgeAPI>(m, "CurseForgeAPI")
        .def(py::init<const std::string &>())
        .def("fetch", &cf::CurseForgeAPI::fetch);
        
}
