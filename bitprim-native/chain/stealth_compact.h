#ifndef BITPRIM_PY_CHAIN_STEALTH_COMPACT_H_
#define BITPRIM_PY_CHAIN_STEALTH_COMPACT_H_

#include <Python.h>

#ifdef __cplusplus
extern "C" {  
#endif  

PyObject* bitprim_native_stealth_compact_get_ephemeral_public_key_hash(PyObject* self, PyObject* args);
PyObject* bitprim_native_stealth_compact_get_transaction_hash(PyObject* self, PyObject* args);
PyObject* bitprim_native_stealth_compact_get_public_key_hash(PyObject* self, PyObject* args);

#ifdef __cplusplus
} //extern "C"
#endif  

#endif
