
import pysndbxbnjmnp
# if one is doing `Extension("pysndbxbnjmnp.pysndbxbnjmnp", ..` in the setup.py 
# but not providing the package in the setup.cfg
# than you need to import via `from pysndbxbnjmnp import pysndbxbnjmnp`

def test_version():
    assert type(pysndbxbnjmnp.__version__) == str


def test_add_one():
    assert pysndbxbnjmnp.add_one(1) == 2