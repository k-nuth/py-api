#include "output_list.h"

#ifdef __cplusplus
extern "C" {  
#endif  

PyObject* bitprim_native_output_list_push_back(PyObject* self, PyObject* args){
    PyObject* py_output_list;
    PyObject* py_output;

    if ( ! PyArg_ParseTuple(args, "OO", &py_output_list, &py_output)) {
        return NULL;
    }

    output_t output = (output_t)get_ptr(py_output);
    output_list_t output_list = (output_list_t)get_ptr(py_output_list);
    chain_output_list_push_back(output_list, output);
    //return Py_BuildValue("O", res);
    Py_RETURN_NONE;
}

PyObject* bitprim_native_output_list_count(PyObject* self, PyObject* args){
    PyObject* py_output_list;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_output_list)) {
        return NULL;
    }

    output_list_t output_list = (output_list_t)get_ptr(py_output_list);
    uint64_t res = chain_output_list_count(output_list);
    return Py_BuildValue("K", res);
}

PyObject* bitprim_native_output_list_nth(PyObject* self, PyObject* args){
    PyObject* py_output_list;
    uint64_t py_n;

    if ( ! PyArg_ParseTuple(args, "OK", &py_output_list, &py_n)) {
        return NULL;
    }
    output_list_t output_list = (output_list_t)get_ptr(py_output_list);
    output_t res = chain_output_list_nth(output_list, py_n);
    return to_py_obj(res);
}

#ifdef __cplusplus
} //extern "C"
#endif  
