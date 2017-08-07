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


PyObject* bitprim_native_chain_transaction_is_coinbase(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_is_null_non_coinbase(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_is_oversized_coinbase(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_is_immature(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_is_overspent(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_is_double_spend(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_is_missing_previous_outputs(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_is_final(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_is_locktime_conflict(PyObject* self, PyObject* args);

PyObject* bitprim_native_chain_transaction_destruct(PyObject* self, PyObject* args);


//PyObject* bitprim_native_chain_transaction_outputs(PyObject* self, PyObject* args);
//PyObject* bitprim_native_chain_transaction_inputs(PyObject* self, PyObject* args);

#endif
