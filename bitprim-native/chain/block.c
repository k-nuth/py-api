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
#include <bitprim/nodecint.h>
#include "../utils.h" //TODO(fernando): poner bien el dir del header

#ifdef __cplusplus
extern "C" {  
#endif  

PyObject* bitprim_native_chain_block_get_header(PyObject* self, PyObject* args){
    PyObject* py_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    header_t header = chain_block_header(block);

    return to_py_obj(header);
}


PyObject* bitprim_native_chain_block_transaction_count(PyObject* self, PyObject* args){
    PyObject* py_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    uint64_t /*size_t*/ res = chain_block_transaction_count(block);

    return Py_BuildValue("K", res);   
}

PyObject* bitprim_native_chain_block_serialized_size(PyObject* self, PyObject* args){
    PyObject* py_block;
    uint32_t py_version;

    if ( ! PyArg_ParseTuple(args, "OI", &py_block, &py_version)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    uint64_t /*size_t*/ res = chain_block_serialized_size(block, py_version);

    return Py_BuildValue("K", res);   
}

PyObject* bitprim_native_chain_block_subsidy(PyObject* self, PyObject* args){
    uint64_t /*size_t*/ py_height;

    if ( ! PyArg_ParseTuple(args, "K", &py_height)) {
        return NULL;
    }

    uint64_t res = chain_block_subsidy(py_height);
    return Py_BuildValue("K", res);
}

PyObject* bitprim_native_chain_block_fees(PyObject* self, PyObject* args){
    PyObject* py_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    uint64_t res = chain_block_fees(block);

    return Py_BuildValue("K", res);   
}

PyObject* bitprim_native_chain_block_claim(PyObject* self, PyObject* args){
    PyObject* py_block;


    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    uint64_t res = chain_block_claim(block);

    return Py_BuildValue("K", res);   
}

PyObject* bitprim_native_chain_block_reward(PyObject* self, PyObject* args){
    PyObject* py_block;
    uint64_t py_height;

    if ( ! PyArg_ParseTuple(args, "OK", &py_block, &py_height)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    uint64_t res = chain_block_reward(block, py_height);

    return Py_BuildValue("K", res);   
}

PyObject* bitprim_native_chain_block_generate_merkle_root(PyObject* self, PyObject* args){
    PyObject* py_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    hash_t res = chain_block_generate_merkle_root(block);

#if PY_MAJOR_VERSION >= 3
    return Py_BuildValue("y#", res.hash, 32);    //TODO: warning, hardcoded hash size!
#else
    return Py_BuildValue("s#", res.hash, 32);    //TODO: warning, hardcoded hash size!
#endif
}

PyObject* bitprim_native_chain_block_hash(PyObject* self, PyObject* args){
    PyObject* py_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    hash_t res = chain_block_hash(block);

#if PY_MAJOR_VERSION >= 3
    return Py_BuildValue("y#", res.hash, 32);    //TODO: warning, hardcoded hash size!
#else
    return Py_BuildValue("s#", res.hash, 32);    //TODO: warning, hardcoded hash size!
#endif
}


PyObject * bitprim_native_chain_block_is_valid(PyObject* self, PyObject* args){
    PyObject* py_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    int res = chain_block_is_valid(block);

    return Py_BuildValue("i", res);   
}


//transaction_t chain_block_transaction_nth(block_t block, uint64_t n);
PyObject * bitprim_native_chain_block_transaction_nth(PyObject* self, PyObject* args){
    PyObject* py_block;
    uint64_t py_n;

    if ( ! PyArg_ParseTuple(args, "OK", &py_block, &py_n)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    transaction_t res = chain_block_transaction_nth(block, py_n);

    return to_py_obj(res);   
}

PyObject * bitprim_native_chain_block_signature_operations(PyObject* self, PyObject* args){
    PyObject* py_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    uint64_t res = chain_block_signature_operations(block);

    return Py_BuildValue("K", res);   
}

PyObject * bitprim_native_chain_block_signature_operations_bip16_active(PyObject* self, PyObject* args){
    PyObject* py_block;
    int py_bip16_active;

    if ( ! PyArg_ParseTuple(args, "Oi", &py_block, &py_bip16_active)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    uint64_t res = chain_block_signature_operations_bip16_active(block, py_bip16_active);

    return Py_BuildValue("K", res);
}

PyObject * bitprim_native_chain_block_total_inputs(PyObject* self, PyObject* args){
    PyObject* py_block;
    int py_with_coinbase;

    if ( ! PyArg_ParseTuple(args, "Oi", &py_block, &py_with_coinbase)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    uint64_t res = chain_block_total_inputs(block, py_with_coinbase);

    return Py_BuildValue("K", res);
}

PyObject * bitprim_native_chain_block_is_extra_coinbases(PyObject* self, PyObject* args){
    PyObject* py_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    int res = chain_block_is_extra_coinbases(block);

    return Py_BuildValue("i", res); 
}

PyObject * bitprim_native_chain_block_is_final(PyObject* self, PyObject* args){
    PyObject* py_block;
    uint64_t py_height;

    if ( ! PyArg_ParseTuple(args, "OK", &py_block, &py_height)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    int res = chain_block_is_final(block, py_height);

    return Py_BuildValue("i", res); 
}

PyObject * bitprim_native_chain_block_is_distinct_transaction_set(PyObject* self, PyObject* args){
    PyObject* py_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    int res = chain_block_is_distinct_transaction_set(block);

    return Py_BuildValue("i", res); 
}

PyObject * bitprim_native_chain_block_is_valid_coinbase_claim(PyObject* self, PyObject* args){
    PyObject* py_block;
    uint64_t py_height;

    if ( ! PyArg_ParseTuple(args, "OK", &py_block, &py_height)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    int res = chain_block_is_valid_coinbase_claim(block, py_height);

    return Py_BuildValue("i", res); 
}
PyObject * bitprim_native_chain_block_is_valid_coinbase_script(PyObject* self, PyObject* args){
    PyObject* py_block;
    uint64_t py_height;

    if ( ! PyArg_ParseTuple(args, "OK", &py_block, &py_height)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    int res = chain_block_is_valid_coinbase_script(block, py_height);

    return Py_BuildValue("i", res); 
}

PyObject * bitprim_native_chain_block_is_internal_double_spend(PyObject* self, PyObject* args){
    PyObject* py_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    int res = chain_block_is_internal_double_spend(block);

    return Py_BuildValue("i", res); 
}

PyObject * bitprim_native_chain_block_is_valid_merkle_root(PyObject* self, PyObject* args){
    PyObject* py_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    int res = chain_block_is_valid_merkle_root(block);

    return Py_BuildValue("i", res);
}


PyObject * bitprim_native_chain_block_destruct(PyObject* self, PyObject* args){
    PyObject* py_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_block)) {
        return NULL;
    }

    block_t block = (block_t)get_ptr(py_block);
    chain_block_destruct(block);

    Py_RETURN_NONE;
}

#ifdef __cplusplus
} //extern "C" 
#endif  
