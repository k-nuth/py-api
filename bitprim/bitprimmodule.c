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

#include <bitprim/nodecint/executor_c.h>

// ---------------------------------------------------------

static
PyObject* bitprim_native_executor_construct(PyObject* self, PyObject* args) {
    char const* path;
    PyObject* py_in;
    PyObject* py_out;
    PyObject* py_err;

    if ( ! PyArg_ParseTuple(args, "sOOO", &path, &py_in, &py_out, &py_err))
        return NULL;

    FILE* sin = PyFile_AsFile(py_in);
    FILE* sout = PyFile_AsFile(py_out);
    FILE* serr = PyFile_AsFile(py_err);

//    PyFile_IncUseCount(p);
///* ... */
//    Py_BEGIN_ALLOW_THREADS
//        do_something(fp);
//    Py_END_ALLOW_THREADS
///* ... */
//        PyFile_DecUseCount(p);



    executor_t exec = executor_construct(path, sin, sout, serr);

    return PyCObject_FromVoidPtr(exec, NULL);
}

// ---------------------------------------------------------


static
PyObject* bitprim_native_executor_destruct(PyObject* self, PyObject* args) {
    PyObject* py_exec;

    if ( ! PyArg_ParseTuple(args, "O", &py_exec))
        return NULL;

    executor_t exec = (executor_t)PyCObject_AsVoidPtr(py_exec);
    executor_destruct(exec);
    return Py_BuildValue("");
}

// ---------------------------------------------------------

static
PyObject* bitprim_native_executor_initchain(PyObject* self, PyObject* args) {
    PyObject* py_exec;

    if ( ! PyArg_ParseTuple(args, "O", &py_exec))
        return NULL;

    executor_t exec = (executor_t)PyCObject_AsVoidPtr(py_exec);
    int res = executor_initchain(exec);
    return Py_BuildValue("i", res);
}

// ---------------------------------------------------------

static
PyObject* bitprim_native_executor_run(PyObject* self, PyObject* args) {
    PyObject* py_exec;

    if ( ! PyArg_ParseTuple(args, "O", &py_exec))
        return NULL;

    executor_t exec = (executor_t)PyCObject_AsVoidPtr(py_exec);
    int res = executor_run(exec);
    return Py_BuildValue("i", res);
}

// ---------------------------------------------------------

// // BITPRIM_EXPORT
// // void fetch_last_height(executor_t exec, last_height_fetch_handler_t handler);

// static
// PyObject* bitprim_native_fetch_last_height(PyObject* self, PyObject* args) {
//     PyObject* py_exec;
//     PyObject* py_callback;

//     if ( ! PyArg_ParseTuple(args, "OO", &py_exec, &py_callback)) {
//         return NULL;
//     }

//     executor_t exec = (executor_t)PyCObject_AsVoidPtr(py_exec);
//     last_height_fetch_handler_t callback = (last_height_fetch_handler_t)PyCObject_AsVoidPtr(py_callback);

//     fetch_last_height(exec, callback);
//     return Py_BuildValue("i", res);
// }

// ---------------------------------------------------------

static
PyMethodDef BitprimNativeMethods[] = {

    {"construct",  bitprim_native_executor_construct, METH_VARARGS, "Construct the executor object."},
    {"destruct",  bitprim_native_executor_destruct, METH_VARARGS, "Destruct the executor object."},
    {"initchain",  bitprim_native_executor_initchain, METH_VARARGS, "Directory Initialization."},
    {"run",  bitprim_native_executor_run, METH_VARARGS, "Directory Initialization."},

    {"fetch_last_height",  bitprim_native_fetch_last_height, METH_VARARGS, "..."},


    {NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC
initbitprim_native(void) {
    (void) Py_InitModule("bitprim_native", BitprimNativeMethods);
}