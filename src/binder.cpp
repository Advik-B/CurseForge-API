#include <pybind11/pybind11.h>
#include <nlohmann/json.hpp>

#include <CurseForgeAPI.hpp>
#include <CurseFileRelationType.hpp>
#include <CurseFileDependency.hpp>
#include <CurseCategory.hpp>
#include <CurseErrors.hpp>

// #include <cpr/cpr.h>

const auto version = "2.0.0";

namespace py = pybind11;
using json = nlohmann::json;

void register_errors_submodule(py::module_ &parent) {
    auto m = parent.def_submodule("errors", "CurseForge API Errors");

    py::register_exception<cf::errors::CurseAPIError>(m, "CurseAPIError");
    py::register_exception<cf::errors::NotFoundError>(m, "NotFoundError", PyExc_LookupError);
    py::register_exception<cf::errors::InvalidAPIKeyError>(m, "InvalidAPIKeyError", PyExc_ValueError);
}

void register_enums_submodule(py::module_ &parent) {
    auto m = parent.def_submodule("enums", "CurseForge API Enums");

    py::enum_<cf::CurseFileRelationType>(m, "CurseFileRelationType")
        .value("EMBEDDED_LIBRARY", cf::CurseFileRelationType::EMBEDDED_LIBRARY)
        .value("OPTIONAL_DEPENDENCY", cf::CurseFileRelationType::OPTIONAL_DEPENDENCY)
        .value("REQUIRED_DEPENDENCY", cf::CurseFileRelationType::REQUIRED_DEPENDENCY)
        .value("TOOL", cf::CurseFileRelationType::TOOL)
        .value("INCOMPATIBLE", cf::CurseFileRelationType::INCOMPATIBLE)
        .value("INCLUDE", cf::CurseFileRelationType::INCLUDE);
}

PYBIND11_MODULE(curseforge, m) {
    m.doc() = "Python bindings for the CurseForge API Wrapper";
    m.attr("__version__") = version;

    
    py::class_<json>(m, "json")
        .def(py::init<>())
        .def_static("parse", [](const std::string &s) { return json::parse(s); })
        .def("dump", &json::dump)
        .def_static("from_dict", [](const py::dict &d) { return d.cast<json>(); });

    py::class_<

    py::class_<cf::CurseForgeAPI>(m, "CurseForgeAPI")
        .def(py::init<const std::string &>())
        .def("fetch", &cf::CurseForgeAPI::fetch);
    
    
    py::class_<cf::CurseFileDependency>(m, "CurseFileDependency")
        .def_readonly("modId", &cf::CurseFileDependency::modId)
        .def_readonly("relationType", &cf::CurseFileDependency::relationType)
        .def_static("from_json", &cf::CurseFileDependency::from_json);

    py::class_<cf::CurseCategory>(m, "CurseCategory")
        .def_readonly("id", &cf::CurseCategory::id)
        .def_readonly("gameId", &cf::CurseCategory::gameId)
        .def_readonly("name", &cf::CurseCategory::name)
        .def_readonly("slug", &cf::CurseCategory::slug)
        .def_readonly("url", &cf::CurseCategory::url)
        .def_readonly("iconUrl", &cf::CurseCategory::iconUrl)
        .def_readonly("dateModified", &cf::CurseCategory::dateModified)
        .def_readonly("isClass", &cf::CurseCategory::isClass)
        .def_readonly("classId", &cf::CurseCategory::classId)
        .def_readonly("parentCategoryId", &cf::CurseCategory::parentCategoryId)
        .def_readonly("displayIndex", &cf::CurseCategory::displayIndex)
        .def_static("from_json", &cf::CurseCategory::from_json)
        .def_static("from_id", &cf::CurseCategory::from_id);

    register_errors_submodule(m);
    register_enums_submodule(m);   

}
