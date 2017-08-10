#ifndef BITPRIM_PY_CHAIN_COMPACT_BLOCK_H_
#define BITPRIM_PY_CHAIN_COMPACT_BLOCK_H_

#include <Python.h>
#include <bitprim/nodecint.h>
#include "../utils.h"


#ifdef __cplusplus
extern "C" {  
#endif  

PyObject * bitprim_native_chain_compact_block_header(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_compact_block_is_valid(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_compact_block_serialized_size(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_compact_block_transaction_count(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_compact_block_transaction_nth(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_compact_block_nonce(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_compact_block_destruct(PyObject* self, PyObject* args);
PyObject * bitprim_native_chain_compact_block_reset(PyObject* self, PyObject* args);


#ifdef __cplusplus
} //extern "C"
#endif  

#endif
