#include <pybind11/pybind11.h>

namespace py = pybind11;
const version = "0.1.0";


PYBIND11_MODULE(curseforge, m) {
    m.def("add", [](int i, int j) { return i + j; });
}
