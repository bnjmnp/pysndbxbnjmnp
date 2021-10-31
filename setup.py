from setuptools import setup, Extension

ext_modules = [
    Extension("pysndbxbnjmnp", ["src/pysndbxbnjmnp.pyx", "src/add.c"])
]

setup(
    ext_modules = ext_modules,
)