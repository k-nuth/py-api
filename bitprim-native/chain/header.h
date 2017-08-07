#ifndef BITPRIM_PY_CHAIN_HEADER_H_
#define BITPRIM_PY_CHAIN_HEADER_H_

#include <Python.h>

PyObject* bitprim_native_chain_header_get_version(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_header_set_version(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_header_get_previous_block_hash(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_header_get_merkle(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_header_get_timestamp(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_header_set_timestamp(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_header_get_bits(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_header_set_bits(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_header_get_nonce(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_header_set_nonce(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_header_destruct(PyObject* self, PyObject* args);

#endif
