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

//TODO: migrate to the new API for Extension Modules
//          https://docs.python.org/3/howto/cporting.html

#include <Python.h>

#include <bitprim/nodecint.h>
// #include <bitprim/nodecint/chain.h>
// #include <bitprim/nodecint/chain/payment_address.h>
// #include <bitprim/nodecint/chain/history_compact_list.h>
// #include <bitprim/nodecint/chain/history_compact.h>
// #include <bitprim/nodecint/chain/point.h>
// #include <bitprim/nodecint/wallet/word_list.h>



// ---------------------------------------------------------

static inline
void* get_ptr(PyObject* obj) {
#if PY_MAJOR_VERSION >= 3
    return PyCapsule_GetPointer(obj, NULL);
#else /* PY_MAJOR_VERSION >= 3 */
    return PyCObject_AsVoidPtr(obj);
#endif /* PY_MAJOR_VERSION >= 3 */
}

static inline
executor_t cast_executor(PyObject* obj) {
    return (executor_t)get_ptr(obj);
}

static inline
PyObject* to_py_obj(void* obj) {
#if PY_MAJOR_VERSION >= 3
    return PyCapsule_New(obj, NULL, NULL);
#else /* PY_MAJOR_VERSION >= 3 */
    return PyCObject_FromVoidPtr(obj, NULL);
#endif /* PY_MAJOR_VERSION >= 3 */
}


// ---------------------------------------------------------

static
PyObject* bitprim_native_executor_construct(PyObject* self, PyObject* args) {
    char const* path;
    PyObject* py_out;
    PyObject* py_err;


    if ( ! PyArg_ParseTuple(args, "sOO", &path, &py_out, &py_err))
        return NULL;

#if PY_MAJOR_VERSION >= 3
    int sout_fd = py_out == Py_None ? -1 : PyObject_AsFileDescriptor(py_out);
    int serr_fd = py_err == Py_None ? -1 : PyObject_AsFileDescriptor(py_err);

    executor_t exec = executor_construct_fd(path, sout_fd, serr_fd);
    printf("bitprim_native_executor_construct exec: %p\n", exec);
    return PyCapsule_New(exec, NULL, NULL);

#else /* PY_MAJOR_VERSION >= 3 */
    FILE* sout = py_out == Py_None ? NULL : PyFile_AsFile(py_out);
    FILE* serr = py_err == Py_None ? NULL : PyFile_AsFile(py_err);
//    PyFile_IncUseCount(p);
///* ... */
//    Py_BEGIN_ALLOW_THREADS
//        do_something(fp);
//    Py_END_ALLOW_THREADS
///* ... */
//        PyFile_DecUseCount(p);

    executor_t exec = executor_construct(path, sout, serr);
    printf("bitprim_native_executor_construct exec: %p\n", exec);
    return PyCObject_FromVoidPtr(exec, NULL);

#endif /* PY_MAJOR_VERSION >= 3 */

}


// ---------------------------------------------------------


static
PyObject* bitprim_native_executor_destruct(PyObject* self, PyObject* args) {
    PyObject* py_exec;

    if ( ! PyArg_ParseTuple(args, "O", &py_exec))
        return NULL;

    executor_t exec = cast_executor(py_exec);

    executor_destruct(exec);
    Py_RETURN_NONE;
}

// ---------------------------------------------------------

static
PyObject* bitprim_native_executor_initchain(PyObject* self, PyObject* args) {

    printf("C bitprim_native_executor_initchain called\n");

    PyObject* py_exec;

    if ( ! PyArg_ParseTuple(args, "O", &py_exec)) {
        return NULL;
    }

    executor_t exec = cast_executor(py_exec);

    int res = executor_initchain(exec);

    return Py_BuildValue("i", res);
}

// ---------------------------------------------------------

static
void executor_run_handler(executor_t exec, void* ctx, int error) {
    printf("C callback (executor_run_handler) called\n");
    // printf("Calling Python callback\n");
    
    PyObject* py_callback = ctx;

    PyObject* arglist = Py_BuildValue("(i)", error);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);
    Py_XDECREF(py_callback);  // Dispose of the call
}


static
PyObject* bitprim_native_executor_run(PyObject* self, PyObject* args) {
    PyObject* py_exec;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OO:set_callback", &py_exec, &py_callback)) {
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    executor_t exec = cast_executor(py_exec);
    Py_XINCREF(py_callback);         // Add a reference to new callback
    executor_run(exec, py_callback, executor_run_handler);
    Py_RETURN_NONE;
}


// ---------------------------------------------------------

static
PyObject* bitprim_native_executor_run_wait(PyObject* self, PyObject* args) {
    PyObject* py_exec;

    if ( ! PyArg_ParseTuple(args, "O", &py_exec))
        return NULL;

    executor_t exec = cast_executor(py_exec);

    int res = executor_run_wait(exec);
    return Py_BuildValue("i", res);
}

// ---------------------------------------------------------

static
PyObject* bitprim_native_executor_stop(PyObject* self, PyObject* args) {
    PyObject* py_exec;

    if ( ! PyArg_ParseTuple(args, "O", &py_exec))
        return NULL;

    executor_t exec = cast_executor(py_exec);

    executor_stop(exec);
    Py_RETURN_NONE;
}

