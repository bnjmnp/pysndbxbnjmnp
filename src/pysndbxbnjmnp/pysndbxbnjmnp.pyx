#cython: language_level=3

cdef extern int add(int a, int b)

def add_one(number):
    return add(number, 1)


cdef class Asdf:
    cdef public int instance_variable

    def __cinit__(self):
        self.instance_variable = 0
