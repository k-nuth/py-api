#include "stealth_compact_list.h"
#include <bitprim/nodecint.h>
#include "../utils.h"

#ifdef __cplusplus
extern "C" {  
#endif  


/*
PyObject* bitprim_native_chain_stealth_compact_list_construct_default(PyObject* self, PyObject* args){
    stealth_compact_list_t res = (stealth_compact_list_t)chain_stealth_compact_list_construct_default();
    return to_py_obj(res);
}


PyObject* bitprim_native_chain_stealth_compact_list_push_back(PyObject* self, PyObject* args){
    PyObject* py_stealth_compact_list;
    PyObject* py_stealth_compact;

    if ( ! PyArg_ParseTuple(args, "OO", &py_stealth_compact_list, &py_stealth_compact)) {
        return NULL;
    }

    stealth_compact_list_t stealth_compact_list = (stealth_compact_list_t)get_ptr(py_stealth_compact_list);
    stealth_compact_t stealth_compact = (stealth_compact_t)get_ptr(py_stealth_compact);
    stealth_compact_list_push_back(stealth_compact_list, stealth_compact);
    Py_RETURN_NONE;
}
*/

PyObject* bitprim_native_chain_stealth_compact_list_destruct(PyObject* self, PyObject* args){
   PyObject* py_stealth_compact_list;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_stealth_compact_list)) {
        return NULL;
    }

    stealth_compact_list_t stealth_compact_list = (stealth_compact_list_t)get_ptr(py_stealth_compact_list);
    stealth_compact_list_destruct(stealth_compact_list);
    Py_RETURN_NONE;
}


PyObject* bitprim_native_chain_stealth_compact_list_count(PyObject* self, PyObject* args){
    PyObject* py_stealth_compact_list;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_stealth_compact_list)) {
        return NULL;
    }

    stealth_compact_list_t stealth_compact_list = (stealth_compact_list_t)get_ptr(py_stealth_compact_list);
    uint64_t res = stealth_compact_list_count(stealth_compact_list);
    return Py_BuildValue("K", res);
}


PyObject* bitprim_native_chain_stealth_compact_list_nth(PyObject* self, PyObject* args){
    PyObject* py_stealth_compact_list;
    uint64_t py_n;

    if ( ! PyArg_ParseTuple(args, "OK", &py_stealth_compact_list, &py_n)) {
        return NULL;
    }
    stealth_compact_list_t stealth_compact_list = (stealth_compact_list_t)get_ptr(py_stealth_compact_list);
    stealth_compact_t res = stealth_compact_list_nth(stealth_compact_list, py_n);
    return to_py_obj(res);
}

#ifdef __cplusplus
} //extern "C"
#endif  
