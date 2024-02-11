#cython: language_level=3

cdef int a_global_variable = 3022

# Provide an extern declaration for the add C function, like we would need to do that in C code.
cdef extern int add(int a, int b)

# This is how to declare an enum
# Note we use "cpdef" telling the Cython compiler we want a Python-like enum.
cpdef enum CheeseState:
    HARD = 1
    SOFT = 2
    RUNNY = 3

# Actually enum's are used to declare constants, as there is no other nice way of doing this (DEF that is similar to a C #define used to be a way that is now deprecated).
cdef enum Constants:
    BUFFER_SIZE = 32

# Define a Python function that makes use of the add C function.
def add_one(number):
    return add(number, 1)

# Example of a cdef class
cdef class Asdf:
    cdef public int instance_variable

    def __cinit__(self):
        self.instance_variable = 0
