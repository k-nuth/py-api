#include <Python.h>
#include <bitprim/nodecint.h>

void* get_ptr(PyObject* obj);

executor_t cast_executor(PyObject* obj);

int char2int(char input);

void hex2bin(const char* src, uint8_t* target);