static
PyObject* bitprim_native_executor_get_chain(PyObject* self, PyObject* args) {
    PyObject* py_exec;
    if ( ! PyArg_ParseTuple(args, "O", &py_exec))
        return NULL;

    executor_t exec = cast_executor(py_exec);
    chain_t chain = executor_get_chain(exec);

// #if PY_MAJOR_VERSION >= 3
//     PyObject* py_chain = PyCapsule_New(chain, NULL, NULL);
// #else /* PY_MAJOR_VERSION >= 3 */
//     PyObject* py_chain = PyCObject_FromVoidPtr(chain, NULL);
// #endif /* PY_MAJOR_VERSION >= 3 */

    PyObject* py_chain = to_py_obj(chain);
    return Py_BuildValue("O", py_chain);
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

static
PyObject* bitprim_native_chain_fetch_last_height(PyObject* self, PyObject* args) {
    PyObject* py_exec;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OO:set_callback", &py_exec, &py_callback)) {
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
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

// static PyObject* global_callback_2 = NULL;


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

static
PyObject* bitprim_native_chain_fetch_history(PyObject* self, PyObject* args) {
    PyObject* py_exec;
    char* address_str;
    uint64_t py_limit;
    uint64_t py_from_height;
    PyObject* py_callback;

    // printf("bitprim_native_chain_fetch_history - 1\n");

    if ( ! PyArg_ParseTuple(args, "OsKKO:set_callback", &py_exec, &address_str, &py_limit, &py_from_height, &py_callback)) {
        // printf("bitprim_native_chain_fetch_history - 2\n");
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
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


// int char2int(char input) {
//     if (input >= '0' && input <= '9')
//         return input - '0';
//     if (input >= 'A' && input <= 'F')
//         return input - 'A' + 10;
//     if (input >= 'a' && input <= 'f')
//         return input - 'a' + 10;
//     return 0;
// }

// void hex2bin(const char* src, uint8_t* target) {
//     int i=0;
//     while (*src && src[1]) {
//         *(target--) = char2int(*src) * 16 + char2int(src[1]);
//         src += 2;
//         i++;
//     }
// }

static
PyObject* bitprim_native_chain_fetch_block_height(PyObject* self, PyObject* args) {
    PyObject* py_exec;
    // PyObject* py_hash;
    Py_buffer py_hash;
    PyObject* py_callback;
    
    // if ( ! PyArg_ParseTuple(args, "OOO:set_callback", &py_exec, &py_hash, &py_callback)) {
    if ( ! PyArg_ParseTuple(args, "Oy*O:set_callback", &py_exec, &py_hash, &py_callback)) {
        // printf("bitprim_native_fetch_block_height - 2\n");
        return NULL;
    }

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
    memcpy(hash.hash, py_hash.buf, 32);

    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_block_height(exec, py_callback, hash, chain_block_height_fetch_handler);
    Py_RETURN_NONE;
}


// // ---------------------------------------------------------
// // stealth_history
// // ---------------------------------------------------------

// /////STEALTH FETCH HANDLER
// void chain_stealth_fetch_handler(chain_t chain, void* ctx, int error, stealth_compact_list_t stealth_list) {
//     PyObject* py_callback = ctx;

// #if PY_MAJOR_VERSION >= 3
//     PyObject* py_stealth_list = PyCapsule_New(stealth_list, NULL, NULL);
// #else /* PY_MAJOR_VERSION >= 3 */
//     PyObject* py_stealth_list = PyCObject_FromVoidPtr(stealth_list, NULL);
// #endif /* PY_MAJOR_VERSION >= 3 */

//     void* ptr_void = PyCapsule_GetPointer(py_stealth_list, NULL);
//     int is_valid = PyCapsule_IsValid(py_stealth_list, NULL);


//     PyObject* arglist = Py_BuildValue("(iO)", error, py_stealth_list);
//     PyObject_CallObject(py_callback, arglist);
//     Py_DECREF(arglist);    
//     Py_XDECREF(py_callback);  // Dispose of the call
// }


// //void fetch_stealth(executor_t exec, binary_t filter, size_t from_height, stealth_fetch_handler_t handler)
// static
// PyObject* bitprim_native_chain_fetch_stealth(PyObject* self, PyObject* args) {
//     PyObject* py_exec;
//     PyObject* py_filter;
//     Py_ssize_t py_from_height;
//     PyObject* py_callback;

//     if ( ! PyArg_ParseTuple(args, "OOnO:set_callback", &py_exec, &py_filter, &py_from_height, &py_callback)) {
//         return NULL;
//     }

//     if ( ! PyCallable_Check(py_callback)) {
//         PyErr_SetString(PyExc_TypeError, "parameter must be callable");
//         return NULL;
//     }    

//     executor_t exec = (executor_t)PyCapsule_GetPointer(py_exec, NULL);

//     Py_XINCREF(py_callback);         /* Add a reference to new callback */

//     binary_t binary_filter = (binary_t)PyCapsule_GetPointer(py_filter, NULL);
//     chain_fetch_stealth(exec, py_callback, binary_filter, py_from_height, chain_stealth_fetch_handler);

//     Py_RETURN_NONE;
// }


// -------------------------------------------------------------------
// history_compact_list
// -------------------------------------------------------------------

static
PyObject* bitprim_native_history_compact_list_destruct(PyObject* self, PyObject* args) {
    PyObject* py_history_compact_list;

    if ( ! PyArg_ParseTuple(args, "O", &py_history_compact_list)) {
        // printf("bitprim_native_history_compact_list_count - 2\n");
        return NULL;
    }

    // history_compact_list_t list = (executor_t)PyCObject_AsVoidPtr(py_history_compact_list);
    history_compact_list_t list = (history_compact_list_t)PyCapsule_GetPointer(py_history_compact_list, NULL);
    history_compact_list_destruct(list);

    Py_RETURN_NONE;
}

static
PyObject* bitprim_native_history_compact_list_count(PyObject* self, PyObject* args) {
    PyObject* py_history_compact_list;

    if ( ! PyArg_ParseTuple(args, "O", &py_history_compact_list)) {
        // printf("bitprim_native_history_compact_list_count - 2\n");
        return NULL;
    }

    // history_compact_list_t list = (executor_t)PyCObject_AsVoidPtr(py_history_compact_list);
    history_compact_list_t list = (history_compact_list_t)PyCapsule_GetPointer(py_history_compact_list, NULL);
    size_t res = history_compact_list_count(list);

    return Py_BuildValue("i", res);
}

static
PyObject* bitprim_native_history_compact_list_nth(PyObject* self, PyObject* args) {
    PyObject* py_history_compact_list;
    uint64_t py_n;

    if ( ! PyArg_ParseTuple(args, "OK", &py_history_compact_list, &py_n)) {
        // printf("bitprim_native_history_compact_list_count - 2\n");
        return NULL;
    }

    // history_compact_list_t list = (executor_t)PyCObject_AsVoidPtr(py_history_compact_list);
    history_compact_list_t list = (history_compact_list_t)PyCapsule_GetPointer(py_history_compact_list, NULL);
    history_compact_t hc = history_compact_list_nth(list, py_n);

// #if PY_MAJOR_VERSION >= 3
//     PyObject* py_hc = PyCapsule_New(hc, NULL, NULL);
// #else /* PY_MAJOR_VERSION >= 3 */
//     PyObject* py_hc = PyCObject_FromVoidPtr(hc, NULL);
// #endif /* PY_MAJOR_VERSION >= 3 */
    
    PyObject* py_hc = to_py_obj(hc);
    return Py_BuildValue("O", py_hc);
}

// -------------------------------------------------------------------


// -------------------------------------------------------------------
// history_compact
// -------------------------------------------------------------------

static
PyObject* bitprim_native_history_compact_get_point_kind(PyObject* self, PyObject* args) {
    PyObject* py_history_compact;

    if ( ! PyArg_ParseTuple(args, "O", &py_history_compact)) {
        // printf("bitprim_native_history_compact_get_point_kind - 2\n");
        return NULL;
    }

    // history_compact_t hist = (history_compact_t)PyCObject_AsVoidPtr(py_history_compact);
    history_compact_t hist = (history_compact_t)PyCapsule_GetPointer(py_history_compact, NULL);
    uint64_t res = history_compact_get_point_kind(hist);

    return Py_BuildValue("K", res);
}

static
PyObject* bitprim_native_history_compact_get_point(PyObject* self, PyObject* args) {
    PyObject* py_history_compact;

    if ( ! PyArg_ParseTuple(args, "O", &py_history_compact)) {
        // printf("bitprim_native_history_compact_get_point - 2\n");
        return NULL;
    }

    // history_compact_t hist = (history_compact_t)PyCObject_AsVoidPtr(py_history_compact);
    history_compact_t hist = (history_compact_t)PyCapsule_GetPointer(py_history_compact, NULL);
    point_t p = history_compact_get_point(hist);

    // printf("bitprim_native_history_compact_get_point - p: %p\n", p);

// #if PY_MAJOR_VERSION >= 3
//     PyObject* py_p = PyCapsule_New(p, NULL, NULL);
// #else /* PY_MAJOR_VERSION >= 3 */
//     PyObject* py_p = PyCObject_FromVoidPtr(p, NULL);
// #endif /* PY_MAJOR_VERSION >= 3 */

    PyObject* py_p = to_py_obj(p);
    return Py_BuildValue("O", py_p);
}

static
PyObject* bitprim_native_history_compact_get_height(PyObject* self, PyObject* args) {
    PyObject* py_history_compact;

    if ( ! PyArg_ParseTuple(args, "O", &py_history_compact)) {
        // printf("bitprim_native_history_compact_get_height - 2\n");
        return NULL;
    }

    // history_compact_t hist = (history_compact_t)PyCObject_AsVoidPtr(py_history_compact);
    history_compact_t hist = (history_compact_t)PyCapsule_GetPointer(py_history_compact, NULL);
    uint64_t res = history_compact_get_height(hist);

    return Py_BuildValue("K", res);
}
static
PyObject* bitprim_native_history_compact_get_value_or_previous_checksum(PyObject* self, PyObject* args) {
    PyObject* py_history_compact;

    if ( ! PyArg_ParseTuple(args, "O", &py_history_compact)) {
        // printf("bitprim_native_history_compact_get_value_or_previous_checksum - 2\n");
        return NULL;
    }

    // history_compact_t hist = (history_compact_t)PyCObject_AsVoidPtr(py_history_compact);
    history_compact_t hist = (history_compact_t)PyCapsule_GetPointer(py_history_compact, NULL);
    uint64_t res = history_compact_get_value_or_previous_checksum(hist);

    return Py_BuildValue("K", res);
}



// -------------------------------------------------------------------
// point
// -------------------------------------------------------------------

// hash_t point_get_hash(point_t point){
// int /*bool*/ point_is_valid(point_t point){
// uint32_t point_get_index(point_t point){
// uint64_t point_get_checksum(point_t point){

static
PyObject* bitprim_native_point_get_hash(PyObject* self, PyObject* args) {
    PyObject* py_point;
        // printf("bitprim_native_point_get_hash - 1\n");

    if ( ! PyArg_ParseTuple(args, "O", &py_point)) {
        // printf("bitprim_native_point_get_hash - 2\n");
        return NULL;
    }

    // printf("bitprim_native_point_get_hash - 3\n");

    // point_t p = (point_t)PyCObject_AsVoidPtr(py_point);
    point_t p = (point_t)PyCapsule_GetPointer(py_point, NULL);

    // printf("bitprim_native_point_get_hash - p: %p\n", p);

    hash_t res = point_get_hash(p);

    // printf("bitprim_native_point_get_hash - 4\n");

    return Py_BuildValue("y#", res.hash, 32);    //TODO: warning, hardcoded hash size!
}

static
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

static
PyObject* bitprim_native_point_get_index(PyObject* self, PyObject* args) {
    PyObject* py_point;

    if ( ! PyArg_ParseTuple(args, "O", &py_point)) {
        // printf("bitprim_native_point_get_index - 2\n");
        return NULL;
    }

    // point_t p = (point_t)PyCObject_AsVoidPtr(py_point);
    point_t p = (point_t)PyCapsule_GetPointer(py_point, NULL);
    uint32_t res = point_get_index(p);
    return Py_BuildValue("K", res);
}
static
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


// -------------------------------------------------------------------

// word_list_t word_list_construct() {
// void point_list_destruct(word_list_t word_list) {
// void word_list_add_word(word_list_t word_list, char const* word) {


static
PyObject* bitprim_native_word_list_construct(PyObject* self, PyObject* args) {
    word_list_t wl = word_list_construct();

// #if PY_MAJOR_VERSION >= 3
//     return PyCapsule_New(wl, NULL, NULL);
// #else /* PY_MAJOR_VERSION >= 3 */
//     return PyCObject_FromVoidPtr(wl, NULL);
// #endif /* PY_MAJOR_VERSION >= 3 */
    return to_py_obj(wl);

}

static
PyObject* bitprim_native_word_list_destruct(PyObject* self, PyObject* args) {
    PyObject* py_wl;

    if ( ! PyArg_ParseTuple(args, "O", &py_wl))
        return NULL;

    // word_list_t wl = (word_list_t)PyCObject_AsVoidPtr(py_wl);
    word_list_t wl = (word_list_t)PyCapsule_GetPointer(py_wl, NULL);

    word_list_destruct(wl);
    Py_RETURN_NONE;
}


static
PyObject* bitprim_native_word_list_add_word(PyObject* self, PyObject* args) {
    PyObject* py_wl;
    char const* word;

    if ( ! PyArg_ParseTuple(args, "Os", &py_wl, &word))
        return NULL;

    // word_list_t wl = (word_list_t)PyCObject_AsVoidPtr(py_wl);
    word_list_t wl = (word_list_t)PyCapsule_GetPointer(py_wl, NULL);

    word_list_add_word(wl, word);
    Py_RETURN_NONE;
}


// -------------------------------------------------------------------

// long_hash_t wallet_mnemonics_to_seed(word_list_t mnemonics){
//     auto hash_cpp = libbitcoin::wallet::decode_mnemonic(*static_cast<const std::vector<std::string>*>(mnemonics));
//     return hash_cpp.data();
// }


static
PyObject* bitprim_native_wallet_mnemonics_to_seed(PyObject* self, PyObject* args) {
    PyObject* py_wl;
    printf("bitprim_native_wallet_mnemonics_to_seed - 1\n");

    if ( ! PyArg_ParseTuple(args, "O", &py_wl)) {
        printf("bitprim_native_wallet_mnemonics_to_seed - 2\n");
        return NULL;
    }

    // word_list_t wl = (word_list_t)PyCObject_AsVoidPtr(py_wl);
    word_list_t wl = (word_list_t)PyCapsule_GetPointer(py_wl, NULL);
    
    long_hash_t res = wallet_mnemonics_to_seed(wl);

    printf("bitprim_native_wallet_mnemonics_to_seed - res: %p\n", res.hash);

    return Py_BuildValue("y#", res.hash, 64);    //TODO: warning, hardcoded hash size!


// #if PY_MAJOR_VERSION >= 3
//     PyObject* py_res = PyCapsule_New(res, NULL, NULL);
// #else /* PY_MAJOR_VERSION >= 3 */
//     PyObject* py_res = PyCObject_FromVoidPtr(res, NULL);
// #endif /* PY_MAJOR_VERSION >= 3 */

//     printf("bitprim_native_wallet_mnemonics_to_seed - 3\n");
//     return Py_BuildValue("O", py_res);

}

// static
// PyObject* bitprim_native_long_hash_t_to_str(PyObject* self, PyObject* args) {
//     PyObject* py_lh;

//     printf("bitprim_native_long_hash_t_to_str - 1\n");

//     if ( ! PyArg_ParseTuple(args, "O", &py_lh)) {
//         printf("bitprim_native_long_hash_t_to_str - 2\n");
//         return NULL;
//     }

//     // long_hash_t lh = (long_hash_t)PyCObject_AsVoidPtr(py_lh);
//     long_hash_t lh = (long_hash_t)PyCapsule_GetPointer(py_lh, NULL);

//     printf("bitprim_native_long_hash_t_to_str - res: %p\n", lh);

//     printf("bitprim_native_long_hash_t_to_str - 3\n");

//     return Py_BuildValue("y#", lh, 32 * 2);    //TODO: warning, hardcoded long hash size!
// }

// static
// PyObject* bitprim_native_long_hash_t_free(PyObject* self, PyObject* args) {
//     PyObject* py_lh;

//     printf("bitprim_native_long_hash_t_free - 1\n");

//     if ( ! PyArg_ParseTuple(args, "O", &py_lh)) {
//         printf("bitprim_native_long_hash_t_free - 2\n");
//         return NULL;
//     }

//     // long_hash_t lh = (long_hash_t)PyCObject_AsVoidPtr(py_lh);
//     long_hash_t lh = (long_hash_t)PyCapsule_GetPointer(py_lh, NULL);
//     printf("bitprim_native_long_hash_t_free - res: %p\n", lh);
//     printf("bitprim_native_long_hash_t_free - 3\n");
    
//     // free(lh);
//     long_hash_destroy(lh);

//     printf("bitprim_native_long_hash_t_free - 4\n");
//     Py_RETURN_NONE;
// }

// // -------------------------------------------------------------------
// // binary
// // -------------------------------------------------------------------

// static
// PyObject * bitprim_native_binary_construct(PyObject* self, PyObject* args){

//     auto binary = binary_construct();

// #if PY_MAJOR_VERSION >= 3
//     return PyCapsule_New(binary, NULL, NULL);
// #else /* PY_MAJOR_VERSION >= 3 */
//     return PyCObject_FromVoidPtr(binary, NULL);
// #endif /* PY_MAJOR_VERSION >= 3 */
// }

// static
// PyObject * bitprim_native_binary_construct_string(PyObject* self, PyObject* args){

//     char const* filter;

//     if ( ! PyArg_ParseTuple(args, "s", &filter)) {
//         printf("bitprim_native_binary_construct_string - 2\n");
//         return NULL;
//     }

//     binary_t binary = binary_construct_string(filter);

// #if PY_MAJOR_VERSION >= 3
//     return PyCapsule_New(binary, NULL, NULL);
// #else /* PY_MAJOR_VERSION >= 3 */
//     return PyCObject_FromVoidPtr(binary, NULL);
// #endif /* PY_MAJOR_VERSION >= 3 */
// }



// static
// PyObject * bitprim_native_binary_construct_blocks(PyObject* self, PyObject* args){

//     Py_ssize_t bits_size;
//     Py_ssize_t lenght;
//     PyObject* blocks;

//     if ( ! PyArg_ParseTuple(args, "nnO", &bits_size, &lenght, &blocks)) {
//         return NULL;
//     }

//     if(PySequence_Check(blocks)) { //Check if its an array
//         int size = PySequence_Size(blocks); //get array size
//         uint8_t *result = malloc(sizeof(uint8_t) * size); // reserve memory
//         for(int i = 0; i < size; i++) {
//             PyObject* item = PySequence_GetItem(blocks, i); //read every item in the array
//             if(PyInt_Check(item)) { //check if the item its an integer
//                result[i] = PyInt_AsLong(item); //extract the value of the pyobject as int
//             } else {
//                return NULL;
//             }  
//         }
   
// //    for(int i=0; i < 4 ; i++)
// //      printf("block construct %u \n", result[i]);

//     auto binary = binary_construct_blocks(bits_size, result, size);
// #if PY_MAJOR_VERSION >= 3
//     return PyCapsule_New(binary, NULL, NULL);
// #else // PY_MAJOR_VERSION >= 3 
//     return PyCObject_FromVoidPtr(binary, NULL);
// #endif //PY_MAJOR_VERSION >= 3 
//     }

//     return NULL;
// }

// static
// PyObject * bitprim_native_binary_blocks(PyObject* self, PyObject* args){

//     PyObject* binary;

//     if ( ! PyArg_ParseTuple(args, "O", &binary)) {
//         return NULL;
//     }
    
//     binary_t binary_pointer = (binary_t)get_ptr(binary);
//     uint8_t* blocks = (uint8_t*)binary_blocks(binary_pointer);
// //    for(int i=0; i < 4 ; i++)
// //      printf("block %u \n", blocks[i]);


// #if PY_MAJOR_VERSION >= 3
//     return PyCapsule_New(blocks, NULL, NULL);
// #else /* PY_MAJOR_VERSION >= 3 */
//     return PyCObject_FromVoidPtr(blocks, NULL);
// #endif /* PY_MAJOR_VERSION >= 3 */
// }


// static
// PyObject * bitprim_native_binary_encoded(PyObject* self, PyObject* args){

//     PyObject* binary;
//     if ( ! PyArg_ParseTuple(args, "O", &binary)) {
//         printf("bitprim_native_binary_encoded - 2\n");
//         return NULL;
//     }
    
//     binary_t binary_pointer = (binary_t)get_ptr(binary);
//     char* str = (char*)binary_encoded(binary_pointer);

//     return PyString_FromString(str);
// }


// -------------------------------------------------------------------

// -------------------------------------------------------------------
// fetch_block
// -------------------------------------------------------------------

void chain_fetch_block_handler(chain_t chain, void* ctx, int error , block_t block, size_t h) {
    PyObject* py_callback = ctx;

// #if PY_MAJOR_VERSION >= 3
//     PyObject* py_block = PyCapsule_New(block, NULL, NULL);
// #else 
//     PyObject* py_block = PyCObject_FromVoidPtr(block, NULL);
// #endif
    PyObject* py_block = to_py_obj(block);

    //PyCapsule_GetPointer(py_header, NULL);

    PyObject* arglist = Py_BuildValue("(iOi)", error, py_block, h);
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

    if ( ! PyCallable_Check(py_callback)) {
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
    // PyObject* py_hash;
    Py_buffer py_hash;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "Oy*O", &py_exec, &py_hash, &py_callback)) {
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    // char* s = PyString_AsString(py_hash);
    // uint8_t * hash = (uint8_t*) malloc (sizeof(uint8_t[32]));
    // hex2bin(s,&hash[31]);

    hash_t hash;
    // void* memcpy( void* dest, const void* src, std::size_t count );
    memcpy(hash.hash, py_hash.buf, 32);
    

    executor_t exec = cast_executor(py_exec);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_block_by_hash(exec, py_callback, hash, chain_fetch_block_handler);

    Py_RETURN_NONE;
}

// -------------------------------------------------------------------
// fetch_merkle_block
// -------------------------------------------------------------------

void chain_fetch_merkle_block_handler(chain_t chain, void* ctx, int error, merkle_block_t merkle, size_t h) {
    PyObject* py_callback = ctx;

// #if PY_MAJOR_VERSION >= 3
//     PyObject* py_merkle = PyCapsule_New(merkle, NULL, NULL);
// #else 
//     PyObject* py_merkle = PyCObject_FromVoidPtr(merkle, NULL);
// #endif
    PyObject* py_merkle = to_py_obj(merkle);

    //PyCapsule_GetPointer(py_header, NULL);

    PyObject* arglist = Py_BuildValue("(iOi)", error, py_merkle, h);
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
        //printf("bitprim_native_chain_fetch_block_header_by_height - 2\n");
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
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
    // PyObject* py_hash;
    Py_buffer py_hash;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "Oy*O", &py_exec, &py_hash, &py_callback)) {
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    // char* s = PyString_AsString(py_hash);
    // uint8_t * hash = (uint8_t*) malloc (sizeof(uint8_t[32]));
    // hex2bin(s,&hash[31]);


    hash_t hash;
    // void* memcpy( void* dest, const void* src, std::size_t count );
    memcpy(hash.hash, py_hash.buf, 32);

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

  
// #if PY_MAJOR_VERSION >= 3
//     PyObject* py_header = PyCapsule_New(header, NULL, NULL);
// #else 
//     PyObject* py_header = PyCObject_FromVoidPtr(header, NULL);
// #endif
    PyObject* py_header = to_py_obj(header);


    //PyCapsule_GetPointer(py_header, NULL);

    PyObject* arglist = Py_BuildValue("(iOi)", error, py_header, h);
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

    if ( ! PyCallable_Check(py_callback)) {
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
    // PyObject* py_hash;
    Py_buffer py_hash;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "Oy*O", &py_exec, &py_hash, &py_callback)) {
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    // char* s = PyString_AsString(py_hash);
    // uint8_t * hash = (uint8_t*) malloc (sizeof(uint8_t[32]));
    // hex2bin(s,&hash[31]);

    hash_t hash;
    // void* memcpy( void* dest, const void* src, std::size_t count );
    memcpy(hash.hash, py_hash.buf, 32);


    executor_t exec = cast_executor(py_exec);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_block_header_by_hash(exec, py_callback, hash, chain_fetch_block_header_handler);

    Py_RETURN_NONE;
}


// -------------------------------------------------------------------
// merkle_block
// -------------------------------------------------------------------
static
PyObject* bitprim_native_chain_merkle_block_get_header(PyObject* self, PyObject* args){
    PyObject* py_merkle;

    if ( ! PyArg_ParseTuple(args, "O", &py_merkle)) {
        return NULL;
    }

    merkle_block_t merkle_block = (merkle_block_t)get_ptr(py_merkle);
    header_t header = chain_merkle_block_header(merkle_block);

  
// #if PY_MAJOR_VERSION >= 3
//     return PyCapsule_New(header, NULL, NULL);
// #else /* PY_MAJOR_VERSION >= 3 */
//     return PyCObject_FromVoidPtr(header, NULL);
// #endif /* PY_MAJOR_VERSION >= 3 */
    return to_py_obj(header); //TODO: Está bien esto? O tiene que ser un BuildValue????

}

static
PyObject * bitprim_native_chain_merkle_block_is_valid(PyObject* self, PyObject* args){
    PyObject* py_merkle_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_merkle_block)) {
        return NULL;
    }

    merkle_block_t block = (merkle_block_t)get_ptr(py_merkle_block);
    int res = chain_merkle_block_is_valid(block);

    return Py_BuildValue("i", res);   
}

static
PyObject * bitprim_native_chain_merkle_block_hash_count(PyObject* self, PyObject* args){
    PyObject* py_merkle_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_merkle_block)) {
        return NULL;
    }

    merkle_block_t block = (merkle_block_t)get_ptr(py_merkle_block);
    uint64_t /*size_t*/ res = chain_merkle_block_hash_count(block);

    return Py_BuildValue("K", res);   
}


