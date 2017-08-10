#include "stealth_compact.h"
#include <bitprim/nodecint.h>
#include "../utils.h" //TODO(fernando): poner bien el dir del header

#ifdef __cplusplus
extern "C" {  
#endif  

PyObject* bitprim_native_stealth_compact_get_ephemeral_public_key_hash(PyObject* self, PyObject* args){
    PyObject* py_stealth;

    if ( ! PyArg_ParseTuple(args, "O", &py_stealth)) {
        return NULL;
    }

    stealth_compact_t stealth = (stealth_compact_t)get_ptr(py_stealth);
    hash_t res = stealth_compact_get_ephemeral_public_key_hash(stealth);

#if PY_MAJOR_VERSION >= 3
    return Py_BuildValue("y#", res.hash, 32); //TODO: warning, hardcoded hash size!   
#else
    return Py_BuildValue("s#", res.hash, 32);    
#endif
}

PyObject* bitprim_native_stealth_compact_get_transaction_hash(PyObject* self, PyObject* args){
    PyObject* py_stealth;

    if ( ! PyArg_ParseTuple(args, "O", &py_stealth)) {
        return NULL;
    }

    stealth_compact_t stealth = (stealth_compact_t)get_ptr(py_stealth);
    hash_t res = stealth_compact_get_transaction_hash(stealth);

#if PY_MAJOR_VERSION >= 3
    return Py_BuildValue("y#", res.hash, 32); //TODO: warning, hardcoded hash size!
#else
    return Py_BuildValue("s#", res.hash, 32);
#endif
}

PyObject* bitprim_native_stealth_compact_get_public_key_hash(PyObject* self, PyObject* args){
    PyObject* py_stealth;

    if ( ! PyArg_ParseTuple(args, "O", &py_stealth)) {
        return NULL;
    }

    stealth_compact_t stealth = (stealth_compact_t)get_ptr(py_stealth);
    short_hash_t res = stealth_compact_get_public_key_hash(stealth);

#if PY_MAJOR_VERSION >= 3
    return Py_BuildValue("y#", res.hash, 20);    //TODO: warning, hardcoded hash size!
#else
    return Py_BuildValue("s#", res.hash, 20);    //TODO: warning, hardcoded hash size!
#endif
}

#ifdef __cplusplus
} //extern "C"
#endif  
