#ifndef BITPRIM_PY_CHAIN_H_
#define BITPRIM_PY_CHAIN_H_

#include <Python.h>

#ifdef __cplusplus
extern "C" {  
#endif  

PyObject* bitprim_native_chain_fetch_block_by_height(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_fetch_block_by_hash(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_fetch_merkle_block_by_height(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_fetch_merkle_block_by_hash(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_fetch_block_header_by_height(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_fetch_block_header_by_hash(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_fetch_last_height(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_fetch_history(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_fetch_block_height(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_fetch_stealth(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_fetch_transaction(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_fetch_output(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_fetch_transaction_position(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_organize_block(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_organize_transaction(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_validate_tx(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_fetch_compact_block_by_hash(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_fetch_compact_block_by_height(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_fetch_spend(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_subscribe_reorganize(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_subscribe_transaction(PyObject* self, PyObject* args);

#ifdef __cplusplus
} //extern "C"
#endif  

#endif
