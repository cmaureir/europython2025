#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>
#include <filesystem>
namespace fs = std::filesystem;

namespace nb = nanobind;

using namespace nb::literals;

nb::list glob(std::string directory, bool recursive) {
    PyObject *l = PyList_New(0);

    // Filling the list depending if it's recursive or not
    if (recursive) {
        for (const auto &entry : fs::recursive_directory_iterator(directory))
            PyList_Append(l, PyUnicode_FromString(entry.path().c_str()));
    } else {
        for (const auto &entry : fs::directory_iterator(directory))
            PyList_Append(l, PyUnicode_FromString(entry.path().c_str()));
    }
    return nb::list(l);
}

NB_MODULE(nanobind_glob_ext, m) {
    m.doc() = "This is a \"glob\" example with nanobind";
    m.def("glob", &glob);
}
