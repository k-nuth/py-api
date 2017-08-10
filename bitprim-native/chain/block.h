#ifndef BITPRIM_PY_CHAIN_BLOCK_H_
#define BITPRIM_PY_CHAIN_BLOCK_H_

#include <Python.h>
// #include <bitprim/nodecint.h>
// #include "../utils.h"

#ifdef __cplusplus
extern "C" {  
#endif  

PyObject* bitprim_native_chain_block_get_header(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_block_transaction_count(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_block_serialized_size(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_block_subsidy(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_block_fees(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_block_claim(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_block_reward(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_block_generate_merkle_root(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_block_hash(PyObject* self, PyObject* args);

PyObject * bitprim_native_chain_block_is_valid(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_block_transaction_nth(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_block_signature_operations(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_block_signature_operations_bip16_active(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_block_total_inputs(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_block_is_extra_coinbases(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_block_is_final(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_block_is_distinct_transaction_set(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_block_is_valid_coinbase_claim(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_block_is_valid_coinbase_script(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_block_is_internal_double_spend(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_block_is_valid_merkle_root(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_block_destruct(PyObject* self, PyObject* args);

#ifdef __cplusplus
} //extern "C"
#endif  

#endif
