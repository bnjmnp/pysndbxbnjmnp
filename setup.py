
import codecs
import os.path

from setuptools import setup, Extension

ext_modules = [
    Extension("pysndbxbnjmnp.pysndbxbnjmnp", ["src/pysndbxbnjmnp/pysndbxbnjmnp.pyx", "src/pysndbxbnjmnp/add.c"])
]

setup(
    ext_modules=ext_modules,
)