#include "chain_point.h"

// -------------------------------------------------------------------
// point
// -------------------------------------------------------------------

// hash_t point_get_hash(point_t point){
// int /*bool*/ point_is_valid(point_t point){
// uint32_t point_get_index(point_t point){
// uint64_t point_get_checksum(point_t point){


PyObject* bitprim_native_point_get_hash(PyObject* self, PyObject* args) {
    PyObject* py_point;
    //printf("bitprim_native_point_get_hash - 1\n");

    if ( ! PyArg_ParseTuple(args, "O", &py_point)) {
        // printf("bitprim_native_point_get_hash - 2\n");
        return NULL;
    }

    //printf("bitprim_native_point_get_hash - 3\n");

    // point_t p = (point_t)PyCObject_AsVoidPtr(py_point);
    point_t p = (point_t)get_ptr(py_point);

    //printf("bitprim_native_point_get_hash - p: %p\n", p);

    hash_t res = point_get_hash(p);

    //printf("bitprim_native_point_get_hash - 4\n");

    return Py_BuildValue("y#", res, 32);    //TODO: warning, hardcoded hash size!
}


PyObject* bitprim_native_point_is_valid(PyObject* self, PyObject* args) {
    PyObject* py_point;

    if ( ! PyArg_ParseTuple(args, "O", &py_point)) {
        // printf("bitprim_native_point_is_valid - 2\n");
        return NULL;
    }

    // point_t p = (point_t)PyCObject_AsVoidPtr(py_point);
    point_t p = (point_t)get_ptr(py_point);
    int res = point_is_valid(p);

    if (res == 0) {
        Py_RETURN_FALSE;
    }

    Py_RETURN_TRUE;
}


PyObject* bitprim_native_point_get_index(PyObject* self, PyObject* args) {
    PyObject* py_point;

    if ( ! PyArg_ParseTuple(args, "O", &py_point)) {
        // printf("bitprim_native_point_get_index - 2\n");
        return NULL;
    }

    // point_t p = (point_t)PyCObject_AsVoidPtr(py_point);
    point_t p = (point_t)get_ptr(py_point);
    uint32_t res = point_get_index(p);
    return Py_BuildValue("K", res);
}

PyObject* bitprim_native_point_get_checksum(PyObject* self, PyObject* args) {
    PyObject* py_point;

    if ( ! PyArg_ParseTuple(args, "O", &py_point)) {
        // printf("bitprim_native_point_get_checksum - 2\n");
        return NULL;
    }

    // point_t p = (point_t)PyCObject_AsVoidPtr(py_point);
    point_t p = (point_t)get_ptr(py_point);
    uint64_t res = point_get_checksum(p);

    return Py_BuildValue("K", res);
}

