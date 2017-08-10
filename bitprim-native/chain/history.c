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

#include "history.h"
#include <bitprim/nodecint.h>
#include "../utils.h" //TODO(fernando): poner bien el dir del header

#ifdef __cplusplus
extern "C" {  
#endif  

// -------------------------------------------------------------------
// history_compact_list
// -------------------------------------------------------------------

PyObject* bitprim_native_history_compact_list_destruct(PyObject* self, PyObject* args) {
    PyObject* py_history_compact_list;

    if ( ! PyArg_ParseTuple(args, "O", &py_history_compact_list)) {
        return NULL;
    }

    history_compact_list_t list = (history_compact_list_t)get_ptr(py_history_compact_list);

    chain_history_compact_list_destruct(list);

    Py_RETURN_NONE;
}

PyObject* bitprim_native_history_compact_list_count(PyObject* self, PyObject* args) {
    PyObject* py_history_compact_list;

    if ( ! PyArg_ParseTuple(args, "O", &py_history_compact_list)) {
        return NULL;
    }

    history_compact_list_t list = (history_compact_list_t)get_ptr(py_history_compact_list);

    uint64_t /*size_t*/ res = chain_history_compact_list_count(list);

    return Py_BuildValue("K", res);
}

PyObject* bitprim_native_history_compact_list_nth(PyObject* self, PyObject* args) {
    PyObject* py_history_compact_list;
    uint64_t py_n;

    if ( ! PyArg_ParseTuple(args, "OK", &py_history_compact_list, &py_n)) {
        return NULL;
    }

    history_compact_list_t list = (history_compact_list_t)get_ptr(py_history_compact_list);

    history_compact_t hc = chain_history_compact_list_nth(list, py_n);

    PyObject* py_hc = to_py_obj(hc);
    return Py_BuildValue("O", py_hc);
}

// -------------------------------------------------------------------


// -------------------------------------------------------------------
// history_compact
// -------------------------------------------------------------------

PyObject* bitprim_native_history_compact_get_point_kind(PyObject* self, PyObject* args) {
    PyObject* py_history_compact;

    if ( ! PyArg_ParseTuple(args, "O", &py_history_compact)) {
        return NULL;
    }

    history_compact_t hist = (history_compact_t)get_ptr(py_history_compact);

    uint64_t res = chain_history_compact_get_point_kind(hist);

    return Py_BuildValue("K", res);
}

PyObject* bitprim_native_history_compact_get_point(PyObject* self, PyObject* args) {
    PyObject* py_history_compact;

    if ( ! PyArg_ParseTuple(args, "O", &py_history_compact)) {
        return NULL;
    }

    history_compact_t hist = (history_compact_t)get_ptr(py_history_compact);

    point_t p = chain_history_compact_get_point(hist);

    PyObject* py_p = to_py_obj(p);
    return Py_BuildValue("O", py_p);
}

PyObject* bitprim_native_history_compact_get_height(PyObject* self, PyObject* args) {
    PyObject* py_history_compact;

    if ( ! PyArg_ParseTuple(args, "O", &py_history_compact)) {
        return NULL;
    }

    history_compact_t hist = (history_compact_t)get_ptr(py_history_compact);

    uint64_t res = chain_history_compact_get_height(hist);

    return Py_BuildValue("K", res);
}

PyObject* bitprim_native_history_compact_get_value_or_previous_checksum(PyObject* self, PyObject* args) {
    PyObject* py_history_compact;

    if ( ! PyArg_ParseTuple(args, "O", &py_history_compact)) {
        return NULL;
    }

    history_compact_t hist = (history_compact_t)get_ptr(py_history_compact);

    uint64_t res = chain_history_compact_get_value_or_previous_checksum(hist);

    return Py_BuildValue("K", res);
}


#ifdef __cplusplus
} //extern "C"
#endif  
