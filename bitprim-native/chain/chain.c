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
    PyObject* py_chain;
    Py_ssize_t py_height;
    PyObject* py_callback;
    if ( ! PyArg_ParseTuple(args, "OnO", &py_chain, &py_height, &py_callback)) {
        //printf("bitprim_native_chain_fetch_block_header_by_height - 2\n");
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_block_by_height(chain, py_callback, py_height, chain_fetch_block_handler);
    Py_RETURN_NONE;
}


PyObject * bitprim_native_chain_fetch_block_by_hash(PyObject* self, PyObject* args){
    PyObject* py_chain;
    // PyObject* py_hash;
    char* py_hash;
    size_t py_size;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy#O", &py_chain, &py_hash, &py_size, &py_callback)) {
        return NULL;
    }
#else
    if ( ! PyArg_ParseTuple(args, "Os#O", &py_chain, &py_hash, &py_size, &py_callback)) {
        return NULL;
    }
#endif


    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    // char* s = PyString_AsString(py_hash);
    // uint8_t * hash = (uint8_t*) malloc (sizeof(uint8_t[32]));
    // hex2bin(s,&hash[31]);
    hash_t hash;
    // void* memcpy( void* dest, const void* src, std::size_t count );
    memcpy(hash.hash, py_hash, 32);

    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_block_by_hash(chain, py_callback, hash, chain_fetch_block_handler);
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
    PyObject* py_chain;
    Py_ssize_t py_height;
    PyObject* py_callback;
    if ( ! PyArg_ParseTuple(args, "OnO", &py_chain, &py_height, &py_callback)) {
        //printf("bitprim_native_chain_fetch_block_header_by_height - 2\n");
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_merkle_block_by_height(chain, py_callback, py_height, chain_fetch_merkle_block_handler);
    Py_RETURN_NONE;
}



PyObject * bitprim_native_chain_fetch_merkle_block_by_hash(PyObject* self, PyObject* args){
    PyObject* py_chain;
    // PyObject* py_hash;
    char* py_hash;
    size_t py_size;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy#O", &py_chain, &py_hash, &py_size, &py_callback)) {
        return NULL;
    }
#else
    if ( ! PyArg_ParseTuple(args, "Os#O", &py_chain, &py_hash, &py_size, &py_callback)) {
        return NULL;
    }
#endif


    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    // char* s = PyString_AsString(py_hash);
    // uint8_t * hash = (uint8_t*) malloc (sizeof(uint8_t[32]));
    // hex2bin(s,&hash[31]);


    hash_t hash;
    // void* memcpy( void* dest, const void* src, std::size_t count );
    memcpy(hash.hash, py_hash, 32);

    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_merkle_block_by_hash(chain, py_callback, hash, chain_fetch_merkle_block_handler);

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
    PyObject* py_chain;
    Py_ssize_t py_height;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OnO", &py_chain, &py_height, &py_callback)) {
        //printf("bitprim_native_chain_fetch_block_header_by_height - 2\n");
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_block_header_by_height(chain, py_callback, py_height, chain_fetch_block_header_handler);

    Py_RETURN_NONE;
}


PyObject * bitprim_native_chain_fetch_block_header_by_hash(PyObject* self, PyObject* args){
    PyObject* py_chain;
    // PyObject* py_hash;
    //Py_buffer py_hash;
    char* py_hash;
    size_t py_size;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy#O", &py_chain, &py_hash, &py_size, &py_callback)) {
        return NULL;
    }
#else
    if ( ! PyArg_ParseTuple(args, "Os#O", &py_chain, &py_hash, &py_size, &py_callback)) {
        return NULL;
    }
#endif

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }
    // char* s = PyString_AsString(py_hash);
    // uint8_t * hash = (uint8_t*) malloc (sizeof(uint8_t[32]));
    // hex2bin(s,&hash[31]);

    hash_t hash;
    // void* memcpy( void* dest, const void* src, std::size_t count );
    memcpy(hash.hash, py_hash, 32);

    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_block_header_by_hash(chain, py_callback, hash, chain_fetch_block_header_handler);
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
    PyObject* py_chain;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OO:set_callback", &py_chain, &py_callback)) {
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_last_height(chain, py_callback, chain_fetch_last_height_handler);

    Py_RETURN_NONE;
}


