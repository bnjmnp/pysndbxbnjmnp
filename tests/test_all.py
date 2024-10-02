
import os

import pytest

import pysndbxbnjmnp


def test_global():
    """Regular globals are not accessible."""
    with pytest.raises(AttributeError) as exec_info:
        assert pysndbxbnjmnp.a_global_variable == 3022


def test_enum():
    """Declaring an enum cpdef (note the p) makes it accessible, but the cdef declared enum Constants is not public."""
    assert pysndbxbnjmnp.CheeseState.SOFT == 2
    with pytest.raises(AttributeError) as exec_info:
        pysndbxbnjmnp.Constants


def test_add_one():
    """Check the add_one() function that actually uses our C coded add function."""
    assert pysndbxbnjmnp.add_one(1) == 2


def test_instance_variable():
    """Show that we created instance variables correctly in the cdef class Asdf"""
    a = pysndbxbnjmnp.Asdf()
    b = pysndbxbnjmnp.Asdf()
    a.instance_variable = 3
    b.instance_variable = 7
    assert a.instance_variable == 3
    assert b.instance_variable == 7


def test_understand_class_asdf():
    """Demonstrate that cdef classes cannot be changed dynamically.
    
    Whereas a regular Python class can be changed dynamically.
    """
    asdf = pysndbxbnjmnp.CdefAsdf()
    with pytest.raises(AttributeError) as exec_info:
        asdf.new_attribute = 3

    asdf = pysndbxbnjmnp.Asdf()
    asdf.new_attribute = 7


def test_version():
    """Quick check if the __version__ of the package is accessible for the user."""
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, '../src/pysndbxbnjmnp/__init__.py'), 'r') as fp:
        first_line_of_init_py = fp.readline()
    delim = '"' if '"' in first_line_of_init_py else "'"
    version_string_inside_init_py = first_line_of_init_py.split(delim)[1]
    assert pysndbxbnjmnp.__version__ == version_string_inside_init_py


def test_struct_factory_function():
    point = pysndbxbnjmnp.get_point()
    assert point['x'] == 1
    assert point['y'] == 2


def test_optimized_array_using_function():
    assert pysndbxbnjmnp.mapping(2) == 55


def test_cm():
    """Demo and check fo the context manager implementation."""
    with pysndbxbnjmnp.CmExample() as cm:
        assert cm.enter_was_called
        assert not cm.exit_was_called
    assert cm.exit_was_called