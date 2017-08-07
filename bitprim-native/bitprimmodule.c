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
#include "binary.h"
#include "utils.h"
#include "chain/point.h"
#include "chain/history.h"
#include "chain/chain.h"
#include "chain/block.h"
#include "chain/header.h"
#include "chain/merkle_block.h"
#include "chain/word_list.h"
#include <bitprim/nodecint.h>

// ---------------------------------------------------------


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
    // printf("bitprim_native_executor_construct exec: %p\n", exec);
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

PyObject* bitprim_native_executor_destruct(PyObject* self, PyObject* args) {
    PyObject* py_exec;

    if ( ! PyArg_ParseTuple(args, "O", &py_exec))
        return NULL;

    executor_t exec = cast_executor(py_exec);

    executor_destruct(exec);
    Py_RETURN_NONE;
}

// ---------------------------------------------------------

PyObject* bitprim_native_executor_initchain(PyObject* self, PyObject* args) {

    // printf("C bitprim_native_executor_initchain called\n");

    PyObject* py_exec;

    if ( ! PyArg_ParseTuple(args, "O", &py_exec)) {
        return NULL;
    }

    executor_t exec = cast_executor(py_exec);

    int res = executor_initchain(exec);

    return Py_BuildValue("i", res);
}

// ---------------------------------------------------------

void executor_run_handler(executor_t exec, void* ctx, int error) {
    printf("C callback (executor_run_handler) called\n");
    // printf("Calling Python callback\n");
    
    PyObject* py_callback = ctx;

    PyObject* arglist = Py_BuildValue("(i)", error);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);
    Py_XDECREF(py_callback);  // Dispose of the call
}


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

PyObject* bitprim_native_executor_run_wait(PyObject* self, PyObject* args) {
    PyObject* py_exec;

    if ( ! PyArg_ParseTuple(args, "O", &py_exec))
        return NULL;

    executor_t exec = cast_executor(py_exec);

    int res = executor_run_wait(exec);
    return Py_BuildValue("i", res);
}

// ---------------------------------------------------------

PyObject* bitprim_native_executor_stop(PyObject* self, PyObject* args) {
    PyObject* py_exec;

    if ( ! PyArg_ParseTuple(args, "O", &py_exec))
        return NULL;

    executor_t exec = cast_executor(py_exec);

    executor_stop(exec);
    Py_RETURN_NONE;
}


PyObject* bitprim_native_executor_get_chain(PyObject* self, PyObject* args) {
    PyObject* py_exec;
    if ( ! PyArg_ParseTuple(args, "O", &py_exec))
        return NULL;

    executor_t exec = cast_executor(py_exec);
    chain_t chain = executor_get_chain(exec);

    PyObject* py_chain = to_py_obj(chain);
    return Py_BuildValue("O", py_chain);
}

// -------------------------------------------------------------------

// long_hash_t wallet_mnemonics_to_seed(word_list_t mnemonics){
//     auto hash_cpp = libbitcoin::wallet::decode_mnemonic(*static_cast<const std::vector<std::string>*>(mnemonics));
//     return hash_cpp.data();
// }

PyObject* bitprim_native_wallet_mnemonics_to_seed(PyObject* self, PyObject* args) {
    PyObject* py_wl;
    printf("bitprim_native_wallet_mnemonics_to_seed - 1\n");

    if ( ! PyArg_ParseTuple(args, "O", &py_wl)) {
        printf("bitprim_native_wallet_mnemonics_to_seed - 2\n");
        return NULL;
    }

    word_list_t wl = (word_list_t)get_ptr(py_wl);
    
    long_hash_t res = wallet_mnemonics_to_seed(wl);

    printf("bitprim_native_wallet_mnemonics_to_seed - res: %p\n", res.hash);

    return Py_BuildValue("y#", res.hash, 64);    //TODO: warning, hardcoded hash size!
}

/*
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
}*/

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
    {"chain_fetch_stealth",  bitprim_native_chain_fetch_stealth, METH_VARARGS, "..."},
    {"chain_fetch_block_height",  bitprim_native_chain_fetch_block_height, METH_VARARGS, "..."},
    {"chain_fetch_block_header_by_height",  bitprim_native_chain_fetch_block_header_by_height, METH_VARARGS, "..."},
    {"chain_fetch_block_header_by_hash",  bitprim_native_chain_fetch_block_header_by_hash, METH_VARARGS, "..."},
    {"chain_fetch_block_by_height",  bitprim_native_chain_fetch_block_by_height, METH_VARARGS, "..."},
    {"chain_fetch_block_by_hash",  bitprim_native_chain_fetch_block_by_hash, METH_VARARGS, "..."},
    {"chain_fetch_merkle_block_by_height",  bitprim_native_chain_fetch_merkle_block_by_height, METH_VARARGS, "..."},
    {"chain_fetch_merkle_block_by_hash",  bitprim_native_chain_fetch_merkle_block_by_hash, METH_VARARGS, "..."},

    {"binary_construct",  bitprim_native_binary_construct, METH_VARARGS, "..."},
    {"binary_construct_string",  bitprim_native_binary_construct_string, METH_VARARGS, "..."},
    {"binary_construct_blocks",  bitprim_native_binary_construct_blocks, METH_VARARGS, "..."},
    {"binary_blocks",  bitprim_native_binary_blocks, METH_VARARGS, "..."},
    {"binary_encoded",  bitprim_native_binary_encoded, METH_VARARGS, "..."},

    {"merkle_block_get_header",  bitprim_native_chain_merkle_block_get_header, METH_VARARGS, "..."},
    {"merkle_block_is_valid",  bitprim_native_chain_merkle_block_is_valid, METH_VARARGS, "..."},
    {"merkle_block_hash_count",  bitprim_native_chain_merkle_block_hash_count, METH_VARARGS, "..."},
    {"merkle_block_serialized_size",  bitprim_native_chain_merkle_block_serialized_size, METH_VARARGS, "..."},
    {"merkle_block_total_transaction_count",  bitprim_native_chain_merkle_block_total_transaction_count, METH_VARARGS, "..."},
    {"merkle_block_reset",  bitprim_native_chain_merkle_block_reset, METH_VARARGS, "..."},

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

    //{"long_hash_t_to_str",  bitprim_native_long_hash_t_to_str, METH_VARARGS, "..."},
    //{"long_hash_t_free",  bitprim_native_long_hash_t_free, METH_VARARGS, "..."},

    {NULL, NULL, 0, NULL}        /* Sentinel */
};

struct module_state {
    PyObject *error;
};

#if PY_MAJOR_VERSION >= 3
#define GETSTATE(m) ((struct module_state*)PyModule_GetState(m))
#else //PY_MAJOR_VERSION >= 3
#define GETSTATE(m) (&_state)
static struct module_state _state;
#endif //PY_MAJOR_VERSION >= 3

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
