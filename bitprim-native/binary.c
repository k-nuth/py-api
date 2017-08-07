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

#include "binary.h"
#include <bitprim/nodecint.h>
#include "utils.h" //TODO(fernando): poner bien el dir del header

// -------------------------------------------------------------------
// binary
// -------------------------------------------------------------------

PyObject* bitprim_native_binary_construct(PyObject* self, PyObject* args){
    binary_t binary = binary_construct();
    return to_py_obj(binary);
}

PyObject* bitprim_native_binary_construct_string(PyObject* self, PyObject* args){

    char const* filter;

    if ( ! PyArg_ParseTuple(args, "s", &filter)) {
        printf("bitprim_native_binary_construct_string - 2\n");
        return NULL;
    }

    binary_t binary = binary_construct_string(filter);
    return to_py_obj(binary);
}

PyObject* bitprim_native_binary_construct_blocks(PyObject* self, PyObject* args){

    Py_ssize_t bits_size;
    Py_ssize_t lenght;
    PyObject* blocks;

    if ( ! PyArg_ParseTuple(args, "nnO", &bits_size, &lenght, &blocks)) {
        return NULL;
    }
    
    if (PySequence_Check(blocks)) { //Check if its an array
        size_t size = PySequence_Size(blocks); //get array size
        uint8_t* result = malloc(sizeof(uint8_t) * size); // reserve memory
        
        for (int i = 0; i < size; ++i) {
            PyObject* item = PySequence_GetItem(blocks, i); //read every item in the array
            if (PyInt_Check(item)) { //check if the item its an integer
               result[i] = PyInt_AsLong(item); //extract the value of the pyobject as int
            } else {
               return NULL;
            }  
        }
   
        binary_t binary = binary_construct_blocks(bits_size, result, size);
        return to_py_obj(binary);
    }

    return NULL;
}

PyObject* bitprim_native_binary_blocks(PyObject* self, PyObject* args){

    PyObject* binary;
    if ( ! PyArg_ParseTuple(args, "O", &binary)) {
        return NULL;
    }
    
    binary_t binary_pointer = (binary_t)get_ptr(binary);
    uint64_t /*size_t*/ out_n;
    uint8_t* blocks = (uint8_t*)binary_blocks(binary_pointer, &out_n); //TODO(bitprim): acá falta un parámetro
    return to_py_obj(blocks);
}

PyObject* bitprim_native_binary_encoded(PyObject* self, PyObject* args){

    PyObject* binary;
    if ( ! PyArg_ParseTuple(args, "O", &binary)) {
        printf("bitprim_native_binary_encoded - 2\n");
        return NULL;
    }
    
    binary_t binary_pointer = (binary_t)get_ptr(binary);
    char* str = (char*)binary_encoded(binary_pointer);

    return PyString_FromString(str);
}
