#include "input_list.h"

#ifdef __cplusplus
extern "C" {  
#endif  

PyObject* bitprim_native_input_list_push_back(PyObject* self, PyObject* args){
    PyObject* py_input_list;
    PyObject* py_input;

    if ( ! PyArg_ParseTuple(args, "OO", &py_input_list, &py_input)) {
        return NULL;
    }

    input_t input = (input_t)get_ptr(py_input);
    input_list_t input_list = (input_list_t)get_ptr(py_input_list);
    chain_input_list_push_back(input_list, input);
    //return Py_BuildValue("O", res);
    Py_RETURN_NONE;
}

PyObject* bitprim_native_input_list_count(PyObject* self, PyObject* args){
    PyObject* py_input_list;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_input_list)) {
        return NULL;
    }

    input_list_t input_list = (input_list_t)get_ptr(py_input_list);
    uint64_t res = chain_input_list_count(input_list);
    return Py_BuildValue("K", res);
}

PyObject* bitprim_native_input_list_nth(PyObject* self, PyObject* args){
    PyObject* py_input_list;
    uint64_t py_n;

    if ( ! PyArg_ParseTuple(args, "OK", &py_input_list, &py_n)) {
        return NULL;
    }
    input_list_t input_list = (input_list_t)get_ptr(py_input_list);
    input_t res = chain_input_list_nth(input_list, py_n);
    return to_py_obj(res);
}

#ifdef __cplusplus
} //extern "C"
#endif  