static
PyObject * bitprim_native_chain_merkle_block_total_transaction_count(PyObject* self, PyObject* args){
    PyObject* py_merkle_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_merkle_block)) {
        return NULL;
    }

    merkle_block_t block = (merkle_block_t)get_ptr(py_merkle_block);
    uint64_t /*size_t*/ res = chain_merkle_block_total_transaction_count(block);

    return Py_BuildValue("K", res);   
}



static
PyObject * bitprim_native_chain_merkle_block_serialized_size(PyObject* self, PyObject* args){
    PyObject* py_merkle_block;
    uint32_t py_version;

    if ( ! PyArg_ParseTuple(args, "OI", &py_merkle_block, &py_version)) {
        return NULL;
    }

    merkle_block_t block = (merkle_block_t)get_ptr(py_merkle_block);
    uint64_t /*size_t*/ res = chain_merkle_block_serialized_size(block, py_version);

    return Py_BuildValue("K", res);   
}

static
PyObject * bitprim_native_chain_merkle_block_reset(PyObject* self, PyObject* args){
    PyObject* py_merkle_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_merkle_block)) {
        return NULL;
    }

    merkle_block_t block = (merkle_block_t)get_ptr(py_merkle_block);
    chain_merkle_block_reset(block);

    Py_RETURN_NONE;   
}



