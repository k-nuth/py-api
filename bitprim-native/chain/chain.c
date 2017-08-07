/**
 * Copyright (c) 2017 Bitprim developers (see AUTHORS)
 *
 * This file is part of Bitprim.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include "chain.h"

// ---------------------------------------------------------
// chain_fetch_last_height
// ---------------------------------------------------------

void chain_fetch_last_height_handler(chain_t chain, void* ctx, int error, uint64_t /*size_t*/ h) {
    PyObject* py_callback = ctx;

    PyObject* arglist = Py_BuildValue("(iK)", error, h);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}

static
PyObject* bitprim_native_chain_fetch_last_height(PyObject* self, PyObject* args) {
    PyObject* py_exec;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OO:set_callback", &py_exec, &py_callback)) {
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    executor_t exec = cast_executor(py_exec);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_last_height(exec, py_callback, chain_fetch_last_height_handler);

    Py_RETURN_NONE;
}



// ---------------------------------------------------------
// chain_fetch_block_height
// ---------------------------------------------------------

void chain_block_height_fetch_handler(chain_t chain, void* ctx, int error, uint64_t /*size_t*/ h) {

    PyObject* py_callback = ctx;

    PyObject* arglist = Py_BuildValue("(iK)", error, h);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}


static
PyObject* bitprim_native_chain_fetch_block_height(PyObject* self, PyObject* args) {
    PyObject* py_exec;
    char* py_hash;
    size_t py_hash_size;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy#O", &py_exec, &py_hash, &py_hash_size, &py_callback)) {
        return NULL;
    }
#else
    if ( ! PyArg_ParseTuple(args, "Os#O", &py_exec, &py_hash, &py_hash_size, &py_callback)) {
        return NULL;
    }
#endif

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    executor_t exec = cast_executor(py_exec);
    
    hash_t hash;
    memcpy(hash.hash, py_hash, 32);

    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_block_height(exec, py_callback, hash, chain_block_height_fetch_handler);
    Py_RETURN_NONE;
}

// -------------------------------------------------------------------
// fetch block header
// -------------------------------------------------------------------

void chain_fetch_block_header_handler(chain_t chain, void* ctx, int error , header_t header, uint64_t /*size_t*/ h) {
    PyObject* py_callback = ctx;

    PyObject* py_header = to_py_obj(header);


    PyObject* arglist = Py_BuildValue("(iOK)", error, py_header, h);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}

static
PyObject * bitprim_native_chain_fetch_block_header_by_height(PyObject* self, PyObject* args){
    PyObject* py_exec;
    uint64_t py_height;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OKO", &py_exec, &py_height, &py_callback)) {
        //printf("bitprim_native_chain_fetch_block_header_by_height - 2\n");
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    executor_t exec = cast_executor(py_exec);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_block_header_by_height(exec, py_callback, py_height, chain_fetch_block_header_handler);

    Py_RETURN_NONE;
}

static
PyObject * bitprim_native_chain_fetch_block_header_by_hash(PyObject* self, PyObject* args){
    PyObject* py_exec;
    char* py_hash;
    size_t py_hash_size;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy#O", &py_exec, &py_hash, &py_hash_size, &py_callback)) {
        return NULL;
    }
#else
    if ( ! PyArg_ParseTuple(args, "Os#O", &py_exec, &py_hash, &py_hash_size, &py_callback)) {
        return NULL;
    }
#endif

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    hash_t hash;
    memcpy(hash.hash, py_hash, 32);

    executor_t exec = cast_executor(py_exec);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_block_header_by_hash(exec, py_callback, hash, chain_fetch_block_header_handler);
    Py_RETURN_NONE;
}


// -------------------------------------------------------------------
// fetch_block
// -------------------------------------------------------------------

void chain_fetch_block_handler(chain_t chain, void* ctx, int error , block_t block, uint64_t /*size_t*/ h) {
    PyObject* py_callback = ctx;

    PyObject* py_block = to_py_obj(block);

    PyObject* arglist = Py_BuildValue("(iOK)", error, py_block, h);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}

static
PyObject * bitprim_native_chain_fetch_block_by_height(PyObject* self, PyObject* args){
    PyObject* py_exec;
    uint64_t py_height;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OKO", &py_exec, &py_height, &py_callback)) {
        //printf("bitprim_native_chain_fetch_block_header_by_height - 2\n");
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    executor_t exec = cast_executor(py_exec);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_block_by_height(exec, py_callback, py_height, chain_fetch_block_handler);
    Py_RETURN_NONE;
}


static
PyObject * bitprim_native_chain_fetch_block_by_hash(PyObject* self, PyObject* args){
    PyObject* py_exec;
    char* py_hash;
    size_t py_hash_size;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy#O", &py_exec, &py_hash, &py_hash_size, &py_callback)) {
        return NULL;
    }
