#ifndef BITPRIM_PY_CHAIN_POINT_H_
#define BITPRIM_PY_CHAIN_POINT_H_

#include <Python.h>

PyObject* bitprim_native_point_get_hash(PyObject* self, PyObject* args);
PyObject* bitprim_native_point_is_valid(PyObject* self, PyObject* args);
PyObject* bitprim_native_point_get_index(PyObject* self, PyObject* args);
PyObject* bitprim_native_point_get_checksum(PyObject* self, PyObject* args);

#endif
