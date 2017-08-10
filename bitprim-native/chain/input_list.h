#ifndef BITPRIM_PY_CHAIN_INPUT_LIST_H_
#define BITPRIM_PY_CHAIN_INPUT_LIST_H_

#include <Python.h>
#include <bitprim/nodecint.h>
#include "../utils.h"

#ifdef __cplusplus
extern "C" {  
#endif  

PyObject* bitprim_native_input_list_push_back(PyObject* self, PyObject* args);
PyObject* bitprim_native_input_list_count(PyObject* self, PyObject* args);
PyObject* bitprim_native_input_list_nth(PyObject* self, PyObject* args);

#ifdef __cplusplus
} //extern "C" 
#endif  


#endif
