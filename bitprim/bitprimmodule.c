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

// static
// PyObject* bitprim_native_executor_construct(PyObject* self, PyObject* args) {
//     char const* path;
//     PyObject* py_in;
//     PyObject* py_out;
//     PyObject* py_err;

//     if ( ! PyArg_ParseTuple(args, "sOOO", &path, &py_in, &py_out, &py_err))
//         return NULL;

//     FILE* sin = PyFile_AsFile(py_in);
//     FILE* sout = PyFile_AsFile(py_out);
//     FILE* serr = PyFile_AsFile(py_err);

// //    PyFile_IncUseCount(p);
// ///* ... */
// //    Py_BEGIN_ALLOW_THREADS
// //        do_something(fp);
// //    Py_END_ALLOW_THREADS
// ///* ... */
// //        PyFile_DecUseCount(p);



//     executor_t exec = executor_construct(path, sin, sout, serr);

//     // return PyCObject_FromVoidPtr(exec, NULL);
//     return PyCapsule_New(exec, NULL, NULL);
// }

static
PyObject* bitprim_native_executor_construct(PyObject* self, PyObject* args) {
    char const* path;
    PyObject* py_in;
    PyObject* py_out;
    PyObject* py_err;

    if ( ! PyArg_ParseTuple(args, "sOOO", &path, &py_in, &py_out, &py_err))
        return NULL;



#if PY_MAJOR_VERSION >= 3

    int sin_fd = PyObject_AsFileDescriptor(py_in);
    int sout_fd = PyObject_AsFileDescriptor(py_out);
    int serr_fd = PyObject_AsFileDescriptor(py_err);

    executor_t exec = executor_construct_fd(path, sin_fd, sout_fd, serr_fd);

    return PyCapsule_New(exec, NULL, NULL);

#else /* PY_MAJOR_VERSION >= 3 */
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

#endif /* PY_MAJOR_VERSION >= 3 */

}


// ---------------------------------------------------------


static
PyObject* bitprim_native_executor_destruct(PyObject* self, PyObject* args) {
    PyObject* py_exec;

    if ( ! PyArg_ParseTuple(args, "O", &py_exec))
        return NULL;

    // executor_t exec = (executor_t)PyCObject_AsVoidPtr(py_exec);
    executor_t exec = (executor_t)PyCapsule_GetPointer(py_exec, NULL);

    executor_destruct(exec);
    Py_RETURN_NONE;
}

// ---------------------------------------------------------

static
PyObject* bitprim_native_executor_initchain(PyObject* self, PyObject* args) {
    PyObject* py_exec;

    if ( ! PyArg_ParseTuple(args, "O", &py_exec))
        return NULL;

    // executor_t exec = (executor_t)PyCObject_AsVoidPtr(py_exec);
    executor_t exec = (executor_t)PyCapsule_GetPointer(py_exec, NULL);
    int res = executor_initchain(exec);
    return Py_BuildValue("i", res);
}

// ---------------------------------------------------------

static
PyObject* bitprim_native_executor_run(PyObject* self, PyObject* args) {
    PyObject* py_exec;

    if ( ! PyArg_ParseTuple(args, "O", &py_exec))
        return NULL;

    // executor_t exec = (executor_t)PyCObject_AsVoidPtr(py_exec);
    executor_t exec = (executor_t)PyCapsule_GetPointer(py_exec, NULL);

    int res = executor_run(exec);
    return Py_BuildValue("i", res);
}

// ---------------------------------------------------------

static
PyObject* bitprim_native_executor_stop(PyObject* self, PyObject* args) {
    PyObject* py_exec;

    if ( ! PyArg_ParseTuple(args, "O", &py_exec))
        return NULL;

    // executor_t exec = (executor_t)PyCObject_AsVoidPtr(py_exec);
    executor_t exec = (executor_t)PyCapsule_GetPointer(py_exec, NULL);

    executor_stop(exec);
    Py_RETURN_NONE;
}

// ---------------------------------------------------------

// // BITPRIM_EXPORT
// // void fetch_last_height(executor_t exec, last_height_fetch_handler_t handler);


static PyObject* global_callback = NULL;

void last_height_fetch_handler(int error, size_t h) {
    // printf("C callback (last_height_fetch_handler) called\n");
    // printf("Calling Python callback\n");

    PyObject* arglist = Py_BuildValue("(ii)", error, h);
    PyObject* result = PyObject_CallObject(global_callback, arglist);
    Py_DECREF(arglist);    
}

// static 
// PyObject* my_set_callback(PyObject *self, PyObject *args) {
//     PyObject *result = NULL;
//     PyObject *temp;

//     if (PyArg_ParseTuple(args, "O:set_callback", &temp)) {
//         if (!PyCallable_Check(temp)) {
//             PyErr_SetString(PyExc_TypeError, "parameter must be callable");
//             return NULL;
//         }
//         Py_XINCREF(temp);         /* Add a reference to new callback */
//         Py_XDECREF(global_callback);  /* Dispose of previous callback */
//         global_callback = temp;       /* Remember new callback */
//         /* Boilerplate to return "None" */
//         Py_INCREF(Py_None);
//         result = Py_None;
//     }
//     return result;
// }

// static 
// PyObject* my_call_callback(PyObject *self, PyObject *args) {
//     int arg;
//     PyObject *arglist;
//     PyObject *result;

//     arg = 123;

//     arglist = Py_BuildValue("(i)", arg);
//     result = PyObject_CallObject(global_callback, arglist);
//     Py_DECREF(arglist);

//     Py_RETURN_NONE; 
// }



static
PyObject* bitprim_native_fetch_last_height(PyObject* self, PyObject* args) {
    PyObject* py_exec;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OO:set_callback", &py_exec, &py_callback)) {
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    // executor_t exec = (executor_t)PyCObject_AsVoidPtr(py_exec);
    executor_t exec = (executor_t)PyCapsule_GetPointer(py_exec, NULL);

    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    Py_XDECREF(global_callback);  /* Dispose of previous callback */
    global_callback = py_callback;       /* Remember new callback */

    // last_height_fetch_handler_t callback = (last_height_fetch_handler_t)PyCObject_AsVoidPtr(global_callback);
    // fetch_last_height(exec, callback);
    // fetch_last_height(exec, global_callback);

    // printf("Setting the global callback\n");

    fetch_last_height(exec, last_height_fetch_handler);

    // printf("fetch_last_height called\n");


    Py_RETURN_NONE;
}

// ---------------------------------------------------------

static
PyMethodDef BitprimNativeMethods[] = {

    {"construct",  bitprim_native_executor_construct, METH_VARARGS, "Construct the executor object."},
    {"destruct",  bitprim_native_executor_destruct, METH_VARARGS, "Destruct the executor object."},
    {"initchain",  bitprim_native_executor_initchain, METH_VARARGS, "Directory Initialization."},
    {"run",  bitprim_native_executor_run, METH_VARARGS, "Node run."},
    {"stop",  bitprim_native_executor_stop, METH_VARARGS, "Node stop."},

    {"fetch_last_height",  bitprim_native_fetch_last_height, METH_VARARGS, "..."},

    // {"my_set_callback", my_set_callback, METH_VARARGS, "..."},
    // {"my_call_callback", my_call_callback, METH_VARARGS, "..."},


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



