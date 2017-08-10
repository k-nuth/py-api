#ifndef BITPRIM_PY_CHAIN_HISTORY_H_
#define BITPRIM_PY_CHAIN_HISTORY_H_

#include <Python.h>

#ifdef __cplusplus
extern "C" {  
#endif  

PyObject* bitprim_native_history_compact_list_destruct(PyObject* self, PyObject* args);
PyObject* bitprim_native_history_compact_list_count(PyObject* self, PyObject* args);
PyObject* bitprim_native_history_compact_list_nth(PyObject* self, PyObject* args);
PyObject* bitprim_native_history_compact_get_point_kind(PyObject* self, PyObject* args);
PyObject* bitprim_native_history_compact_get_point(PyObject* self, PyObject* args);
PyObject* bitprim_native_history_compact_get_height(PyObject* self, PyObject* args);
PyObject* bitprim_native_history_compact_get_value_or_previous_checksum(PyObject* self, PyObject* args);

#ifdef __cplusplus
} //extern "C" {  
#endif  

#endif
