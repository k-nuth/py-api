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

#include "block.h"

static
PyObject * bitprim_native_chain_block_get_header(PyObject* self, PyObject* args){
    PyObject* py_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    header_t header = chain_block_header(block);

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

    return Py_BuildValue("y#", res.hash, 32); //TODO: ojo con y# en Python2
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
}

