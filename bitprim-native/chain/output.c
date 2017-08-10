#include "output.h"

#ifdef __cplusplus
extern "C" {  
#endif  

PyObject* bitprim_native_chain_output_is_valid(PyObject* self, PyObject* args){
    PyObject* py_output;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_output)) {
        return NULL;
    }

    output_t output = (output_t)get_ptr(py_output);
    int res = chain_output_is_valid(output);
    return Py_BuildValue("i", res);
}

PyObject* bitprim_native_chain_output_serialized_size(PyObject* self, PyObject* args){
    PyObject* py_output;
    int py_wire;
    
    if ( ! PyArg_ParseTuple(args, "Oi", &py_output, &py_wire)) {
        return NULL;
    }

    output_t output = (output_t)get_ptr(py_output);
    uint64_t res = chain_output_serialized_size(output, py_wire);
    return Py_BuildValue("K", res);
}


PyObject* bitprim_native_chain_output_value(PyObject* self, PyObject* args){
    PyObject* py_output;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_output)) {
        return NULL;
    }

    output_t output = (output_t)get_ptr(py_output);
    uint64_t res = chain_output_value(output);
    return Py_BuildValue("K", res);
}


PyObject* bitprim_native_chain_output_signature_operations(PyObject* self, PyObject* args){
    PyObject* py_output;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_output)) {
        return NULL;
    }

    output_t output = (output_t)get_ptr(py_output);
    uint64_t res = chain_output_signature_operations(output);
    return Py_BuildValue("K", res);

}

PyObject* bitprim_native_chain_output_destruct(PyObject* self, PyObject* args){
    PyObject* py_output;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_output)) {
        return NULL;
    }

    output_t output = (output_t)get_ptr(py_output);
    chain_output_destruct(output);
    Py_RETURN_NONE;
}

PyObject* bitprim_native_chain_output_script(PyObject* self, PyObject* args){
    PyObject* py_output;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_output)) {
        return NULL;
    }

    output_t output = (output_t)get_ptr(py_output);
    script_t script = chain_output_script(output);
    return to_py_obj(script);
}

/*
PyObject* bitprim_native_chain_output_get_hash(PyObject* self, PyObject* args){
    PyObject* py_output;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_output)) {
        return NULL;
    }

    output_t output = (output_t)get_ptr(py_output);
    hash_t res = chain_output_get_hash(output);
    return PyByteArray_FromStringAndSize(res.hash, 32);

}
*/

/*
PyObject* bitprim_native_chain_output_get_index(PyObject* self, PyObject* args){
    PyObject* py_output;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_output)) {
        return NULL;
    }

    output_t output = (output_t)get_ptr(py_output);
    uint32_t res = chain_output_get_index(output);
    return Py_BuildValue("L", res);

}
*/


#ifdef __cplusplus
} //extern "C"
#endif  
