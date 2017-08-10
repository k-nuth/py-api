#ifndef BITPRIM_PY_BINARY_H_
#define BITPRIM_PY_BINARY_H_

#include <Python.h>
// #include <bitprim/nodecint.h>
// #include "utils.h"

#ifdef __cplusplus
extern "C" {  
#endif  


PyObject* bitprim_native_binary_construct(PyObject* self, PyObject* args);
PyObject* bitprim_native_binary_construct_string(PyObject* self, PyObject* args);
PyObject* bitprim_native_binary_construct_blocks(PyObject* self, PyObject* args);
PyObject* bitprim_native_binary_blocks(PyObject* self, PyObject* args);
PyObject* bitprim_native_binary_encoded(PyObject* self, PyObject* args);

#ifdef __cplusplus
} // extern "C"
#endif  

#endif
