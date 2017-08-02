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
    // PyObject* py_hash;
    char* py_hash;
    size_t py_size;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy*O", &py_exec, &py_hash, &py_size, &py_callback)) {
        return NULL;
    }
#else
    if ( ! PyArg_ParseTuple(args, "Os#O", &py_exec, &py_hash, &py_size, &py_callback)) {
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
    // PyObject* py_hash;
    char* py_hash;
    size_t py_size;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy*O", &py_exec, &py_hash, &py_size, &py_callback)) {
        return NULL;
    }
#else
    if ( ! PyArg_ParseTuple(args, "Os#O", &py_exec, &py_hash, &py_size, &py_callback)) {
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
    // PyObject* py_hash;
    //Py_buffer py_hash;
    char* py_hash;
    size_t py_size;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy*O", &py_exec, &py_hash, &py_size, &py_callback)) {
        return NULL;
    }
#else
    if ( ! PyArg_ParseTuple(args, "Os#O", &py_exec, &py_hash, &py_size, &py_callback)) {
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
    // PyObject* py_hash;
    char* py_hash;
    size_t py_size;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy*O", &py_exec, &py_hash, &py_size, &py_callback)) {
        return NULL;
    }
#else
    if ( ! PyArg_ParseTuple(args, "Os#O", &py_exec, &py_hash, &py_size, &py_callback)) {
        return NULL;
    }
#endif

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    executor_t exec = cast_executor(py_exec);
    
    // char* s = PyString_AsString(py_hash);
    // uint8_t * hash = (uint8_t*) malloc (sizeof(uint8_t[32]));
    // hex2bin(s, &hash[31]);

    hash_t hash;
    // void* memcpy( void* dest, const void* src, std::size_t count );
    memcpy(hash.hash, py_hash, 32);

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

    PyObject* py_stealth_list = to_py_obj(stealth_list);
    PyCapsule_GetPointer(py_stealth_list, NULL);
    PyCapsule_IsValid(py_stealth_list, NULL);

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

void chain_fetch_transaction_handler(chain_t chain, void* ctx, int error, transaction_t transaction, uint64_t height, uint64_t index) {
    PyObject* py_callback = ctx;
    PyObject* py_transaction = to_py_obj(transaction);

    PyObject* arglist = Py_BuildValue("(iOnn)", error, py_transaction, height, index);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}

PyObject* bitprim_native_chain_fetch_transaction(PyObject* self, PyObject* args) {
    PyObject* py_exec;
    // PyObject* py_hash;
    char* py_hash;
    size_t py_size;
    int py_require_confirmed;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy*iO", &py_exec, &py_hash, &py_size, &py_require_confirmed,&py_callback)) {
        return NULL;
    }
#else
    if ( ! PyArg_ParseTuple(args, "Os#iO", &py_exec, &py_hash, &py_size, &py_require_confirmed,&py_callback)) {
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
    Py_XINCREF(py_callback);
    chain_fetch_transaction(exec, py_callback, hash, py_require_confirmed, chain_fetch_transaction_handler);

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
    PyObject* py_exec;
    // PyObject* py_hash;
    char* py_hash;
    size_t py_size;
    uint32_t py_index;
    int py_require_confirmed;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy*LiO", &py_exec, &py_hash, &py_size, &py_index, &py_require_confirmed, &py_callback)) {
        return NULL;
    }
#else
    if ( ! PyArg_ParseTuple(args, "Os#LiO", &py_exec, &py_hash, &py_size, &py_index, &py_require_confirmed, &py_callback)) {
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
    Py_XINCREF(py_callback);
    chain_fetch_output(exec, py_callback, hash, py_index, py_require_confirmed, chain_fetch_output_handler);

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
    PyObject* py_exec;
    // PyObject* py_hash;
    char* py_hash;
    size_t py_size;
    int py_require_confirmed;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy*iO", &py_exec, &py_hash, &py_size, &py_require_confirmed,&py_callback)) {
        return NULL;
    }
#else
    if ( ! PyArg_ParseTuple(args, "Os#iO", &py_exec, &py_hash, &py_size, &py_require_confirmed,&py_callback)) {
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
    Py_XINCREF(py_callback);
    chain_fetch_transaction_position(exec, py_callback, hash, py_require_confirmed, chain_fetch_transaction_position_handler);
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

    PyObject* py_exec;
    PyObject* py_block;
    PyObject* py_callback;


    if ( ! PyArg_ParseTuple(args, "OOO", &py_exec, &py_block, &py_callback)) {
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    executor_t exec = cast_executor(py_exec);
    block_t block = get_ptr(py_block);

    Py_XINCREF(py_callback);
    chain_organize_block(exec, py_callback, block, chain_organize_handler);
    Py_RETURN_NONE;
}

PyObject* bitprim_native_chain_organize_transaction(PyObject* self, PyObject* args){

    PyObject* py_exec;
    PyObject* py_transaction;
    PyObject* py_callback;


    if ( ! PyArg_ParseTuple(args, "OOO", &py_exec, &py_transaction, &py_callback)) {
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    executor_t exec = cast_executor(py_exec);
    transaction_t transaction = get_ptr(py_transaction);

    Py_XINCREF(py_callback);
    chain_organize_transaction(exec, py_callback, transaction, chain_organize_handler);
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
    PyObject* py_exec;
    PyObject* py_transaction;
    PyObject* py_callback;


    if ( ! PyArg_ParseTuple(args, "OOO", &py_exec, &py_transaction, &py_callback)) {
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    executor_t exec = cast_executor(py_exec);
    transaction_t transaction = get_ptr(py_transaction);

    Py_XINCREF(py_callback);
    chain_validate_tx(exec, py_callback, transaction, chain_validate_tx_handler);
    Py_RETURN_NONE;
}





void chain_fetch_compact_block_handler(chain_t chain, void* ctx, int error , compact_block_t compact, size_t h) {
    PyObject* py_callback = ctx;
    get_ptr(compact);
    PyObject* arglist = Py_BuildValue("(iOi)", error, compact, h);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}


PyObject * bitprim_native_chain_fetch_compact_block_by_height(PyObject* self, PyObject* args){
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
    chain_fetch_compact_block_by_height(exec, py_callback, py_height, chain_fetch_compact_block_handler);
    Py_RETURN_NONE;
}



PyObject * bitprim_native_chain_fetch_compact_block_by_hash(PyObject* self, PyObject* args){
    PyObject* py_exec;
    char* py_hash;
    size_t py_size;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy*O", &py_exec, &py_hash, &py_size, &py_callback)) {
        return NULL;
    }
#else
    if ( ! PyArg_ParseTuple(args, "Os#O", &py_exec, &py_hash, &py_size, &py_callback)) {
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
    chain_fetch_compact_block_by_hash(exec, py_callback, hash, chain_fetch_compact_block_handler);

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



