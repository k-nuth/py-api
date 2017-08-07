#ifndef BITPRIM_PY_CHAIN_OUTPUT_POINT_H_
#define BITPRIM_PY_CHAIN_OUTPUT_POINT_H_

#include <Python.h>
#include <bitprim/nodecint.h>
#include "../utils.h"


PyObject * bitprim_native_chain_output_point_get_hash(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_output_point_construct(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_output_point_construct_from_hash_index(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_output_point_get_index(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_output_point_destruct(PyObject* self, PyObject* args);

#endif



/*
BITPRIM_EXPORT
hash_t output_point_get_hash(output_point_t output);

BITPRIM_EXPORT
output_point_t output_point_construct();

BITPRIM_EXPORT
uint32_t output_point_get_index(output_point_t output);

BITPRIM_EXPORT
void output_point_destruct(output_point_t output);

*/
