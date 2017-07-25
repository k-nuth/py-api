#include "chain.h"

// -------------------------------------------------------------------
// fetch_block
// -------------------------------------------------------------------

void chain_fetch_block_handler(chain_t chain, void* ctx, int error , block_t block, size_t h) {
    PyObject* py_callback = ctx;

#if PY_MAJOR_VERSION >= 3
    PyObject* py_block = PyCapsule_New(block, NULL, NULL);
#else 
    PyObject* py_block = PyCObject_FromVoidPtr(block, NULL);
#endif
    //PyCapsule_GetPointer(py_header, NULL);

    PyObject* arglist = Py_BuildValue("(iOi)", error, py_block, h);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}


PyObject * bitprim_native_chain_fetch_block_by_height(PyObject* self, PyObject* args){
    PyObject* py_exec;
    Py_ssize_t py_height;
    PyObject* py_callback;
    if ( ! PyArg_ParseTuple(args, "OnO", &py_exec, &py_height, &py_callback)) {
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


PyObject * bitprim_native_chain_fetch_block_by_hash(PyObject* self, PyObject* args){
    PyObject* py_exec;
    PyObject* py_hash;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OOO", &py_exec, &py_hash, &py_callback)) {
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    char* s = PyString_AsString(py_hash);
    uint8_t * hash = (uint8_t*) malloc (sizeof(uint8_t[32]));
    hex2bin(s,&hash[31]);

    executor_t exec = cast_executor(py_exec);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_block_by_hash(exec, py_callback, hash, chain_fetch_block_handler);

    Py_RETURN_NONE;
}

// -------------------------------------------------------------------
// fetch_merkle_block
// -------------------------------------------------------------------

void chain_fetch_merkle_block_handler(chain_t chain, void* ctx, int error , merkle_block_t merkle, size_t h) {
    PyObject* py_callback = ctx;

#if PY_MAJOR_VERSION >= 3
    PyObject* py_merkle = PyCapsule_New(merkle, NULL, NULL);
#else 
    PyObject* py_merkle = PyCObject_FromVoidPtr(merkle, NULL);
#endif
    //PyCapsule_GetPointer(py_header, NULL);

    PyObject* arglist = Py_BuildValue("(iOi)", error, py_merkle, h);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}


PyObject * bitprim_native_chain_fetch_merkle_block_by_height(PyObject* self, PyObject* args){
    PyObject* py_exec;
    Py_ssize_t py_height;
    PyObject* py_callback;
    if ( ! PyArg_ParseTuple(args, "OnO", &py_exec, &py_height, &py_callback)) {
        //printf("bitprim_native_chain_fetch_block_header_by_height - 2\n");
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



PyObject * bitprim_native_chain_fetch_merkle_block_by_hash(PyObject* self, PyObject* args){
    PyObject* py_exec;
    PyObject* py_hash;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OOO", &py_exec, &py_hash, &py_callback)) {
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    char* s = PyString_AsString(py_hash);
    uint8_t * hash = (uint8_t*) malloc (sizeof(uint8_t[32]));
    hex2bin(s,&hash[31]);

    executor_t exec = cast_executor(py_exec);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_merkle_block_by_hash(exec, py_callback, hash, chain_fetch_merkle_block_handler);

    Py_RETURN_NONE;
}


// -------------------------------------------------------------------
// fetch block header
// -------------------------------------------------------------------

void chain_fetch_block_header_handler(chain_t chain, void* ctx, int error , header_t header, size_t h) {
    PyObject* py_callback = ctx;

  
#if PY_MAJOR_VERSION >= 3
    PyObject* py_header = PyCapsule_New(header, NULL, NULL);
#else 
    PyObject* py_header = PyCObject_FromVoidPtr(header, NULL);
#endif

    //PyCapsule_GetPointer(py_header, NULL);

    PyObject* arglist = Py_BuildValue("(iOi)", error, py_header, h);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}


PyObject * bitprim_native_chain_fetch_block_header_by_height(PyObject* self, PyObject* args){
    PyObject* py_exec;
    Py_ssize_t py_height;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OnO", &py_exec, &py_height, &py_callback)) {
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


PyObject * bitprim_native_chain_fetch_block_header_by_hash(PyObject* self, PyObject* args){
    PyObject* py_exec;
    PyObject* py_hash;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OOO", &py_exec, &py_hash, &py_callback)) {
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    char* s = PyString_AsString(py_hash);
    uint8_t * hash = (uint8_t*) malloc (sizeof(uint8_t[32]));
    hex2bin(s,&hash[31]);

    executor_t exec = cast_executor(py_exec);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_block_header_by_hash(exec, py_callback, hash, chain_fetch_block_header_handler);

    Py_RETURN_NONE;
}


// ---------------------------------------------------------
// chain_fetch_last_height
// ---------------------------------------------------------

void chain_fetch_last_height_handler(chain_t chain, void* ctx, int error, size_t h) {
    PyObject* py_callback = ctx;

    PyObject* arglist = Py_BuildValue("(ii)", error, h);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}

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
// chain_fetch_history
// ---------------------------------------------------------

void chain_fetch_history_handler(chain_t chain, void* ctx, int error, history_compact_list_t history_list) {

    PyObject* py_callback = ctx;

#if PY_MAJOR_VERSION >= 3
    PyObject* py_history_list = PyCapsule_New(history_list, NULL, NULL);
#else /* PY_MAJOR_VERSION >= 3 */
    PyObject* py_history_list = PyCObject_FromVoidPtr(history_list, NULL);
#endif /* PY_MAJOR_VERSION >= 3 */


    PyCapsule_GetPointer(py_history_list, NULL);
    PyCapsule_IsValid(py_history_list, NULL);

    PyObject* arglist = Py_BuildValue("(iO)", error, py_history_list);

    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);
    Py_XDECREF(py_callback);  // Dispose of the call
}

PyObject* bitprim_native_chain_fetch_history(PyObject* self, PyObject* args) {
    PyObject* py_exec;
    char* address_str;
    Py_ssize_t py_limit;
    Py_ssize_t py_from_height;
    PyObject* py_callback;

    // printf("bitprim_native_chain_fetch_history - 1\n");

    if ( ! PyArg_ParseTuple(args, "OsnnO:set_callback", &py_exec, &address_str, &py_limit, &py_from_height, &py_callback)) {
        // printf("bitprim_native_chain_fetch_history - 2\n");
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        // printf("bitprim_native_chain_fetch_history - 3\n");
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    // printf("bitprim_native_chain_fetch_history - 4\n");


    executor_t exec = cast_executor(py_exec);

    Py_XINCREF(py_callback);         /* Add a reference to new callback */

    payment_address_t pa = payment_address_construct_from_string(address_str);
    chain_fetch_history(exec, py_callback, pa, py_limit, py_from_height, chain_fetch_history_handler);
    // payment_address_destruct(pa);

    Py_RETURN_NONE;
}

// ---------------------------------------------------------
// chain_fetch_block_height
// ---------------------------------------------------------

void chain_block_height_fetch_handler(chain_t chain, void* ctx, int error, size_t h) {

    PyObject* py_callback = ctx;

    PyObject* arglist = Py_BuildValue("(in)", error, h);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}


PyObject* bitprim_native_chain_fetch_block_height(PyObject* self, PyObject* args) {
    PyObject* py_exec;
    PyObject* py_hash;
    PyObject* py_callback;
    
    if ( ! PyArg_ParseTuple(args, "OOO:set_callback", &py_exec, &py_hash, &py_callback)) {
        // printf("bitprim_native_fetch_block_height - 2\n");
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    
    executor_t exec = cast_executor(py_exec);
    char* s = PyString_AsString(py_hash);
    uint8_t * hash = (uint8_t*) malloc (sizeof(uint8_t[32]));
    hex2bin(s,&hash[31]);

    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_block_height(exec, py_callback, hash, chain_block_height_fetch_handler);
    Py_RETURN_NONE;
}


// ---------------------------------------------------------
// stealth_history
// ---------------------------------------------------------

/////STEALTH FETCH HANDLER
void chain_stealth_fetch_handler(chain_t chain, void* ctx, int error, stealth_compact_list_t stealth_list) {
    PyObject* py_callback = ctx;

#if PY_MAJOR_VERSION >= 3
    PyObject* py_stealth_list = PyCapsule_New(stealth_list, NULL, NULL);
#else /* PY_MAJOR_VERSION >= 3 */
    PyObject* py_stealth_list = PyCObject_FromVoidPtr(stealth_list, NULL);
#endif /* PY_MAJOR_VERSION >= 3 */

    void* ptr_void = PyCapsule_GetPointer(py_stealth_list, NULL);
    int is_valid = PyCapsule_IsValid(py_stealth_list, NULL);


    PyObject* arglist = Py_BuildValue("(iO)", error, py_stealth_list);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}


//void fetch_stealth(executor_t exec, binary_t filter, size_t from_height, stealth_fetch_handler_t handler)
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


