#ifndef BITPRIM_PY_CHAIN_INPUT_H_
#define BITPRIM_PY_CHAIN_INPUT_H_

#include <Python.h>
#include <bitprim/nodecint.h>
#include "../utils.h"


PyObject* bitprim_native_chain_input_is_valid(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_input_is_final(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_input_serialized_size(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_input_sequence(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_input_signature_operations(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_input_destruct(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_input_script(PyObject* self, PyObject* args);
//PyObject* bitprim_native_chain_input_get_hash(PyObject* self, PyObject* args);
//PyObject* bitprim_native_chain_input_get_index(PyObject* self, PyObject* args);


/*
BITPRIM_EXPORT
input_t chain_input_construct_default();

//input(uint64_t value, chain::script&& script);
//input(uint64_t value, const chain::script& script);
BITPRIM_EXPORT
input_t chain_input_construct(uint64_t value, script_t script);

BITPRIM_EXPORT
void chain_input_destruct(input_t input);

BITPRIM_EXPORT
int chain_input_is_valid(input_t input);

BITPRIM_EXPORT
uint64_t chain_input_serialized_size(input_t input, int wire );

BITPRIM_EXPORT
uint64_t chain_input_value(input_t input);

BITPRIM_EXPORT
uint64_t chain_input_signature_operations(input_t input);

BITPRIM_EXPORT
script_t chain_input_script(input_t input);

BITPRIM_EXPORT
hash_t chain_input_get_hash(input_t input);

BITPRIM_EXPORT
uint32_t chain_input_get_index(input_t input);

*/

#endif
