#include "output_point.h"

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
    //PyObject* py_exec;
    char* py_hash;
    size_t py_size;
    uint32_t py_index;
    //printf("bitprim_native_chain_output_point_construct_from_hash_index 1\n");
#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "y#I", &py_hash, &py_size, &py_index)) {
        return NULL;
    }
#else
    if ( ! PyArg_ParseTuple(args, "s#I", &py_hash, &py_size, &py_index)) {
        return NULL;
    }
#endif

    printf("bitprim_native_chain_output_point_construct_from_hash_index 2   %s\n", py_hash);
    hash_t hash;
    memcpy(hash.hash, py_hash, 32);
    //memcpy(hash.hash, "0e3e2357e806b6cdb1f70b54c3a3a17b6714ee1f0e68bebb44a74b1efd512098", 32);
    //printf("bitprim_native_chain_output_point_construct_from_hash_index 3\n");
    output_point_t res = output_point_construct_from_hash_index(hash, py_index);
    printf("bitprim_native_chain_output_point_construct_from_hash_index 4 %p\n", res);
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
