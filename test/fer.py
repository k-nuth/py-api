from __future__ import print_function

# class OutputList:
#     def __init__(self, ptr):
#         self._ptr = ptr

#     def push_back(self, output):
#         bn.output_list_push_back(self._ptr, output._ptr)

#     def _count(self):
#         return bn.output_list_count(self._ptr)

#     def _nth(self, n):
#         return Output(bn.output_list_nth(self._ptr, n))

#     def __len__(self):
#         return self._count()

#     def __getitem__(self, key):
#         return self._nth(key)

class _AList:
    def _destroy(self):
        print('_AList::_destroy')

    # def push_back(self, block):
    #     print('_AList::push_back')

    def _count(self):
        print('_AList::_count')

    def _nth(self, n):
        print('_AList::_nth')
        return 99


class _BList:
    def _destroy(self):
        print('_BList::_destroy')

    # def push_back(self, block):
    #     print('_BList::push_back')

    def _count(self):
        print('_BList::_count')

    def _nth(self, n):
        print('_BList::_nth')
        return 88

class _CList:
    def __init__(self, ptr, destroy_code, count_code, nth_code):
        print('_CList::__init__')
        self._ptr = ptr
        self._destroy_code = destroy_code
        self._count_code = count_code
        self._nth_code = nth_code

    def _destroy(self):
        print('_CList::_destroy')
        return self._destroy_code(self._ptr)

    # def push_back(self, x):
    #     print('_CList::push_back')
    #     bn.x_list_push_back(self._ptr, x._ptr)

    def _count(self):
        print('_CList::_count')
        return self._count_code(self._ptr)

    def _nth(self, n):
        print('_CList::_nth')
        return self._nth_code(self._ptr, n)


class GenericListOld():
    def __init__(self, internal_list):
        self._internal_list = internal_list
    
    def __del__(self):
        self._internal_list._destroy()

    def __len__(self):
        return self._internal_list._count()

    def __getitem__(self, key):
        return self._internal_list._nth(key)

    def __iter__(self):
        for i in xrange(len(self)):
            yield self[i]




# a = GenericList(_AList())
# print(a[15])

# b = GenericList(_BList())
# print(b[15])



class GenericList():
    def __init__(self, ptr, destroy_code, count_code, nth_code):
        print('GenericList::__init__')
        self._ptr = ptr
        self._destroy_code = destroy_code
        self._count_code = count_code
        self._nth_code = nth_code
    
    def __del__(self):
        print('GenericList::__del__')
        return self._destroy_code(self._ptr)

    # def push_back(self, x):
    #     print('_CList::push_back')
    #     bn.x_list_push_back(self._ptr, x._ptr)

    def __len__(self):
        print('GenericList::__len__')
        return self._count_code(self._ptr)

    def __getitem__(self, key):
        print('GenericList::__getitem__')
        return self._nth_code(self._ptr, key)

    def __iter__(self):
        for i in xrange(len(self)):
            yield self[i]





# c = GenericList(1234,   lambda x: print("destroy x: %d" % (x,)), 
#                         lambda x: print("count x: %d" % (x,)), 
#                         lambda x, n: print("nth x: %d, n: %d" % (x, n)))

c = GenericList(1234,   lambda x: print("destroy x: %d" % (x,)), 
                        lambda x: 123, 
                        lambda x, n: 987)

print(c[15])

