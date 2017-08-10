#ifndef BITPRIM_PY_CHAIN_INPUT_H_
#define BITPRIM_PY_CHAIN_INPUT_H_

#include <Python.h>
#include <bitprim/nodecint.h>
#include "../utils.h"

#ifdef __cplusplus
extern "C" {  
#endif  


PyObject* bitprim_native_chain_input_is_valid(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_input_is_final(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_input_serialized_size(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_input_sequence(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_input_signature_operations(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_input_destruct(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_input_script(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_input_previous_output(PyObject* self, PyObject* args);
//PyObject* bitprim_native_chain_input_get_hash(PyObject* self, PyObject* args);
//PyObject* bitprim_native_chain_input_get_index(PyObject* self, PyObject* args);



#ifdef __cplusplus
} //extern "C"
#endif  


#endif
