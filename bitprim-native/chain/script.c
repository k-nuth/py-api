#include "script.h"

#ifdef __cplusplus
extern "C" {  
#endif  

PyObject* bitprim_native_chain_script_destruct(PyObject* self, PyObject* args){
    PyObject* py_script;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_script)) {
        return NULL;
    }

    script_t script = (script_t)get_ptr(py_script);
    chain_script_destruct(script);
    Py_RETURN_NONE;
}

PyObject* bitprim_native_chain_script_is_valid(PyObject* self, PyObject* args){
    PyObject* py_script;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_script)) {
        return NULL;
    }

    script_t script = (script_t)get_ptr(py_script);
    int res = chain_script_is_valid(script);
    return Py_BuildValue("i", res);
}


PyObject* bitprim_native_chain_script_is_valid_operations(PyObject* self, PyObject* args){
    PyObject* py_script;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_script)) {
        return NULL;
    }

    script_t script = (script_t)get_ptr(py_script);
    int res = chain_script_is_valid_operations(script);
    return Py_BuildValue("i", res);
}


PyObject* bitprim_native_chain_script_satoshi_content_size(PyObject* self, PyObject* args){
    PyObject* py_script;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_script)) {
        return NULL;
    }

    script_t script = (script_t)get_ptr(py_script);
    uint64_t res = chain_script_satoshi_content_size(script);
    return Py_BuildValue("K", res);
}

PyObject* bitprim_native_chain_script_serialized_size(PyObject* self, PyObject* args){
    PyObject* py_script;
    int py_prefix;

    if ( ! PyArg_ParseTuple(args, "Oi", &py_script, &py_prefix)) {
        return NULL;
    }

    script_t script = (script_t)get_ptr(py_script);
    uint64_t res = chain_script_serialized_size(script, py_prefix);
    return Py_BuildValue("K", res);
}


PyObject* bitprim_native_chain_script_to_string(PyObject* self, PyObject* args){
    PyObject* py_script;
    uint32_t py_active_forks;

    if ( ! PyArg_ParseTuple(args, "OI", &py_script, &py_active_forks)) {
        return NULL;
    }

    script_t script = (script_t)get_ptr(py_script);
    char const* res = chain_script_to_string(script, py_active_forks);
    return Py_BuildValue("s", res);
}

PyObject* bitprim_native_chain_script_sigops(PyObject* self, PyObject* args){
    PyObject* py_script;
    int py_embedded;

    if ( ! PyArg_ParseTuple(args, "Oi", &py_script, &py_embedded)) {
        return NULL;
    }

    script_t script = (script_t)get_ptr(py_script);
    uint64_t res = chain_script_sigops(script, py_embedded);
    return Py_BuildValue("K", res);
}

PyObject* bitprim_native_chain_script_embedded_sigops(PyObject* self, PyObject* args){
    PyObject* py_script;
    PyObject* py_prevout_script;

    if ( ! PyArg_ParseTuple(args, "Oi", &py_script, &py_prevout_script)) {
        return NULL;
    }

    script_t script = (script_t)get_ptr(py_script);
    script_t prevout_script = (script_t)get_ptr(py_prevout_script);
    uint64_t res = chain_script_embedded_sigops(script, prevout_script);
    return Py_BuildValue("K", res);
}


#ifdef __cplusplus
} // extern "C"
#endif  
