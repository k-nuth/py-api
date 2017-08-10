#ifndef BITPRIM_PY_CHAIN_OUTPUT_H_
#define BITPRIM_PY_CHAIN_OUTPUT_H_

#include <Python.h>
#include <bitprim/nodecint.h>
#include "../utils.h"

#ifdef __cplusplus
extern "C" {  
#endif  


PyObject* bitprim_native_chain_output_is_valid(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_output_serialized_size(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_output_value(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_output_signature_operations(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_output_destruct(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_output_script(PyObject* self, PyObject* args);

//PyObject* bitprim_native_chain_output_get_hash(PyObject* self, PyObject* args);
//PyObject* bitprim_native_chain_output_get_index(PyObject* self, PyObject* args);


/*
BITPRIM_EXPORT
output_t chain_output_construct_default();

//output(uint64_t value, chain::script&& script);
//output(uint64_t value, const chain::script& script);
BITPRIM_EXPORT
output_t chain_output_construct(uint64_t value, script_t script);

BITPRIM_EXPORT
void chain_output_destruct(output_t output);

BITPRIM_EXPORT
int chain_output_is_valid(output_t output);

BITPRIM_EXPORT
uint64_t chain_output_serialized_size(output_t output, int wire );

BITPRIM_EXPORT
uint64_t chain_output_value(output_t output);

BITPRIM_EXPORT
uint64_t chain_output_signature_operations(output_t output);

BITPRIM_EXPORT
script_t chain_output_script(output_t output);

BITPRIM_EXPORT
hash_t chain_output_get_hash(output_t output);

BITPRIM_EXPORT
uint32_t chain_output_get_index(output_t output);

*/


#ifdef __cplusplus
} //extern "C"
#endif  


#endif