// ---------------------------------------------------------
// chain_fetch_history
// ---------------------------------------------------------

void chain_fetch_history_handler(chain_t chain, void* ctx, int error, history_compact_list_t history_list) {

    PyObject* py_callback = ctx;

// #if PY_MAJOR_VERSION >= 3
//     PyObject* py_history_list = PyCapsule_New(history_list, NULL, NULL);
// #else /* PY_MAJOR_VERSION >= 3 */
//     PyObject* py_history_list = PyCObject_FromVoidPtr(history_list, NULL);
// #endif /* PY_MAJOR_VERSION >= 3 */

    PyObject* py_history_list = to_py_obj(history_list);

    PyCapsule_GetPointer(py_history_list, NULL);
    PyCapsule_IsValid(py_history_list, NULL);

    PyObject* arglist = Py_BuildValue("(iO)", error, py_history_list);

    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);
    Py_XDECREF(py_callback);  // Dispose of the call
}

PyObject* bitprim_native_chain_fetch_history(PyObject* self, PyObject* args) {
    PyObject* py_chain;
    char* address_str;
    Py_ssize_t py_limit;
    Py_ssize_t py_from_height;
    PyObject* py_callback;

    // printf("bitprim_native_chain_fetch_history - 1\n");

    if ( ! PyArg_ParseTuple(args, "OsnnO:set_callback", &py_chain, &address_str, &py_limit, &py_from_height, &py_callback)) {
        // printf("bitprim_native_chain_fetch_history - 2\n");
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        // printf("bitprim_native_chain_fetch_history - 3\n");
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    // printf("bitprim_native_chain_fetch_history - 4\n");


    chain_t chain = (chain_t)get_ptr(py_chain);

    Py_XINCREF(py_callback);         /* Add a reference to new callback */

    payment_address_t pa = payment_address_construct_from_string(address_str);
    chain_fetch_history(chain, py_callback, pa, py_limit, py_from_height, chain_fetch_history_handler);
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
    PyObject* py_chain;
    // PyObject* py_hash;
    char* py_hash;
    size_t py_size;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy#O", &py_chain, &py_hash, &py_size, &py_callback)) {
        return NULL;
    }
#else
    if ( ! PyArg_ParseTuple(args, "Os#O", &py_chain, &py_hash, &py_size, &py_callback)) {
        return NULL;
    }
#endif

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    chain_t chain = (chain_t)get_ptr(py_chain);
    
    // char* s = PyString_AsString(py_hash);
    // uint8_t * hash = (uint8_t*) malloc (sizeof(uint8_t[32]));
    // hex2bin(s, &hash[31]);

    hash_t hash;
    // void* memcpy( void* dest, const void* src, std::size_t count );
    memcpy(hash.hash, py_hash, 32);

    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_block_height(chain, py_callback, hash, chain_block_height_fetch_handler);
    Py_RETURN_NONE;
}


// ---------------------------------------------------------
// stealth_history
// ---------------------------------------------------------

/////STEALTH FETCH HANDLER
void chain_stealth_fetch_handler(chain_t chain, void* ctx, int error, stealth_compact_list_t stealth_list) {
    PyObject* py_callback = ctx;

    PyObject* py_stealth_list = to_py_obj(stealth_list);
    PyCapsule_GetPointer(py_stealth_list, NULL);
    PyCapsule_IsValid(py_stealth_list, NULL);

    PyObject* arglist = Py_BuildValue("(iO)", error, py_stealth_list);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}


PyObject* bitprim_native_chain_fetch_stealth(PyObject* self, PyObject* args) {
    PyObject* py_chain;
    PyObject* py_filter;
    Py_ssize_t py_from_height;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OOnO:set_callback", &py_chain, &py_filter, &py_from_height, &py_callback)) {
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    chain_t chain = (chain_t)get_ptr(py_chain);

    Py_XINCREF(py_callback);         /* Add a reference to new callback */

    binary_t binary_filter = (binary_t)PyCapsule_GetPointer(py_filter, NULL);
    chain_fetch_stealth(chain, py_callback, binary_filter, py_from_height, chain_stealth_fetch_handler);

    Py_RETURN_NONE;
}

