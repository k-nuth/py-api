#ifndef BITPRIM_PY_CHAIN_PAYMENT_ADDRESS_H_
#define BITPRIM_PY_CHAIN_PAYMENT_ADDRESS_H_

#include <Python.h>
#include <bitprim/nodecint.h>
#include "../utils.h"

#ifdef __cplusplus
extern "C" {  
#endif  

PyObject* bitprim_native_chain_payment_address_destruct(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_payment_address_encoded(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_payment_address_version(PyObject* self, PyObject* args);
PyObject* bitprim_native_chain_payment_address_construct_from_string(PyObject* self, PyObject* args);

#ifdef __cplusplus
} //extern "C"
#endif  

#endif
