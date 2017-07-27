#ifndef BITPRIM_PY_CHAIN_TRANSACTION_H_
#define BITPRIM_PY_CHAIN_TRANSACTION_H_

#include <Python.h>
#include <bitprim/nodecint.h>
#include "../utils.h"

PyObject* bitprim_native_chain_transaction_version(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_set_version(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_hash(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_hash_sighash_type(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_locktime(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_serialized_size(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_fees(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_signature_operations(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_signature_operations_bip16_active(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_total_input_value(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_total_output_value(PyObject* self, PyObject* args);

/*
PyObject* bitprim_native_chain_transaction_is_coinbase(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_is_null_non_coinbase(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_is_oversized_coinbase(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_is_immature(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_is_overspent(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_is_double_spend(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_is_missing_previous_outputs(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_is_final(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_is_locktime_conflict(PyObject* self, PyObject* args);
*/

//PyObject* bitprim_native_chain_transaction_outputs(PyObject* self, PyObject* args);
//PyObject* bitprim_native_chain_transaction_inputs(PyObject* self, PyObject* args);

/*
BITPRIM_EXPORT
uint32_t chain_transaction_version(transaction_t transaction);

BITPRIM_EXPORT
void chain_transaction_set_version(transaction_t transaction, uint32_t version);

BITPRIM_EXPORT
hash_t chain_transaction_hash(transaction_t transaction);

BITPRIM_EXPORT
hash_t chain_transaction_hash_sighash_type(transaction_t transaction, uint32_t sighash_type);

BITPRIM_EXPORT
uint32_t chain_transaction_locktime(transaction_t transaction);

BITPRIM_EXPORT
uint64_t chain_transaction_serialized_size(transaction_t transaction, int wire);

BITPRIM_EXPORT
uint64_t chain_transaction_fees(transaction_t transaction);

BITPRIM_EXPORT
uint64_t chain_transaction_signature_operations(transaction_t transaction);

BITPRIM_EXPORT
uint64_t chain_transaction_signature_operations_bip16_active(transaction_t transaction, intbip16_active);

BITPRIM_EXPORT
uint64_t chain_transaction_total_input_value(transaction_t transaction);

BITPRIM_EXPORT
uint64_t chain_transaction_total_output_value(transaction_t transaction);

BITPRIM_EXPORT
int chain_transaction_is_coinbase(transaction_t transaction);

BITPRIM_EXPORT
int chain_transaction_is_null_non_coinbase(transaction_t transaction);

BITPRIM_EXPORT
int chain_transaction_is_oversized_coinbase(transaction_t transaction);

BITPRIM_EXPORT
int chain_transaction_is_immature(transaction_t transaction, uint64_ttarget_height);

BITPRIM_EXPORT
int chain_transaction_is_overspent(transaction_t transaction);

BITPRIM_EXPORT
int chain_transaction_is_double_spend(transaction_t transaction, intinclude_unconfirmed);

BITPRIM_EXPORT
int chain_transaction_is_missing_previous_outputs(transaction_t transaction);

BITPRIM_EXPORT
int chain_transaction_is_final(transaction_t transaction, uint64_tblock_height, uint32_t block_time);

BITPRIM_EXPORT
int chain_transaction_is_locktime_conflict(transaction_t transaction);

BITPRIM_EXPORT
output_list_t chain_transaction_outputs(transaction_t transaction);

BITPRIM_EXPORT
input_list_t chain_transaction_inputs(transaction_t transaction);
*/

#endif
