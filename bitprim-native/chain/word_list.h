#ifndef BITPRIM_PY_CHAIN_WORD_LIST_H_
#define BITPRIM_PY_CHAIN_WORD_LIST_H_

#include <Python.h>

#ifdef __cplusplus
extern "C" {  
#endif  

PyObject* bitprim_native_word_list_construct(PyObject* self, PyObject* args);
PyObject* bitprim_native_word_list_destruct(PyObject* self, PyObject* args);
PyObject* bitprim_native_word_list_add_word(PyObject* self, PyObject* args);

#ifdef __cplusplus
} //extern "C"
#endif  

#endif
