#include "output_point.h"

#ifdef __cplusplus
extern "C" {  
#endif  

PyObject * bitprim_native_chain_output_point_get_hash(PyObject* self, PyObject* args){
    PyObject* py_output_point;

    if ( ! PyArg_ParseTuple(args, "O", &py_output_point)) {
        return NULL;
    }

    output_point_t p = (output_point_t)get_ptr(py_output_point);
    hash_t res = output_point_get_hash(p);
#if PY_MAJOR_VERSION >= 3
    return Py_BuildValue("y#", res.hash, 32);    //TODO: warning, hardcoded hash size!
#else
    return Py_BuildValue("s#", res.hash, 32);    //TODO: warning, hardcoded hash size!
#endif

}

PyObject * bitprim_native_chain_output_point_get_index(PyObject* self, PyObject* args){
    PyObject* py_output_point;

    if ( ! PyArg_ParseTuple(args, "O", &py_output_point)) {
        return NULL;
    }

    output_point_t p = (output_point_t)get_ptr(py_output_point);
    uint32_t res = output_point_get_index(p);
    return Py_BuildValue("K", res);
}



PyObject * bitprim_native_chain_output_point_construct(PyObject* self, PyObject* args){
    return to_py_obj(output_point_construct());
}

PyObject * bitprim_native_chain_output_point_construct_from_hash_index(PyObject* self, PyObject* args){
    char* py_hash;
    size_t py_size;
    uint32_t py_index;
#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "y#I", &py_hash, &py_size, &py_index)) {
        return NULL;
    }
#else
    if ( ! PyArg_ParseTuple(args, "s#I", &py_hash, &py_size, &py_index)) {
        return NULL;
    }
#endif

    hash_t hash;
    memcpy(hash.hash, py_hash, 32);
    output_point_t res = output_point_construct_from_hash_index(hash, py_index);
    return to_py_obj(res);
}


PyObject * bitprim_native_chain_output_point_destruct(PyObject* self, PyObject* args){
    PyObject* py_output_point;  
    if ( ! PyArg_ParseTuple(args, "O", &py_output_point)) {
        return NULL;
    }
    output_point_t output_point = (output_point_t)get_ptr(py_output_point);
    output_point_destruct(output_point);
    Py_RETURN_NONE; 
}


/*


PyObject* bitprim_native_point_is_valid(PyObject* self, PyObject* args) {
    PyObject* py_point;

    if ( ! PyArg_ParseTuple(args, "O", &py_point)) {
        // printf("bitprim_native_point_is_valid - 2\n");
        return NULL;
    }

    // point_t p = (point_t)PyCObject_AsVoidPtr(py_point);
    point_t p = (point_t)PyCapsule_GetPointer(py_point, NULL);
    int res = point_is_valid(p);

    if (res == 0) {
        Py_RETURN_FALSE;
    }

    Py_RETURN_TRUE;
}


PyObject* bitprim_native_point_get_checksum(PyObject* self, PyObject* args) {
    PyObject* py_point;

    if ( ! PyArg_ParseTuple(args, "O", &py_point)) {
        // printf("bitprim_native_point_get_checksum - 2\n");
        return NULL;
    }

    // point_t p = (point_t)PyCObject_AsVoidPtr(py_point);
    point_t p = (point_t)PyCapsule_GetPointer(py_point, NULL);
    uint64_t res = point_get_checksum(p);

    return Py_BuildValue("K", res);
}


*/


#ifdef __cplusplus
} //extern "C"
#endif  