void chain_fetch_transaction_handler(chain_t chain, void* ctx, int error, transaction_t transaction, uint64_t height, uint64_t index) {
    PyObject* py_callback = ctx;
    PyObject* py_transaction = to_py_obj(transaction);

    PyObject* arglist = Py_BuildValue("(iOnn)", error, py_transaction, height, index);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}

PyObject* bitprim_native_chain_fetch_transaction(PyObject* self, PyObject* args) {
    PyObject* py_chain;
    // PyObject* py_hash;
    char* py_hash;
    size_t py_size;
    int py_require_confirmed;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy#iO", &py_chain, &py_hash, &py_size, &py_require_confirmed,&py_callback)) {
        return NULL;
    }
#else
    if ( ! PyArg_ParseTuple(args, "Os#iO", &py_chain, &py_hash, &py_size, &py_require_confirmed,&py_callback)) {
        return NULL;
    }
#endif


    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }
    printf("bitprim_native_chain_fetch_transaction 2   %s\n", py_hash);
    hash_t hash;
    memcpy(hash.hash, py_hash, 32);

    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);
    chain_fetch_transaction(chain, py_callback, hash, py_require_confirmed, chain_fetch_transaction_handler);

    Py_RETURN_NONE;
}


void chain_fetch_output_handler(chain_t chain, void* ctx, int error, output_t output) {
    PyObject* py_callback = ctx;
    PyObject* py_output = to_py_obj(output);

    PyObject* arglist = Py_BuildValue("(iO)", error, py_output);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}


PyObject* bitprim_native_chain_fetch_output(PyObject* self, PyObject* args){
    PyObject* py_chain;
    // PyObject* py_hash;
    char* py_hash;
    size_t py_size;
    uint32_t py_index;
    int py_require_confirmed;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy#IiO", &py_chain, &py_hash, &py_size, &py_index, &py_require_confirmed, &py_callback)) {
        return NULL;
    }
#else
    if ( ! PyArg_ParseTuple(args, "Os#IiO", &py_chain, &py_hash, &py_size, &py_index, &py_require_confirmed, &py_callback)) {
        return NULL;
    }
#endif

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    hash_t hash;
    memcpy(hash.hash, py_hash, 32);

    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);
    chain_fetch_output(chain, py_callback, hash, py_index, py_require_confirmed, chain_fetch_output_handler);

    Py_RETURN_NONE;
}

void chain_fetch_transaction_position_handler(chain_t chain, void* ctx, int error, uint64_t position, uint64_t height) {
    PyObject* py_callback = ctx;
    PyObject* arglist = Py_BuildValue("(iKK)", error, position, height);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}


PyObject* bitprim_native_chain_fetch_transaction_position(PyObject* self, PyObject* args){
    PyObject* py_chain;
    // PyObject* py_hash;
    char* py_hash;
    size_t py_size;
    int py_require_confirmed;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy#iO", &py_chain, &py_hash, &py_size, &py_require_confirmed,&py_callback)) {
        return NULL;
    }
#else
    if ( ! PyArg_ParseTuple(args, "Os#iO", &py_chain, &py_hash, &py_size, &py_require_confirmed,&py_callback)) {
        return NULL;
    }
#endif

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    hash_t hash;
    memcpy(hash.hash, py_hash, 32);
    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);
    chain_fetch_transaction_position(chain, py_callback, hash, py_require_confirmed, chain_fetch_transaction_position_handler);
    Py_RETURN_NONE;
}

void chain_organize_handler(chain_t chain, void* ctx, int error) {
    PyObject* py_callback = ctx;
    PyObject* arglist = Py_BuildValue("(i)", error);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}

