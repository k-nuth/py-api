#ifndef BITPRIM_PY_CHAIN_OUTPUT_POINT_H_
#define BITPRIM_PY_CHAIN_OUTPUT_POINT_H_

#include <Python.h>
#include <bitprim/nodecint.h>
#include "../utils.h"

#ifdef __cplusplus
extern "C" {  
#endif  


PyObject * bitprim_native_chain_output_point_get_hash(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_output_point_construct(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_output_point_construct_from_hash_index(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_output_point_get_index(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_output_point_destruct(PyObject* self, PyObject* args);

#ifdef __cplusplus
} //extern "C"
#endif  

#endif
