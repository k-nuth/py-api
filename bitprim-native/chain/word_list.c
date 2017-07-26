#import "word_list.h"
// word_list_t word_list_construct() {
// void point_list_destruct(word_list_t word_list) {
// void word_list_add_word(word_list_t word_list, char const* word) {


PyObject* bitprim_native_word_list_construct(PyObject* self, PyObject* args) {
    word_list_t wl = word_list_construct();

// #if PY_MAJOR_VERSION >= 3
//     return PyCapsule_New(wl, NULL, NULL);
// #else /* PY_MAJOR_VERSION >= 3 */
//     return PyCObject_FromVoidPtr(wl, NULL);
// #endif /* PY_MAJOR_VERSION >= 3 */
    return to_py_obj(wl);

}

PyObject* bitprim_native_word_list_destruct(PyObject* self, PyObject* args) {
    PyObject* py_wl;

    if ( ! PyArg_ParseTuple(args, "O", &py_wl))
        return NULL;

    // word_list_t wl = (word_list_t)PyCObject_AsVoidPtr(py_wl);
    word_list_t wl = (word_list_t)PyCapsule_GetPointer(py_wl, NULL);

    word_list_destruct(wl);
    Py_RETURN_NONE;
}

PyObject* bitprim_native_word_list_add_word(PyObject* self, PyObject* args) {
    PyObject* py_wl;
    char const* word;

    if ( ! PyArg_ParseTuple(args, "Os", &py_wl, &word))
        return NULL;

    // word_list_t wl = (word_list_t)PyCObject_AsVoidPtr(py_wl);
    word_list_t wl = (word_list_t)PyCapsule_GetPointer(py_wl, NULL);

    word_list_add_word(wl, word);
    Py_RETURN_NONE;
}


