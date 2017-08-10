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

#include "merkle_block.h"
#include <bitprim/nodecint.h>
#include "../utils.h" //TODO(fernando): poner bien el dir del header

#ifdef __cplusplus
extern "C" {  
#endif  


PyObject* bitprim_native_chain_merkle_block_get_header(PyObject* self, PyObject* args){
    PyObject* py_merkle;

    if ( ! PyArg_ParseTuple(args, "O", &py_merkle)) {
        return NULL;
    }

    merkle_block_t merkle_block = (merkle_block_t)get_ptr(py_merkle);
    header_t header = chain_merkle_block_header(merkle_block);

    return to_py_obj(header);//TODO: Está bien esto? O tiene que ser un BuildValue????

}

PyObject* bitprim_native_chain_merkle_block_is_valid(PyObject* self, PyObject* args){
    PyObject* py_merkle_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_merkle_block)) {
        return NULL;
    }

    merkle_block_t block = (merkle_block_t)get_ptr(py_merkle_block);
    int res = chain_merkle_block_is_valid(block);

    return Py_BuildValue("i", res);   
}

PyObject* bitprim_native_chain_merkle_block_hash_count(PyObject* self, PyObject* args){
    PyObject* py_merkle_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_merkle_block)) {
        return NULL;
    }

    merkle_block_t block = (merkle_block_t)get_ptr(py_merkle_block);
    uint64_t /*size_t*/ res = chain_merkle_block_hash_count(block);

    return Py_BuildValue("K", res);   
}


PyObject* bitprim_native_chain_merkle_block_total_transaction_count(PyObject* self, PyObject* args){
    PyObject* py_merkle_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_merkle_block)) {
        return NULL;
    }

    merkle_block_t block = (merkle_block_t)get_ptr(py_merkle_block);
    uint64_t /*size_t*/ res = chain_merkle_block_total_transaction_count(block);

    return Py_BuildValue("K", res);   
}

PyObject* bitprim_native_chain_merkle_block_serialized_size(PyObject* self, PyObject* args){
    PyObject* py_merkle_block;
    uint32_t py_version;

    if ( ! PyArg_ParseTuple(args, "OI", &py_merkle_block, &py_version)) {
        return NULL;
    }

    merkle_block_t block = (merkle_block_t)get_ptr(py_merkle_block);
    uint64_t /*size_t*/ res = chain_merkle_block_serialized_size(block, py_version);

    return Py_BuildValue("K", res);   
}

PyObject* bitprim_native_chain_merkle_block_reset(PyObject* self, PyObject* args){
    PyObject* py_merkle_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_merkle_block)) {
        return NULL;
    }

    merkle_block_t block = (merkle_block_t)get_ptr(py_merkle_block);
    chain_merkle_block_reset(block);

    Py_RETURN_NONE;   
}

PyObject * bitprim_native_chain_merkle_block_destruct(PyObject* self, PyObject* args){
    PyObject* py_merkle_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_merkle_block)) {
        return NULL;
    }

    merkle_block_t block = (merkle_block_t)get_ptr(py_merkle_block);
    chain_merkle_block_destruct(block);

    Py_RETURN_NONE;   
}


#ifdef __cplusplus
} //extern "C"
#endif  