PyObject* bitprim_native_chain_organize_block(PyObject* self, PyObject* args){

    PyObject* py_chain;
    PyObject* py_block;
    PyObject* py_callback;


    if ( ! PyArg_ParseTuple(args, "OOO", &py_chain, &py_block, &py_callback)) {
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    chain_t chain = (chain_t)get_ptr(py_chain);
    block_t block = get_ptr(py_block);

    Py_XINCREF(py_callback);
    chain_organize_block(chain, py_callback, block, chain_organize_handler);
    Py_RETURN_NONE;
}

PyObject* bitprim_native_chain_organize_transaction(PyObject* self, PyObject* args){

    PyObject* py_chain;
    PyObject* py_transaction;
    PyObject* py_callback;


    if ( ! PyArg_ParseTuple(args, "OOO", &py_chain, &py_transaction, &py_callback)) {
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    chain_t chain = (chain_t)get_ptr(py_chain);
    transaction_t transaction = get_ptr(py_transaction);

    Py_XINCREF(py_callback);
    chain_organize_transaction(chain, py_callback, transaction, chain_organize_handler);
    Py_RETURN_NONE;
}

void chain_validate_tx_handler(chain_t chain, void* ctx, int error, char* msg) {
    PyObject* py_callback = ctx;
    PyObject* arglist = Py_BuildValue("(is)", error, msg);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}

PyObject* bitprim_native_chain_validate_tx(PyObject* self, PyObject* args){
    PyObject* py_chain;
    PyObject* py_transaction;
    PyObject* py_callback;


    if ( ! PyArg_ParseTuple(args, "OOO", &py_chain, &py_transaction, &py_callback)) {
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    chain_t chain = (chain_t)get_ptr(py_chain);
    transaction_t transaction = get_ptr(py_transaction);

    Py_XINCREF(py_callback);
    chain_validate_tx(chain, py_callback, transaction, chain_validate_tx_handler);
    Py_RETURN_NONE;
}





void chain_fetch_compact_block_handler(chain_t chain, void* ctx, int error , compact_block_t compact, size_t h) {
    PyObject* py_callback = ctx;
    PyObject* py_compact = to_py_obj(compact);

    PyObject* arglist = Py_BuildValue("(iOi)", error, py_compact, h);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}


PyObject * bitprim_native_chain_fetch_compact_block_by_height(PyObject* self, PyObject* args){
    PyObject* py_chain;
    Py_ssize_t py_height;
    PyObject* py_callback;
    if ( ! PyArg_ParseTuple(args, "OnO", &py_chain, &py_height, &py_callback)) {
        //printf("bitprim_native_chain_fetch_block_header_by_height - 2\n");
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_compact_block_by_height(chain, py_callback, py_height, chain_fetch_compact_block_handler);
    Py_RETURN_NONE;
}



PyObject * bitprim_native_chain_fetch_compact_block_by_hash(PyObject* self, PyObject* args){
    PyObject* py_chain;
    char* py_hash;
    size_t py_size;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy#O", &py_chain, &py_hash, &py_size, &py_callback)) {
        return NULL;
    }
#else
    if ( ! PyArg_ParseTuple(args, "Os#O", &py_chain, &py_hash, &py_size, &py_callback)) {
        return NULL;
    }
#endif


    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }


    hash_t hash;
    memcpy(hash.hash, py_hash, 32);

    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_compact_block_by_hash(chain, py_callback, hash, chain_fetch_compact_block_handler);

    Py_RETURN_NONE;
}


void chain_fetch_spend_handler(chain_t chain, void* ctx, int error , point_t point) {
    PyObject* py_callback = ctx;
    PyObject* py_point = to_py_obj(point);

    PyObject* arglist = Py_BuildValue("(iO)", error, py_point);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}

PyObject * bitprim_native_chain_fetch_spend(PyObject* self, PyObject* args){
    PyObject* py_chain;
    PyObject* py_output_point;
    PyObject* py_callback;

    printf("bitprim_native_chain_fetch_spend 1\n");
    if ( ! PyArg_ParseTuple(args, "OOO", &py_chain, &py_output_point, &py_callback)) {
        return NULL;
    }

    printf("bitprim_native_chain_fetch_spend 2\n");
    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    printf("bitprim_native_chain_fetch_spend 3\n");
    chain_t chain = (chain_t)get_ptr(py_chain);

    printf("bitprim_native_chain_fetch_spend 4 %p \n", py_output_point);
    output_point_t output_point = (output_point_t)get_ptr(py_output_point);

    printf("bitprim_native_chain_fetch_spend 5 %p\n", output_point);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */

    printf("bitprim_native_chain_fetch_spend 6\n");
    chain_fetch_spend(chain, py_callback, output_point, chain_fetch_spend_handler);

    printf("bitprim_native_chain_fetch_spend 7\n");
    Py_RETURN_NONE;
}

PyObject * bitprim_native_chain_fetch_spend_hash_index(PyObject* self, PyObject* args){
    PyObject* py_chain;
    char* py_hash;
    size_t py_size;
    uint32_t py_index;
    PyObject* py_callback;
    //printf("bitprim_native_chain_fetch_spend_hash_index 1\n");
#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "y#IOO",  &py_hash, &py_size, &py_index, &py_chain, &py_callback)) {
        return NULL;
    }
#else
    if ( ! PyArg_ParseTuple(args, "s#IOO", &py_hash, &py_size, &py_index, &py_chain, &py_callback)) {
        return NULL;
    }
#endif

    //printf("bitprim_native_chain_fetch_spend_hash_index 2   %s\n", py_hash);
    hash_t hash;
    memcpy(hash.hash, py_hash, 32);
    //printf("bitprim_native_chain_fetch_spend_hash_index 3   %s\n", py_hash);
    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }
    //printf("bitprim_native_chain_fetch_spend_hash_index 4   %s\n", py_hash);
    chain_t chain = (chain_t)get_ptr(py_chain);
    //printf("bitprim_native_chain_fetch_spend_hash_index 5   %s\n", py_hash);
    output_point_t p = output_point_construct_from_hash_index(hash, py_index);
    Py_XINCREF(py_callback);
    chain_fetch_spend(chain, py_callback, p, chain_fetch_spend_handler);
    Py_RETURN_NONE;
}

