#include "transaction_list.h"
#include <bitprim/nodecint.h>
#include "../utils.h"

#ifdef __cplusplus
extern "C" {  
#endif  

PyObject* bitprim_native_chain_transaction_list_construct_default(PyObject* self, PyObject* args){
    transaction_list_t res = (transaction_list_t)chain_transaction_list_construct_default();
    return to_py_obj(res);
}

PyObject* bitprim_native_chain_transaction_list_push_back(PyObject* self, PyObject* args){
    PyObject* py_transaction_list;
    PyObject* py_transaction;

    if ( ! PyArg_ParseTuple(args, "OO", &py_transaction_list, &py_transaction)) {
        return NULL;
    }

    transaction_list_t transaction_list = (transaction_list_t)get_ptr(py_transaction_list);
    transaction_t transaction = (transaction_t)get_ptr(py_transaction);
    chain_transaction_list_push_back(transaction_list, transaction);
    Py_RETURN_NONE;
}

PyObject* bitprim_native_chain_transaction_list_destruct(PyObject* self, PyObject* args){
   PyObject* py_transaction_list;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_transaction_list)) {
        return NULL;
    }

    transaction_list_t transaction_list = (transaction_list_t)get_ptr(py_transaction_list);
    chain_transaction_list_destruct(transaction_list);
    Py_RETURN_NONE;
}


PyObject* bitprim_native_chain_transaction_list_count(PyObject* self, PyObject* args){
    PyObject* py_transaction_list;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_transaction_list)) {
        return NULL;
    }

    transaction_list_t transaction_list = (transaction_list_t)get_ptr(py_transaction_list);
    uint64_t res = chain_transaction_list_count(transaction_list);
    return Py_BuildValue("K", res);
}

PyObject* bitprim_native_chain_transaction_list_nth(PyObject* self, PyObject* args){
    PyObject* py_transaction_list;
    uint64_t py_n;

    if ( ! PyArg_ParseTuple(args, "OK", &py_transaction_list, &py_n)) {
        return NULL;
    }
    transaction_list_t transaction_list = (transaction_list_t)get_ptr(py_transaction_list);
    transaction_t res = chain_transaction_list_nth(transaction_list, py_n);
    return to_py_obj(res);
}

#ifdef __cplusplus
} //extern "C"
#endif  
