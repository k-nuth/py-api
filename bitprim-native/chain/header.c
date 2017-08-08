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


#include "chain.h"
#include <bitprim/nodecint.h>
#include "../utils.h" //TODO(fernando): poner bien el dir del header

// -------------------------------------------------------------------
// header
// -------------------------------------------------------------------


PyObject* bitprim_native_chain_header_get_version(PyObject* self, PyObject* args){
    PyObject* py_header;

    if ( ! PyArg_ParseTuple(args, "O", &py_header)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    uint32_t res = chain_header_version(header);

    return Py_BuildValue("I", res);   
}

PyObject* bitprim_native_chain_header_set_version(PyObject* self, PyObject* args){
    PyObject* py_header;
    uint32_t py_version;

    if ( ! PyArg_ParseTuple(args, "OI", &py_header, &py_version)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    chain_header_set_version(header, py_version);

    Py_RETURN_NONE;   
}

PyObject* bitprim_native_chain_header_get_previous_block_hash(PyObject* self, PyObject* args){
    PyObject* py_header;

    if ( ! PyArg_ParseTuple(args, "O", &py_header)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    hash_t res = chain_header_previous_block_hash(header);

#if PY_MAJOR_VERSION >= 3
    return Py_BuildValue("y#", res.hash, 32);    //TODO: warning, hardcoded hash size!
#else
    return Py_BuildValue("s#", res.hash, 32);    //TODO: warning, hardcoded hash size!
#endif

}



/*
PyObject* bitprim_native_chain_header_set_previous_block_hash(PyObject* self, PyObject* args){
    PyObject* py_header;
    Py_ssize_t py_hash;

    if ( ! PyArg_ParseTuple(args, "OO", &py_header, &py_hash)) {
        return NULL;
    }

    char* s = PyString_AsString(py_hash);
    uint8_t * hash = (uint8_t*) malloc (sizeof(uint8_t[32]));
    hex2bin(s,&hash[31]);

    header_t header = (header_t)get_ptr(py_header);
    header_set_previous_block_hash(header, hash);

    Py_RETURN_NONE;   
}

PyObject* bitprim_native_chain_header_set_merkle(PyObject* self, PyObject* args){
    PyObject* py_header;
    Py_ssize_t py_merkle;

    if ( ! PyArg_ParseTuple(args, "OO", &py_header, &py_merkle)) {
        return NULL;
    }

    char* s = PyString_AsString(py_merkle);
    uint8_t * hash = (uint8_t*) malloc (sizeof(uint8_t[32]));
    hex2bin(s,&hash[31]);

    header_t header = (header_t)get_ptr(py_header);
    header_set_merkle(header, hash);

    Py_RETURN_NONE;   
}

*/
PyObject* bitprim_native_chain_header_get_merkle(PyObject* self, PyObject* args){
    PyObject* py_header;

    if ( ! PyArg_ParseTuple(args, "O", &py_header)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    hash_t res = chain_header_merkle(header);

#if PY_MAJOR_VERSION >= 3
    return Py_BuildValue("y#", res.hash, 32);    //TODO: warning, hardcoded hash size!
#else
    return Py_BuildValue("s#", res.hash, 32);    //TODO: warning, hardcoded hash size!
#endif

}

PyObject* bitprim_native_chain_header_get_timestamp(PyObject* self, PyObject* args){
    PyObject* py_header;

    if ( ! PyArg_ParseTuple(args, "O", &py_header)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    uint32_t res = chain_header_timestamp(header);

    return Py_BuildValue("I", res);   
}

PyObject* bitprim_native_chain_header_set_timestamp(PyObject* self, PyObject* args){
    PyObject* py_header;
    uint32_t py_timestamp;

    if ( ! PyArg_ParseTuple(args, "OI", &py_header, &py_timestamp)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    chain_header_set_timestamp(header, py_timestamp);

    Py_RETURN_NONE;   
}


PyObject* bitprim_native_chain_header_get_bits(PyObject* self, PyObject* args){
    PyObject* py_header;

    if ( ! PyArg_ParseTuple(args, "O", &py_header)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    uint32_t res = chain_header_bits(header);

    return Py_BuildValue("I", res);   
}

PyObject* bitprim_native_chain_header_set_bits(PyObject* self, PyObject* args){
    PyObject* py_header;
    uint32_t py_bits;

    if ( ! PyArg_ParseTuple(args, "OI", &py_header, &py_bits)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    chain_header_set_bits(header, py_bits);

    Py_RETURN_NONE;   
}

PyObject* bitprim_native_chain_header_get_nonce(PyObject* self, PyObject* args){
    PyObject* py_header;

    if ( ! PyArg_ParseTuple(args, "O", &py_header)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    uint32_t res = chain_header_nonce(header);

    return Py_BuildValue("I", res);  
}

PyObject* bitprim_native_chain_header_set_nonce(PyObject* self, PyObject* args){
    PyObject* py_header;
    uint32_t py_nonce;

    if ( ! PyArg_ParseTuple(args, "OI", &py_header, &py_nonce)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    chain_header_set_nonce(header, py_nonce);

    Py_RETURN_NONE;   
}


PyObject * bitprim_native_chain_header_destruct(PyObject* self, PyObject* args){
    PyObject* py_header;

    if ( ! PyArg_ParseTuple(args, "O", &py_header)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    chain_header_destruct(header);

    Py_RETURN_NONE;
}