/*

/////////////////// input point

//It is the user's responsibility to release the input point returned in the callback
void chain_fetch_spend(chain_t chain, void* ctx, output_point_t outpoint, spend_fetch_handler_t handler) {
    libbitcoin::chain::output_point* outpoint_cpp = static_cast<libbitcoin::chain::output_point*>(outpoint);

    safe_chain(chain).fetch_spend(*outpoint_cpp, [chain, ctx, handler](std::error_code const& ec, libbitcoin::chain::input_point input_point) {
        auto new_input_point = new libbitcoin::chain::input_point(input_point);
        handler(chain, ctx, ec.value(), new_input_point);
    });
}




void chain_subscribe_reorganize(chain_t chain, void* ctx, reorganize_handler_t handler) {
    safe_chain(chain).subscribe_reorganize([chain, ctx, handler](std::error_code const& ec, size_t fork_height, libbitcoin::block_const_ptr_list_const_ptr incoming, libbitcoin::block_const_ptr_list_const_ptr replaced_blocks) {
//        auto new_history = new libbitcoin::chain::history_compact::list(history);

        auto* incoming_cpp = chain_block_list_construct_default();
        for (auto&& x : *incoming) {
            auto new_block = new libbitcoin::message::block(*x.get());
            chain_block_list_push_back(incoming_cpp, new_block);
        }

        auto* replaced_blocks_cpp = chain_block_list_construct_default();
        for (auto&& x : *replaced_blocks) {
            auto new_block = new libbitcoin::message::block(*x.get());
            chain_block_list_push_back(replaced_blocks_cpp, new_block);
        }

        return handler(chain, ctx, ec.value(), fork_height, incoming_cpp, replaced_blocks_cpp);
    });
}

void chain_subscribe_transaction(chain_t chain, void* ctx, transaction_handler_t handler) {
    safe_chain(chain).subscribe_transaction([chain, ctx, handler](std::error_code const& ec, libbitcoin::transaction_const_ptr tx) {
        auto new_tx = new libbitcoin::message::transaction(*tx.get());
        return handler(chain, ctx, ec.value(), new_tx);
    });
}






*/



