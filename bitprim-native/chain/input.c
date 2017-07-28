#include "input.h"

PyObject* bitprim_native_chain_input_is_valid(PyObject* self, PyObject* args){
    PyObject* py_input;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_input)) {
        return NULL;
    }

    input_t input = (input_t)get_ptr(py_input);
    int res = chain_input_is_valid(input);
    return Py_BuildValue("i", res);
}

PyObject* bitprim_native_chain_input_serialized_size(PyObject* self, PyObject* args){
    PyObject* py_input;
    int py_wire;
    
    if ( ! PyArg_ParseTuple(args, "Oi", &py_input, &py_wire)) {
        return NULL;
    }

    input_t input = (input_t)get_ptr(py_input);
    uint64_t res = chain_input_serialized_size(input, py_wire);
    return Py_BuildValue("K", res);
}


PyObject* bitprim_native_chain_input_value(PyObject* self, PyObject* args){
    PyObject* py_input;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_input)) {
        return NULL;
    }

    input_t input = (input_t)get_ptr(py_input);
    uint64_t res = chain_input_value(input);
    return Py_BuildValue("K", res);
}


PyObject* bitprim_native_chain_input_signature_operations(PyObject* self, PyObject* args){
    PyObject* py_input;
    int py_bip16_active;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_input, &py_bip16_active)) {
        return NULL;
    }

    input_t input = (input_t)get_ptr(py_input);
    uint64_t res = chain_input_signature_operations(input, py_bip16_active);
    return Py_BuildValue("K", res);

}
/*
PyObject* bitprim_native_chain_input_get_hash(PyObject* self, PyObject* args){
    PyObject* py_input;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_input)) {
        return NULL;
    }

    input_t input = (input_t)get_ptr(py_input);
    hash_t res = chain_input_get_hash(input);
    return PyByteArray_FromStringAndSize(res.hash, 32);

}
*/

/*
PyObject* bitprim_native_chain_input_get_index(PyObject* self, PyObject* args){
    PyObject* py_input;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_input)) {
        return NULL;
    }

    input_t input = (input_t)get_ptr(py_input);
    uint32_t res = chain_input_get_index(input);
    return Py_BuildValue("L", res);

}
*/
