#include "chain_block.h"

PyObject * bitprim_native_chain_block_get_header(PyObject* self, PyObject* args){
    PyObject* py_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    header_t header = block_header(block);

  
#if PY_MAJOR_VERSION >= 3
    return PyCapsule_New(header, NULL, NULL);
#else /* PY_MAJOR_VERSION >= 3 */
    return PyCObject_FromVoidPtr(header, NULL);
#endif /* PY_MAJOR_VERSION >= 3 */

}

PyObject * bitprim_native_chain_block_transaction_count(PyObject* self, PyObject* args){
    PyObject* py_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    uint64_t res = block_transaction_count(block);

    return Py_BuildValue("n", res);   
}

PyObject * bitprim_native_chain_block_serialized_size(PyObject* self, PyObject* args){
    PyObject* py_block;
    uint32_t py_version;

    if ( ! PyArg_ParseTuple(args, "OI", &py_block, &py_version)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    uint64_t res = block_serialized_size(block, py_version);

    return Py_BuildValue("n", res);   
}


PyObject * bitprim_native_chain_block_subsidy(PyObject* self, PyObject* args){
    PyObject* py_block;


    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    uint64_t res = block_subsidy(block);

    return Py_BuildValue("n", res);   
}


PyObject * bitprim_native_chain_block_fees(PyObject* self, PyObject* args){
    PyObject* py_block;


    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    uint64_t res = block_fees(block);

    return Py_BuildValue("n", res);   
}

PyObject * bitprim_native_chain_block_claim(PyObject* self, PyObject* args){
    PyObject* py_block;


    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    uint64_t res = block_claim(block);

    return Py_BuildValue("n", res);   
}

PyObject * bitprim_native_chain_block_reward(PyObject* self, PyObject* args){
    PyObject* py_block;
    uint32_t py_height;

    if ( ! PyArg_ParseTuple(args, "OI", &py_block, &py_height)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    uint64_t res = block_reward(block, py_height);

    return Py_BuildValue("n", res);   
}

PyObject * bitprim_native_chain_block_generate_merkle_root(PyObject* self, PyObject* args){
    PyObject* py_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    hash_t res = block_generate_merkle_root(block);

#if PY_MAJOR_VERSION >= 3
    return PyCapsule_New(res, NULL, NULL);
#else /* PY_MAJOR_VERSION >= 3 */
    return PyCObject_FromVoidPtr(res, NULL);
#endif /* PY_MAJOR_VERSION >= 3 */

}

PyObject * bitprim_native_chain_block_hash(PyObject* self, PyObject* args){
    PyObject* py_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    hash_t res = block_hash(block);

#if PY_MAJOR_VERSION >= 3
    return PyCapsule_New(res, NULL, NULL);
#else /* PY_MAJOR_VERSION >= 3 */
    return PyCObject_FromVoidPtr(res, NULL);
#endif /* PY_MAJOR_VERSION >= 3 */

}

