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

#include "word_list.h"
#include <bitprim/nodecint.h>
#include "../utils.h" //TODO(fernando): poner bien el dir del header

#ifdef __cplusplus
extern "C" {  
#endif  

// word_list_t word_list_construct() {
// void point_list_destruct(word_list_t word_list) {
// void word_list_add_word(word_list_t word_list, char const* word) {

PyObject* bitprim_native_word_list_construct(PyObject* self, PyObject* args) {
    word_list_t wl = word_list_construct();

    return to_py_obj(wl);

}

PyObject* bitprim_native_word_list_destruct(PyObject* self, PyObject* args) {
    PyObject* py_wl;

    if ( ! PyArg_ParseTuple(args, "O", &py_wl))
        return NULL;

    word_list_t wl = (word_list_t)get_ptr(py_wl);

    word_list_destruct(wl);
    Py_RETURN_NONE;
}

PyObject* bitprim_native_word_list_add_word(PyObject* self, PyObject* args) {
    PyObject* py_wl;
    char const* word;

    if ( ! PyArg_ParseTuple(args, "Os", &py_wl, &word))
        return NULL;

    word_list_t wl = (word_list_t)get_ptr(py_wl);

    word_list_add_word(wl, word);
    Py_RETURN_NONE;
}


#ifdef __cplusplus
} //extern "C" 
#endif  
