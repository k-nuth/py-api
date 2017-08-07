#ifndef BITPRIM_PY_CHAIN_OUTPUT_LIST_H_
#define BITPRIM_PY_CHAIN_OUTPUT_LIST_H_

#include <Python.h>
#include <bitprim/nodecint.h>
#include "../utils.h"

PyObject* bitprim_native_output_list_push_back(PyObject* self, PyObject* args);
PyObject* bitprim_native_output_list_count(PyObject* self, PyObject* args);
PyObject* bitprim_native_output_list_nth(PyObject* self, PyObject* args);


#endif
