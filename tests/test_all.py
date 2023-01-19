
import pysndbxbnjmnp
# if one is doing `Extension("pysndbxbnjmnp.pysndbxbnjmnp", ..` in the setup.py 
# but not providing the package in the setup.cfg
# than you need to import via `from pysndbxbnjmnp import pysndbxbnjmnp`

def test_version():
    assert type(pysndbxbnjmnp.__version__) == str


def test_add_one():
    assert pysndbxbnjmnp.add_one(1) == 2


def test_instance_variable():
    a = pysndbxbnjmnp.Asdf()
    b = pysndbxbnjmnp.Asdf()
    a.instance_variable = 3
    b.instance_variable = 7
    assert a.instance_variable == 3
    assert b.instance_variable == 7