// -------------------------------------------------------------------
// block
// -------------------------------------------------------------------
static
PyObject * bitprim_native_chain_block_get_header(PyObject* self, PyObject* args){
    PyObject* py_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    header_t header = chain_block_header(block);

  
// #if PY_MAJOR_VERSION >= 3
//     return PyCapsule_New(header, NULL, NULL);
// #else /* PY_MAJOR_VERSION >= 3 */
//     return PyCObject_FromVoidPtr(header, NULL);
// #endif /* PY_MAJOR_VERSION >= 3 */
    return to_py_obj(header);

}


static
PyObject * bitprim_native_chain_block_transaction_count(PyObject* self, PyObject* args){
    PyObject* py_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    uint64_t /*size_t*/ res = chain_block_transaction_count(block);

    return Py_BuildValue("K", res);   
}



static
PyObject * bitprim_native_chain_block_serialized_size(PyObject* self, PyObject* args){
    PyObject* py_block;
    uint32_t py_version;

    if ( ! PyArg_ParseTuple(args, "OI", &py_block, &py_version)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    uint64_t /*size_t*/ res = chain_block_serialized_size(block, py_version);

    return Py_BuildValue("K", res);   
}


static
PyObject * bitprim_native_chain_block_subsidy(PyObject* self, PyObject* args){
    uint64_t /*size_t*/ py_height;

    if ( ! PyArg_ParseTuple(args, "K", &py_height)) {
        return NULL;
    }

    uint64_t res = chain_block_subsidy(py_height);
    return Py_BuildValue("K", res);
}

static
PyObject * bitprim_native_chain_block_fees(PyObject* self, PyObject* args){
    PyObject* py_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    uint64_t res = chain_block_fees(block);

    return Py_BuildValue("K", res);   
}

static
PyObject * bitprim_native_chain_block_claim(PyObject* self, PyObject* args){
    PyObject* py_block;


    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    uint64_t res = chain_block_claim(block);

    return Py_BuildValue("K", res);   
}

static
PyObject * bitprim_native_chain_block_reward(PyObject* self, PyObject* args){
    PyObject* py_block;
    uint64_t py_height;

    if ( ! PyArg_ParseTuple(args, "OK", &py_block, &py_height)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    uint64_t res = chain_block_reward(block, py_height);

    return Py_BuildValue("K", res);   
}

static
PyObject * bitprim_native_chain_block_generate_merkle_root(PyObject* self, PyObject* args){
    PyObject* py_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    hash_t res = chain_block_generate_merkle_root(block);

    return Py_BuildValue("y#", res.hash, 32);

// #if PY_MAJOR_VERSION >= 3
//     return PyCapsule_New(res, NULL, NULL);
// #else /* PY_MAJOR_VERSION >= 3 */
//     return PyCObject_FromVoidPtr(res, NULL);
// #endif /* PY_MAJOR_VERSION >= 3 */

}

static
PyObject * bitprim_native_chain_block_hash(PyObject* self, PyObject* args){
    PyObject* py_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    hash_t res = chain_block_hash(block);

    return Py_BuildValue("y#", res.hash, 32);

// #if PY_MAJOR_VERSION >= 3
//     return PyCapsule_New(res, NULL, NULL);
// #else /* PY_MAJOR_VERSION >= 3 */
//     return PyCObject_FromVoidPtr(res, NULL);
// #endif /* PY_MAJOR_VERSION >= 3 */

}



// -------------------------------------------------------------------
// header
// -------------------------------------------------------------------


static
PyObject * bitprim_native_chain_header_get_version(PyObject* self, PyObject* args){
    PyObject* py_header;

    if ( ! PyArg_ParseTuple(args, "O", &py_header)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    uint32_t res = chain_header_version(header);

    return Py_BuildValue("I", res);   
}

static
PyObject * bitprim_native_chain_header_set_version(PyObject* self, PyObject* args){
    PyObject* py_header;
    uint32_t py_version;

    if ( ! PyArg_ParseTuple(args, "OI", &py_header, &py_version)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    chain_header_set_version(header, py_version);

    Py_RETURN_NONE;   
}

static
PyObject * bitprim_native_chain_header_get_previous_block_hash(PyObject* self, PyObject* args){
    PyObject* py_header;

    if ( ! PyArg_ParseTuple(args, "O", &py_header)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    hash_t res = chain_header_previous_block_hash(header);

    return Py_BuildValue("y#", res.hash, 32);

// #if PY_MAJOR_VERSION >= 3
//     return PyCapsule_New(res, NULL, NULL);
// #else /* PY_MAJOR_VERSION >= 3 */
//     return PyCObject_FromVoidPtr(res, NULL);
// #endif /* PY_MAJOR_VERSION >= 3 */
}

/*
static
PyObject * bitprim_native_chain_header_set_previous_block_hash(PyObject* self, PyObject* args){
    PyObject* py_header;
    Py_ssize_t py_hash;

    if ( ! PyArg_ParseTuple(args, "OO", &py_header, &py_hash)) {
        return NULL;
    }

    char* s = PyString_AsString(py_hash);
    uint8_t * hash = (uint8_t*) malloc (sizeof(uint8_t[32]));
    hex2bin(s,&hash[31]);

    header_t header = (header_t)get_ptr(py_header);
    header_header_set_previous_block_hash(header, hash);

    Py_RETURN_NONE;   
}

static
PyObject * bitprim_native_chain_header_set_merkle(PyObject* self, PyObject* args){
    PyObject* py_header;
    Py_ssize_t py_merkle;

    if ( ! PyArg_ParseTuple(args, "OO", &py_header, &py_merkle)) {
        return NULL;
    }

    char* s = PyString_AsString(py_merkle);
    uint8_t * hash = (uint8_t*) malloc (sizeof(uint8_t[32]));
    hex2bin(s,&hash[31]);

    header_t header = (header_t)get_ptr(py_header);
    header_header_set_merkle(header, hash);

    Py_RETURN_NONE;   
}

*/
static
PyObject * bitprim_native_chain_header_get_merkle(PyObject* self, PyObject* args){
    PyObject* py_header;

    if ( ! PyArg_ParseTuple(args, "O", &py_header)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    hash_t res = chain_header_merkle(header);

    return Py_BuildValue("y#", res.hash, 32);

// #if PY_MAJOR_VERSION >= 3
//     return PyCapsule_New(res, NULL, NULL);
// #else /* PY_MAJOR_VERSION >= 3 */
//     return PyCObject_FromVoidPtr(res, NULL);
// #endif /* PY_MAJOR_VERSION >= 3 */

}

static
PyObject * bitprim_native_chain_header_get_timestamp(PyObject* self, PyObject* args){
    PyObject* py_header;

    if ( ! PyArg_ParseTuple(args, "O", &py_header)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    uint32_t res = chain_header_timestamp(header);

    return Py_BuildValue("I", res);   
}

static
PyObject * bitprim_native_chain_header_set_timestamp(PyObject* self, PyObject* args){
    PyObject* py_header;
    uint32_t py_timestamp;

    if ( ! PyArg_ParseTuple(args, "OI", &py_header, &py_timestamp)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    chain_header_set_timestamp(header, py_timestamp);

    Py_RETURN_NONE;
}


static
PyObject * bitprim_native_chain_header_get_bits(PyObject* self, PyObject* args){
    PyObject* py_header;

    if ( ! PyArg_ParseTuple(args, "O", &py_header)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    uint32_t res = chain_header_bits(header);

    return Py_BuildValue("I", res);   
}

static
PyObject * bitprim_native_chain_header_set_bits(PyObject* self, PyObject* args){
    PyObject* py_header;
    uint32_t py_bits;

    if ( ! PyArg_ParseTuple(args, "OI", &py_header, &py_bits)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    chain_header_set_bits(header, py_bits);

    Py_RETURN_NONE;
}

static
PyObject * bitprim_native_chain_header_get_nonce(PyObject* self, PyObject* args){
    PyObject* py_header;

    if ( ! PyArg_ParseTuple(args, "O", &py_header)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    uint32_t res = chain_header_nonce(header);

    return Py_BuildValue("I", res);  
}

static
PyObject * bitprim_native_chain_header_set_nonce(PyObject* self, PyObject* args){
    PyObject* py_header;
    uint32_t py_nonce;

    if ( ! PyArg_ParseTuple(args, "OI", &py_header, &py_nonce)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    chain_header_set_nonce(header, py_nonce);

    Py_RETURN_NONE;   
}

static
PyMethodDef BitprimNativeMethods[] = {

    {"construct",  bitprim_native_executor_construct, METH_VARARGS, "Construct the executor object."},
    // {"construct_devnull",  bitprim_native_executor_construct_devnull, METH_VARARGS, "Construct the executor object."},
    {"destruct",  bitprim_native_executor_destruct, METH_VARARGS, "Destruct the executor object."},
    {"initchain",  bitprim_native_executor_initchain, METH_VARARGS, "Directory Initialization."},
    {"run",  bitprim_native_executor_run, METH_VARARGS, "Node run."},
    {"run_wait",  bitprim_native_executor_run_wait, METH_VARARGS, "Node run."},
    {"stop",  bitprim_native_executor_stop, METH_VARARGS, "Node stop."},
    {"get_chain",  bitprim_native_executor_get_chain, METH_VARARGS, "Get Chain."},

    {"chain_fetch_last_height",  bitprim_native_chain_fetch_last_height, METH_VARARGS, "..."},
    {"chain_fetch_history",  bitprim_native_chain_fetch_history, METH_VARARGS, "..."},
    // {"chain_fetch_stealth",  bitprim_native_chain_fetch_stealth, METH_VARARGS, "..."},
    {"chain_fetch_block_height",  bitprim_native_chain_fetch_block_height, METH_VARARGS, "..."},
    {"chain_fetch_block_header_by_height",  bitprim_native_chain_fetch_block_header_by_height, METH_VARARGS, "..."},
    {"chain_fetch_block_header_by_hash",  bitprim_native_chain_fetch_block_header_by_hash, METH_VARARGS, "..."},
    {"chain_fetch_block_by_height",  bitprim_native_chain_fetch_block_by_height, METH_VARARGS, "..."},
    {"chain_fetch_block_by_hash",  bitprim_native_chain_fetch_block_by_hash, METH_VARARGS, "..."},
    {"chain_fetch_merkle_block_by_height",  bitprim_native_chain_fetch_merkle_block_by_height, METH_VARARGS, "..."},
    {"chain_fetch_merkle_block_by_hash",  bitprim_native_chain_fetch_merkle_block_by_hash, METH_VARARGS, "..."},

    // {"binary_construct",  bitprim_native_binary_construct, METH_VARARGS, "..."},
    // {"binary_construct_string",  bitprim_native_binary_construct_string, METH_VARARGS, "..."},
    // {"binary_construct_blocks",  bitprim_native_binary_construct_blocks, METH_VARARGS, "..."},
    // {"binary_blocks",  bitprim_native_binary_blocks, METH_VARARGS, "..."},
    // {"binary_encoded",  bitprim_native_binary_encoded, METH_VARARGS, "..."},


    // {"merkle_block_get_header",  bitprim_native_chain_merkle_block_get_header, METH_VARARGS, "..."},
    // {"merkle_block_is_valid",  bitprim_native_chain_merkle_block_is_valid, METH_VARARGS, "..."},
    // {"merkle_block_hash_count",  bitprim_native_chain_merkle_block_hash_count, METH_VARARGS, "..."},
    // {"merkle_block_serialized_size",  bitprim_native_chain_merkle_block_serialized_size, METH_VARARGS, "..."},
    // {"merkle_block_total_transaction_count",  bitprim_native_chain_merkle_block_total_transaction_count, METH_VARARGS, "..."},
    // {"merkle_block_reset",  bitprim_native_chain_merkle_block_reset, METH_VARARGS, "..."},

    {"block_get_header",  bitprim_native_chain_block_get_header, METH_VARARGS, "..."},
    {"block_hash",  bitprim_native_chain_block_hash, METH_VARARGS, "..."},
    {"block_transaction_count",  bitprim_native_chain_block_transaction_count, METH_VARARGS, "..."},
    {"block_serialized_size",  bitprim_native_chain_block_serialized_size, METH_VARARGS, "..."},
    {"block_fees",  bitprim_native_chain_block_fees, METH_VARARGS, "..."},
    {"block_claim",  bitprim_native_chain_block_claim, METH_VARARGS, "..."},
    {"block_reward",  bitprim_native_chain_block_reward, METH_VARARGS, "..."},
    {"block_generate_merkle_root",  bitprim_native_chain_block_generate_merkle_root, METH_VARARGS, "..."},

    {"header_get_version",  bitprim_native_chain_header_get_version, METH_VARARGS, "..."},
    {"header_set_version",  bitprim_native_chain_header_set_version, METH_VARARGS, "..."},
    {"header_get_previous_block_hash",  bitprim_native_chain_header_get_previous_block_hash, METH_VARARGS, "..."},
    //{"header_set_previous_block_hash",  bitprim_native_chain_header_set_previous_block_hash, METH_VARARGS, "..."},
    {"header_get_merkle",  bitprim_native_chain_header_get_merkle, METH_VARARGS, "..."},
    //{"header_set_merkle",  bitprim_native_chain_header_set_merkle, METH_VARARGS, "..."},
    {"header_get_timestamp",  bitprim_native_chain_header_get_timestamp, METH_VARARGS, "..."},
    {"header_set_timestamp",  bitprim_native_chain_header_set_timestamp, METH_VARARGS, "..."},
    {"header_get_bits",  bitprim_native_chain_header_get_bits, METH_VARARGS, "..."},
    {"header_set_bits",  bitprim_native_chain_header_set_bits, METH_VARARGS, "..."},
    {"header_get_nonce",  bitprim_native_chain_header_get_nonce, METH_VARARGS, "..."},
    {"header_set_nonce",  bitprim_native_chain_header_set_nonce, METH_VARARGS, "..."},

    {"history_compact_list_destruct",  bitprim_native_history_compact_list_destruct, METH_VARARGS, "..."},
    {"history_compact_list_count",  bitprim_native_history_compact_list_count, METH_VARARGS, "..."},
    {"history_compact_list_nth",  bitprim_native_history_compact_list_nth, METH_VARARGS, "..."},
    {"history_compact_get_point_kind",  bitprim_native_history_compact_get_point_kind, METH_VARARGS, "..."},
    {"history_compact_get_point",  bitprim_native_history_compact_get_point, METH_VARARGS, "..."},
    {"history_compact_get_height",  bitprim_native_history_compact_get_height, METH_VARARGS, "..."},
    {"history_compact_get_value_or_previous_checksum",  bitprim_native_history_compact_get_value_or_previous_checksum, METH_VARARGS, "..."},

    {"point_get_hash",  bitprim_native_point_get_hash, METH_VARARGS, "..."},
    {"point_is_valid",  bitprim_native_point_is_valid, METH_VARARGS, "..."},
    {"point_get_index",  bitprim_native_point_get_index, METH_VARARGS, "..."},
    {"point_get_checksum",  bitprim_native_point_get_checksum, METH_VARARGS, "..."},

    {"word_list_construct",  bitprim_native_word_list_construct, METH_VARARGS, "..."},
    {"word_list_destruct",  bitprim_native_word_list_destruct, METH_VARARGS, "..."},
    {"word_list_add_word",  bitprim_native_word_list_add_word, METH_VARARGS, "..."},


    {"wallet_mnemonics_to_seed",  bitprim_native_wallet_mnemonics_to_seed, METH_VARARGS, "..."},

    // {"long_hash_t_to_str",  bitprim_native_long_hash_t_to_str, METH_VARARGS, "..."},
    // {"long_hash_t_free",  bitprim_native_long_hash_t_free, METH_VARARGS, "..."},

    {NULL, NULL, 0, NULL}        /* Sentinel */
};

struct module_state {
    PyObject *error;
};

#if PY_MAJOR_VERSION >= 3
#define GETSTATE(m) ((struct module_state*)PyModule_GetState(m))
#else
#define GETSTATE(m) (&_state)
static struct module_state _state;
#endif

#if PY_MAJOR_VERSION >= 3

static 
int myextension_traverse(PyObject *m, visitproc visit, void *arg) {
    Py_VISIT(GETSTATE(m)->error);
    return 0;
}

static 
int myextension_clear(PyObject *m) {
    Py_CLEAR(GETSTATE(m)->error);
    return 0;
}

static 
struct PyModuleDef moduledef = {
        PyModuleDef_HEAD_INIT,
        "bitprim_native",
        NULL,
        sizeof(struct module_state),
        BitprimNativeMethods,
        NULL,
        myextension_traverse,
        myextension_clear,
        NULL
};

#define INITERROR return NULL

PyMODINIT_FUNC
PyInit_bitprim_native(void)


#else /* PY_MAJOR_VERSION >= 3 */

#define INITERROR return

void /*PyMODINIT_FUNC*/
initbitprim_native(void)

#endif /* PY_MAJOR_VERSION >= 3 */


{
#if PY_MAJOR_VERSION >= 3
    PyObject *module = PyModule_Create(&moduledef);
#else
    PyObject *module = Py_InitModule("bitprim_native", BitprimNativeMethods);
    // (void) Py_InitModule("bitprim_native", BitprimNativeMethods);
#endif

    if (module == NULL) {
        INITERROR;
    }

    struct module_state *st = GETSTATE(module);

    st->error = PyErr_NewException("myextension.Error", NULL, NULL);
    
    if (st->error == NULL) {
        Py_DECREF(module);
        INITERROR;
    }

#if PY_MAJOR_VERSION >= 3
    return module;
#endif
}



