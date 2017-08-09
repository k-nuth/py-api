#ifndef BITPRIM_PY_CHAIN_TRANSACTION_LIST_H_
#define BITPRIM_PY_CHAIN_TRANSACTION_LIST_H_

#include <Python.h>

PyObject* bitprim_native_chain_transaction_list_construct_default(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_list_push_back(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_list_destruct(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_list_count(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_transaction_list_nth(PyObject* self, PyObject* args);

#endif