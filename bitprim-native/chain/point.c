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

#include "point.h"
#include <bitprim/nodecint.h>
#include "../utils.h" //TODO(fernando): poner bien el dir del header

// -------------------------------------------------------------------
// point
// -------------------------------------------------------------------

// hash_t point_get_hash(point_t point){
// int /*bool*/ point_is_valid(point_t point){
// uint32_t point_get_index(point_t point){
// uint64_t point_get_checksum(point_t point){

PyObject* bitprim_native_point_get_hash(PyObject* self, PyObject* args) {
    PyObject* py_point;

    if ( ! PyArg_ParseTuple(args, "O", &py_point)) {
        return NULL;
    }

    point_t p = (point_t)get_ptr(py_point);

    hash_t res = chain_point_get_hash(p);

    return Py_BuildValue("y#", res.hash, 32);    //TODO: warning, hardcoded hash size!
}

PyObject* bitprim_native_point_is_valid(PyObject* self, PyObject* args) {
    PyObject* py_point;

    if ( ! PyArg_ParseTuple(args, "O", &py_point)) {
        // printf("bitprim_native_point_is_valid - 2\n");
        return NULL;
    }

    point_t p = (point_t)get_ptr(py_point);

    int res = chain_point_is_valid(p);

    if (res == 0) {
        Py_RETURN_FALSE;
    }

    Py_RETURN_TRUE;
}

PyObject* bitprim_native_point_get_index(PyObject* self, PyObject* args) {
    PyObject* py_point;

    if ( ! PyArg_ParseTuple(args, "O", &py_point)) {
        return NULL;
    }

    point_t p = (point_t)get_ptr(py_point);

    uint32_t res = chain_point_get_index(p);
    return Py_BuildValue("K", res);
}

PyObject* bitprim_native_point_get_checksum(PyObject* self, PyObject* args) {
    PyObject* py_point;

    if ( ! PyArg_ParseTuple(args, "O", &py_point)) {
        return NULL;
    }

    point_t p = (point_t)get_ptr(py_point);

    uint64_t res = chain_point_get_checksum(p);

    return Py_BuildValue("K", res);
}

