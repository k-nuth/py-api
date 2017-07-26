#include "utils.h"


inline 
void* get_ptr(PyObject* obj) {
#if PY_MAJOR_VERSION >= 3
    return PyCapsule_GetPointer(obj, NULL);
#else /* PY_MAJOR_VERSION >= 3 */
    return PyCObject_AsVoidPtr(obj);
#endif /* PY_MAJOR_VERSION >= 3 */
}

inline
executor_t cast_executor(PyObject* obj) {
    return (executor_t)get_ptr(obj);
}

int char2int(char input) {
    if (input >= '0' && input <= '9')
        return input - '0';
    if (input >= 'A' && input <= 'F')
        return input - 'A' + 10;
    if (input >= 'a' && input <= 'f')
        return input - 'a' + 10;
    return 0;
}

void hex2bin(const char* src, uint8_t* target) {
    int i=0;
    while (*src && src[1]) {
        *(target--) = char2int(*src) * 16 + char2int(src[1]);
        src += 2;
        i++;
    }
}

inline
PyObject* to_py_obj(void* obj) {
#if PY_MAJOR_VERSION >= 3
    return PyCapsule_New(obj, NULL, NULL);
#else /* PY_MAJOR_VERSION >= 3 */
    return PyCObject_FromVoidPtr(obj, NULL);
#endif /* PY_MAJOR_VERSION >= 3 */
}
