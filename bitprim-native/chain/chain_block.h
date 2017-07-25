#include <Python.h>
#include <bitprim/nodecint.h>
#include "../utils.h"


PyObject * bitprim_native_chain_block_get_header(PyObject* self, PyObject* args);


PyObject * bitprim_native_chain_block_transaction_count(PyObject* self, PyObject* args);


PyObject * bitprim_native_chain_block_serialized_size(PyObject* self, PyObject* args);


PyObject * bitprim_native_chain_block_subsidy(PyObject* self, PyObject* args);


PyObject * bitprim_native_chain_block_fees(PyObject* self, PyObject* args);


PyObject * bitprim_native_chain_block_claim(PyObject* self, PyObject* args);


PyObject * bitprim_native_chain_block_reward(PyObject* self, PyObject* args);


PyObject * bitprim_native_chain_block_generate_merkle_root(PyObject* self, PyObject* args);


PyObject * bitprim_native_chain_block_hash(PyObject* self, PyObject* args);
