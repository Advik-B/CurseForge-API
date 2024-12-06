#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(curseforge_bindings, m) {
    m.def("add", [](int i, int j) { return i + j; });
}
