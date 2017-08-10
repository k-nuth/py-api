#ifndef BITPRIM_PY_CHAIN_STEALTH_COMPACT_LIST_H_
#define BITPRIM_PY_CHAIN_STEALTH_COMPACT_LIST_H_

#include <Python.h>

#ifdef __cplusplus
extern "C" {  
#endif  

//PyObject* bitprim_native_chain_stealth_compact_list_construct_default(PyObject* self, PyObject* args);
//PyObject* bitprim_native_chain_stealth_compact_list_push_back(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_stealth_compact_list_destruct(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_stealth_compact_list_count(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_stealth_compact_list_nth(PyObject* self, PyObject* args);

#ifdef __cplusplus
} //extern "C"
#endif  

#endif
