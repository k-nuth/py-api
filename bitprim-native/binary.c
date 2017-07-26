#include "binary.h"

// -------------------------------------------------------------------
// binary
// -------------------------------------------------------------------

PyObject * bitprim_native_binary_construct(PyObject* self, PyObject* args){

    binary_t binary = binary_construct();

#if PY_MAJOR_VERSION >= 3
    return PyCapsule_New(binary, NULL, NULL);
#else /* PY_MAJOR_VERSION >= 3 */
    return PyCObject_FromVoidPtr(binary, NULL);
#endif /* PY_MAJOR_VERSION >= 3 */
}

PyObject * bitprim_native_binary_construct_string(PyObject* self, PyObject* args){

    char const* filter;

    if ( ! PyArg_ParseTuple(args, "s", &filter)) {
        printf("bitprim_native_binary_construct_string - 2\n");
        return NULL;
    }

    binary_t binary = binary_construct_string(filter);

#if PY_MAJOR_VERSION >= 3
    return PyCapsule_New(binary, NULL, NULL);
#else /* PY_MAJOR_VERSION >= 3 */
    return PyCObject_FromVoidPtr(binary, NULL);
#endif /* PY_MAJOR_VERSION >= 3 */
}

PyObject * bitprim_native_binary_construct_blocks(PyObject* self, PyObject* args){

    Py_ssize_t bits_size;
    Py_ssize_t lenght;
    PyObject* blocks;

    if ( ! PyArg_ParseTuple(args, "nnO", &bits_size, &lenght, &blocks)) {
        return NULL;
    }
    
    if(PySequence_Check(blocks)) { //Check if its an array
        int size = PySequence_Size(blocks); //get array size
        uint8_t *result = malloc(sizeof(uint8_t) * size); // reserve memory
        for(int i = 0; i < size; i++) {
            PyObject* item = PySequence_GetItem(blocks, i); //read every item in the array
            if(PyInt_Check(item)) { //check if the item its an integer
               result[i] = PyInt_AsLong(item); //extract the value of the pyobject as int
            } else {
               return NULL;
            }  
        }
   
//    for(int i=0; i < 4 ; i++)
//      printf("block construct %u \n", result[i]);


    auto binary = binary_construct_blocks(bits_size, result, size);
#if PY_MAJOR_VERSION >= 3
    return PyCapsule_New(binary, NULL, NULL);
#else // PY_MAJOR_VERSION >= 3 
    return PyCObject_FromVoidPtr(binary, NULL);
#endif //PY_MAJOR_VERSION >= 3 
    }

    return NULL;

}

PyObject * bitprim_native_binary_blocks(PyObject* self, PyObject* args){

    PyObject* binary;
    if ( ! PyArg_ParseTuple(args, "O", &binary)) {
        return NULL;
    }
    
    binary_t binary_pointer = (binary_t)get_ptr(binary);
    uint8_t* blocks = (uint8_t*)binary_blocks(binary_pointer);
//    for(int i=0; i < 4 ; i++)
//      printf("block %u \n", blocks[i]);
    

#if PY_MAJOR_VERSION >= 3
    return PyCapsule_New(blocks, NULL, NULL);
#else 
    return PyCObject_FromVoidPtr(blocks, NULL);
#endif

}


PyObject * bitprim_native_binary_encoded(PyObject* self, PyObject* args){

    PyObject* binary;
    if ( ! PyArg_ParseTuple(args, "O", &binary)) {
        printf("bitprim_native_binary_encoded - 2\n");
        return NULL;
    }
    
    binary_t binary_pointer = (binary_t)get_ptr(binary);
    char* str = (char*)binary_encoded(binary_pointer);

    return PyString_FromString(str);
}

