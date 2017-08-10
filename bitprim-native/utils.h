#ifndef BITPRIM_PY_UTILS_H_
#define BITPRIM_PY_UTILS_H_


#include <Python.h>
#include <bitprim/nodecint.h>

#ifdef __cplusplus
extern "C" {  
#endif  

void* get_ptr(PyObject* obj);
executor_t cast_executor(PyObject* obj);
int char2int(char input);
void hex2bin(const char* src, uint8_t* target);
PyObject* to_py_obj(void*);

#ifdef __cplusplus
} //extern "C"
#endif  

#endif
