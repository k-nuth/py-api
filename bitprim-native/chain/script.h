#ifndef BITPRIM_PY_CHAIN_SCRIPT_H_
#define BITPRIM_PY_CHAIN_SCRIPT_H_

#include <Python.h>
#include <bitprim/nodecint.h>
#include "../utils.h"

#ifdef __cplusplus
extern "C" {  
#endif  

PyObject* bitprim_native_chain_script_destruct(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_script_is_valid(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_script_is_valid_operations(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_script_satoshi_content_size(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_script_serialized_size(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_script_to_string(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_script_sigops(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_script_embedded_sigops(PyObject* self, PyObject* args);


#ifdef __cplusplus
} //extern "C"
#endif  

#endif
