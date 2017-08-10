#include "block_list.h"
#include <bitprim/nodecint.h>
#include "../utils.h" //TODO(fernando): poner bien el dir del header

#ifdef __cplusplus
extern "C" {  
#endif  

PyObject* bitprim_native_chain_block_list_construct_default(PyObject* self, PyObject* args){
    block_list_t res = (block_list_t)chain_block_list_construct_default();
    return to_py_obj(res);
}

PyObject* bitprim_native_chain_block_list_push_back(PyObject* self, PyObject* args){
    PyObject* py_block_list;
    PyObject* py_block;

    if ( ! PyArg_ParseTuple(args, "OO", &py_block_list, &py_block)) {
        return NULL;
    }

    block_list_t block_list = (block_list_t)get_ptr(py_block_list);
    block_t block = (block_t)get_ptr(py_block);
    chain_block_list_push_back(block_list, block);
    Py_RETURN_NONE;
}

PyObject* bitprim_native_chain_block_list_destruct(PyObject* self, PyObject* args){
   PyObject* py_block_list;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_block_list)) {
        return NULL;
    }

    block_list_t block_list = (block_list_t)get_ptr(py_block_list);
    chain_block_list_destruct(block_list);
    Py_RETURN_NONE;
}

PyObject* bitprim_native_chain_block_list_count(PyObject* self, PyObject* args){
    PyObject* py_block_list;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_block_list)) {
        return NULL;
    }

    block_list_t block_list = (block_list_t)get_ptr(py_block_list);
    uint64_t res = chain_block_list_count(block_list);
    return Py_BuildValue("K", res);
}

PyObject* bitprim_native_chain_block_list_nth(PyObject* self, PyObject* args){
    PyObject* py_block_list;
    uint64_t py_n;

    if ( ! PyArg_ParseTuple(args, "OK", &py_block_list, &py_n)) {
        return NULL;
    }
    block_list_t block_list = (block_list_t)get_ptr(py_block_list);
    block_t res = chain_block_list_nth(block_list, py_n);
    return to_py_obj(res);
}

#ifdef __cplusplus
} //extern "C"
#endif  
