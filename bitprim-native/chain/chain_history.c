#include "chain_history.h"

// -------------------------------------------------------------------
// history_compact_list
// -------------------------------------------------------------------

PyObject* bitprim_native_history_compact_list_destruct(PyObject* self, PyObject* args) {
    PyObject* py_history_compact_list;

    if ( ! PyArg_ParseTuple(args, "O", &py_history_compact_list)) {
        // printf("bitprim_native_history_compact_list_count - 2\n");
        return NULL;
    }

    // history_compact_list_t list = (executor_t)PyCObject_AsVoidPtr(py_history_compact_list);
    history_compact_list_t list = (history_compact_list_t)get_ptr(py_history_compact_list);
    chain_history_compact_list_destruct(list);

    Py_RETURN_NONE;
}

PyObject* bitprim_native_history_compact_list_count(PyObject* self, PyObject* args) {
    PyObject* py_history_compact_list;

    if ( ! PyArg_ParseTuple(args, "O", &py_history_compact_list)) {
        // printf("bitprim_native_history_compact_list_count - 2\n");
        return NULL;
    }

    // history_compact_list_t list = (executor_t)PyCObject_AsVoidPtr(py_history_compact_list);
    history_compact_list_t list = (history_compact_list_t)get_ptr(py_history_compact_list);
    size_t res = chain_history_compact_list_count(list);

    return Py_BuildValue("i", res);
}

PyObject* bitprim_native_history_compact_list_nth(PyObject* self, PyObject* args) {
    PyObject* py_history_compact_list;
    Py_ssize_t py_n;

    if ( ! PyArg_ParseTuple(args, "On", &py_history_compact_list, &py_n)) {
        // printf("bitprim_native_history_compact_list_count - 2\n");
        return NULL;
    }

    // history_compact_list_t list = (executor_t)PyCObject_AsVoidPtr(py_history_compact_list);
    history_compact_list_t list = (history_compact_list_t)get_ptr(py_history_compact_list);
    history_compact_t hc = chain_history_compact_list_nth(list, py_n);

// #if PY_MAJOR_VERSION >= 3
//     PyObject* py_hc = PyCapsule_New(hc, NULL, NULL);
// #else /* PY_MAJOR_VERSION >= 3 */
//     PyObject* py_hc = PyCObject_FromVoidPtr(hc, NULL);
// #endif /* PY_MAJOR_VERSION >= 3 */
    
    PyObject* py_hc = to_py_obj(hc);
    return Py_BuildValue("O", py_hc);
}

// -------------------------------------------------------------------


// -------------------------------------------------------------------
// history_compact
// -------------------------------------------------------------------

PyObject* bitprim_native_history_compact_get_point_kind(PyObject* self, PyObject* args) {
    PyObject* py_history_compact;

    if ( ! PyArg_ParseTuple(args, "O", &py_history_compact)) {
        // printf("bitprim_native_history_compact_get_point_kind - 2\n");
        return NULL;
    }

    // history_compact_t hist = (history_compact_t)PyCObject_AsVoidPtr(py_history_compact);
    history_compact_t hist = (history_compact_t)get_ptr(py_history_compact);
    uint64_t res = chain_history_compact_get_point_kind(hist);

    return Py_BuildValue("K", res);
}

PyObject* bitprim_native_history_compact_get_point(PyObject* self, PyObject* args) {
    PyObject* py_history_compact;

    if ( ! PyArg_ParseTuple(args, "O", &py_history_compact)) {
        // printf("bitprim_native_history_compact_get_point - 2\n");
        return NULL;
    }

    // history_compact_t hist = (history_compact_t)PyCObject_AsVoidPtr(py_history_compact);
    history_compact_t hist = (history_compact_t)get_ptr(py_history_compact);
    point_t p = chain_history_compact_get_point(hist);

    // printf("bitprim_native_history_compact_get_point - p: %p\n", p);


// #if PY_MAJOR_VERSION >= 3
//     PyObject* py_p = PyCapsule_New(p, NULL, NULL);
// #else /* PY_MAJOR_VERSION >= 3 */
//     PyObject* py_p = PyCObject_FromVoidPtr(p, NULL);
// #endif /* PY_MAJOR_VERSION >= 3 */
    PyObject* py_p = to_py_obj(p);
    return Py_BuildValue("O", py_p);
}

PyObject* bitprim_native_history_compact_get_height(PyObject* self, PyObject* args) {
    PyObject* py_history_compact;

    if ( ! PyArg_ParseTuple(args, "O", &py_history_compact)) {
        // printf("bitprim_native_history_compact_get_height - 2\n");
        return NULL;
    }

    // history_compact_t hist = (history_compact_t)PyCObject_AsVoidPtr(py_history_compact);
    history_compact_t hist = (history_compact_t)get_ptr(py_history_compact);
    uint64_t res = chain_history_compact_get_height(hist);

    return Py_BuildValue("K", res);
}

PyObject* bitprim_native_history_compact_get_value_or_previous_checksum(PyObject* self, PyObject* args) {
    PyObject* py_history_compact;

    if ( ! PyArg_ParseTuple(args, "O", &py_history_compact)) {
        // printf("bitprim_native_history_compact_get_value_or_previous_checksum - 2\n");
        return NULL;
    }

    // history_compact_t hist = (history_compact_t)PyCObject_AsVoidPtr(py_history_compact);
    history_compact_t hist = (history_compact_t)get_ptr(py_history_compact);
    uint64_t res = chain_history_compact_get_value_or_previous_checksum(hist);

    return Py_BuildValue("K", res);
}