#else
    if ( ! PyArg_ParseTuple(args, "Os#O", &py_exec, &py_hash, &py_hash_size, &py_callback)) {
        return NULL;
    }
#endif

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    hash_t hash;
    memcpy(hash.hash, py_hash, 32);

    executor_t exec = cast_executor(py_exec);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_block_by_hash(exec, py_callback, hash, chain_fetch_block_handler);
    Py_RETURN_NONE;
}


// -------------------------------------------------------------------
// fetch_merkle_block
// -------------------------------------------------------------------

void chain_fetch_merkle_block_handler(chain_t chain, void* ctx, int error, merkle_block_t merkle, uint64_t /*size_t*/ h) {
    PyObject* py_callback = ctx;

    PyObject* py_merkle = to_py_obj(merkle);

    PyObject* arglist = Py_BuildValue("(iOK)", error, py_merkle, h);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}

static
PyObject * bitprim_native_chain_fetch_merkle_block_by_height(PyObject* self, PyObject* args){
    PyObject* py_exec;
    uint64_t py_height;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OKO", &py_exec, &py_height, &py_callback)) {
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    executor_t exec = cast_executor(py_exec);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_merkle_block_by_height(exec, py_callback, py_height, chain_fetch_merkle_block_handler);
    Py_RETURN_NONE;
}


static
PyObject * bitprim_native_chain_fetch_merkle_block_by_hash(PyObject* self, PyObject* args){
    PyObject* py_exec;
    char* py_hash;
    size_t py_hash_size;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy#O", &py_exec, &py_hash, &py_hash_size, &py_callback)) {
        return NULL;
    }
#else
    if ( ! PyArg_ParseTuple(args, "Os#O", &py_exec, &py_hash, &py_hash_size, &py_callback)) {
        return NULL;
    }
#endif

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    hash_t hash;
    memcpy(hash.hash, py_hash, 32);

    executor_t exec = cast_executor(py_exec);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_merkle_block_by_hash(exec, py_callback, hash, chain_fetch_merkle_block_handler);

    Py_RETURN_NONE;
}




// ---------------------------------------------------------
// chain_fetch_history
// ---------------------------------------------------------

void chain_fetch_history_handler(chain_t chain, void* ctx, int error, history_compact_list_t history_list) {

    PyObject* py_callback = ctx;

    PyObject* py_history_list = to_py_obj(history_list);

    // PyCapsule_GetPointer(py_history_list, NULL); //TODO: ????
    PyCapsule_IsValid(py_history_list, NULL);

    PyObject* arglist = Py_BuildValue("(iO)", error, py_history_list);

    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);
    Py_XDECREF(py_callback);  // Dispose of the call
}

static
PyObject* bitprim_native_chain_fetch_history(PyObject* self, PyObject* args) {
    PyObject* py_exec;
    char* address_str;
    uint64_t py_limit;
    uint64_t py_from_height;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OsKKO:set_callback", &py_exec, &address_str, &py_limit, &py_from_height, &py_callback)) {
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    executor_t exec = cast_executor(py_exec);

    Py_XINCREF(py_callback);         /* Add a reference to new callback */

    payment_address_t pa = chain_payment_address_construct_from_string(address_str);
    chain_fetch_history(exec, py_callback, pa, py_limit, py_from_height, chain_fetch_history_handler);
    // payment_address_destruct(pa); //TODO!

    Py_RETURN_NONE;
}



// ---------------------------------------------------------
// stealth_history
// ---------------------------------------------------------

void chain_stealth_fetch_handler(chain_t chain, void* ctx, int error, stealth_compact_list_t stealth_list) {
    PyObject* py_callback = ctx;

    PyObject* py_stealth_list = to_py_obj(stealth_list);
    void* ptr_void = PyCapsule_GetPointer(py_stealth_list, NULL);
    int is_valid = PyCapsule_IsValid(py_stealth_list, NULL);

    PyObject* arglist = Py_BuildValue("(iO)", error, py_stealth_list);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}


static
PyObject* bitprim_native_chain_fetch_stealth(PyObject* self, PyObject* args) {
    PyObject* py_exec;
    PyObject* py_filter;
    Py_ssize_t py_from_height;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OOnO:set_callback", &py_exec, &py_filter, &py_from_height, &py_callback)) {
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    executor_t exec = (executor_t)PyCapsule_GetPointer(py_exec, NULL);

    Py_XINCREF(py_callback);         /* Add a reference to new callback */

    binary_t binary_filter = (binary_t)PyCapsule_GetPointer(py_filter, NULL);
    chain_fetch_stealth(exec, py_callback, binary_filter, py_from_height, chain_stealth_fetch_handler);

    Py_RETURN_NONE;
}


