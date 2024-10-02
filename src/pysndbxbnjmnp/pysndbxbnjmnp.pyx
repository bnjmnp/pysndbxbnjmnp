#cython: language_level=3

# This is like an include in C, we include the C standard library or libc
# Here we include some selected integer types from the stdint.h header file.
from libc.stdint cimport uint8_t, int32_t, uint32_t

cdef int a_global_variable = 3022

# Provide an extern declaration for the add C function, like we would need to do that in C code.
cdef extern int add(int a, int b)

# This is how to declare an enum.
# Note we use "cpdef" telling the Cython compiler we want a Python-like enum.
cpdef enum CheeseState:
    HARD = 1
    SOFT = 2
    RUNNY = 3

# Actually enum's are used to declare constants, as there is no other nice way of doing this (DEF that is similar to a C #define used to be a way that is now deprecated).
# Cython documentations on using const for defining constants: "Moreover, the const modifier is unusable in a lot of contexts since Cython needs to generate definitions and their assignments separately. Therefore we suggest using it mainly for function argument and pointer types where const is necessary to work with an existing C/C++ interface."
# This enum is only available within Cython code.
cdef enum Constants:
    BUFFER_SIZE = 32

# Define a Python function that makes use of the add C function.
def add_one(number):
    return add(number, 1)

# Example of a cdef class
cdef class CdefAsdf:
    cdef public int instance_variable

    def __cinit__(self):
        self.instance_variable = 0

# Example of a recular Python class
class Asdf:

    def __init__(self):
        self.instance_variable = 0

# Example of a struct - This can only be used inside Cython code
cdef struct Point:
    int x
    int y

# The struct will be returned as a dictionary
def get_point():
    cdef Point p = Point(1, 2)
    return p

def mapping(x):
    # This is the way to go for declaring arrays, a C style declaration is discouraged.
    cdef int[5] mapping_table = [11, 33, 55, 77, 99]  # OK
    return mapping_table[x]

# Example of a context manager
cdef class CmExample:
    cdef public bint enter_was_called
    cdef public bint exit_was_called
    
    def __cinit__(self):
        self.enter_was_called = False
        self.exit_was_called = False

    def __enter__(self):
        self.enter_was_called = True
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.exit_was_called = True
