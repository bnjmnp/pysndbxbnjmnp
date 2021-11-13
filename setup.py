
import codecs
import os.path

from setuptools import setup, Extension


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    """Get the __version__ string variable from a given file.

    Taken from: https://packaging.python.org/guides/single-sourcing-package-version/
    """
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

ext_modules = [
    Extension("pysndbxbnjmnp.pysndbxbnjmnp", ["src/pysndbxbnjmnp/pysndbxbnjmnp.pyx", "src/pysndbxbnjmnp/add.c"])
]

setup(
    version=get_version("src/pysndbxbnjmnp/__init__.py"),
    ext_modules=ext_modules,
)