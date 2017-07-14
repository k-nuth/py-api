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

// ---------------------------------------------------------
// chain_fetch_last_height
// ---------------------------------------------------------

void chain_fetch_last_height_handler(executor_t exec, void* ctx, int error, size_t h) {
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

// static PyObject* global_callback_2 = NULL;


void chain_fetch_history_handler(executor_t exec, void* ctx, int error, history_compact_list_t history_list) {

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

static
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
    Py_ssize_t py_n;

    if ( ! PyArg_ParseTuple(args, "On", &py_history_compact_list, &py_n)) {
        // printf("bitprim_native_history_compact_list_count - 2\n");
        return NULL;
    }

    // history_compact_list_t list = (executor_t)PyCObject_AsVoidPtr(py_history_compact_list);
    history_compact_list_t list = (history_compact_list_t)PyCapsule_GetPointer(py_history_compact_list, NULL);
    history_compact_t hc = history_compact_list_nth(list, py_n);

#if PY_MAJOR_VERSION >= 3
    PyObject* py_hc = PyCapsule_New(hc, NULL, NULL);
#else /* PY_MAJOR_VERSION >= 3 */
    PyObject* py_hc = PyCObject_FromVoidPtr(hc, NULL);
#endif /* PY_MAJOR_VERSION >= 3 */


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

#if PY_MAJOR_VERSION >= 3
    PyObject* py_p = PyCapsule_New(p, NULL, NULL);
#else /* PY_MAJOR_VERSION >= 3 */
    PyObject* py_p = PyCObject_FromVoidPtr(p, NULL);
#endif /* PY_MAJOR_VERSION >= 3 */

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

    return Py_BuildValue("y#", res, 32);    //TODO: warning, hardcoded hash size!
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

#if PY_MAJOR_VERSION >= 3
    return PyCapsule_New(wl, NULL, NULL);
#else /* PY_MAJOR_VERSION >= 3 */
    return PyCObject_FromVoidPtr(wl, NULL);
#endif /* PY_MAJOR_VERSION >= 3 */
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

    printf("bitprim_native_wallet_mnemonics_to_seed - res: %p\n", res);

#if PY_MAJOR_VERSION >= 3
    PyObject* py_res = PyCapsule_New(res, NULL, NULL);
#else /* PY_MAJOR_VERSION >= 3 */
    PyObject* py_res = PyCObject_FromVoidPtr(res, NULL);
#endif /* PY_MAJOR_VERSION >= 3 */

    printf("bitprim_native_wallet_mnemonics_to_seed - 3\n");
    return Py_BuildValue("O", py_res);

    // PyObject* py_ret = Py_BuildValue("y#", res, 32 * 2);    //TODO: warning, hardcoded long hash size!

    // // free(res);

    // return py_ret;
}

static
PyObject* bitprim_native_long_hash_t_to_str(PyObject* self, PyObject* args) {
    PyObject* py_lh;

    printf("bitprim_native_long_hash_t_to_str - 1\n");

    if ( ! PyArg_ParseTuple(args, "O", &py_lh)) {
        printf("bitprim_native_long_hash_t_to_str - 2\n");
        return NULL;
    }

    // long_hash_t lh = (long_hash_t)PyCObject_AsVoidPtr(py_lh);
    long_hash_t lh = (long_hash_t)PyCapsule_GetPointer(py_lh, NULL);

    printf("bitprim_native_long_hash_t_to_str - res: %p\n", lh);

    printf("bitprim_native_long_hash_t_to_str - 3\n");

    return Py_BuildValue("y#", lh, 32 * 2);    //TODO: warning, hardcoded long hash size!
}

static
PyObject* bitprim_native_long_hash_t_free(PyObject* self, PyObject* args) {
    PyObject* py_lh;

    printf("bitprim_native_long_hash_t_free - 1\n");

    if ( ! PyArg_ParseTuple(args, "O", &py_lh)) {
        printf("bitprim_native_long_hash_t_free - 2\n");
        return NULL;
    }

    // long_hash_t lh = (long_hash_t)PyCObject_AsVoidPtr(py_lh);
    long_hash_t lh = (long_hash_t)PyCapsule_GetPointer(py_lh, NULL);
    printf("bitprim_native_long_hash_t_free - res: %p\n", lh);
    printf("bitprim_native_long_hash_t_free - 3\n");
    
    // free(lh);
    long_hash_destroy(lh);

    printf("bitprim_native_long_hash_t_free - 4\n");
    Py_RETURN_NONE;
}



// -------------------------------------------------------------------

static
PyMethodDef BitprimNativeMethods[] = {

    {"construct",  bitprim_native_executor_construct, METH_VARARGS, "Construct the executor object."},
    // {"construct_devnull",  bitprim_native_executor_construct_devnull, METH_VARARGS, "Construct the executor object."},
    {"destruct",  bitprim_native_executor_destruct, METH_VARARGS, "Destruct the executor object."},
    {"initchain",  bitprim_native_executor_initchain, METH_VARARGS, "Directory Initialization."},
    {"run",  bitprim_native_executor_run, METH_VARARGS, "Node run."},
    {"run_wait",  bitprim_native_executor_run_wait, METH_VARARGS, "Node run."},
    {"stop",  bitprim_native_executor_stop, METH_VARARGS, "Node stop."},

    {"fetch_last_height",  bitprim_native_chain_fetch_last_height, METH_VARARGS, "..."},
    {"fetch_history",  bitprim_native_chain_fetch_history, METH_VARARGS, "..."},

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

    {"long_hash_t_to_str",  bitprim_native_long_hash_t_to_str, METH_VARARGS, "..."},
    {"long_hash_t_free",  bitprim_native_long_hash_t_free, METH_VARARGS, "..."},

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



