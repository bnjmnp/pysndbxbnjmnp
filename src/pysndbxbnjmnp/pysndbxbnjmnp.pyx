#cython: language_level=3

cdef extern int add(int a, int b)

def add_one(number):
    return add(number, 1)