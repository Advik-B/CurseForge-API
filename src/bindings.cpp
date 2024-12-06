#include <pybind11/pybind11.h>

namespace py = pybind11;


PYBIND11_MODULE(curseforge, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring

    m.def("add", &add, "A function which adds two numbers");
}