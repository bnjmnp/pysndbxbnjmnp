
=============
pysndbxbnjmnp
=============

My Python sandbox project to try and learn some technologies, including

* Cython
* cibuildwheel
* GitHub Actions
* later maybe: `scikit-build <https://scikit-build.readthedocs.io/en/latest/index.html>`_

TestPyPI: `<https://test.pypi.org/project/pysndbxbnjmnp/>`_

Note
----

* One cannot do it without a setup.py because of the extra Cython build step, but people might work on this: `<https://github.com/pypa/setuptools/issues/2220>`_

Resources
---------

* `Python Packaging User Guide - Packaging Python Projects <https://packaging.python.org/tutorials/packaging-projects/>`_
* `Python Packaging User Guide - Packaging binary Extensions <https://packaging.python.org/guides/packaging-binary-extensions/>`_

  * This led me to `cibuildwheel <https://packaging.python.org/key_projects/#cibuildwheel>`_

* `Setuptools User Guide <https://setuptools.pypa.io/en/latest/userguide/index.html>`_

  * There is a tip for when using Cython in combination with setuptools: `Distributing Extensions compiled with Cython <https://setuptools.pypa.io/en/latest/userguide/ext_modules.html#distributing-extensions-compiled-with-cython>`_

    * This is why don't use ``cythonize()`` in my ``setup.py``.

* `Scikit HEP - On Packaging <https://scikit-hep.org/developer/packaging>`_

  * There is also useful information on how to use GitHub Actions
    
    * `<https://scikit-hep.org/developer/gha_basic>`_
    * `<https://scikit-hep.org/developer/gha_wheels>`_

* `Cython - Interfacing with External C Code <https://cython.readthedocs.io/en/latest/src/userguide/external_C_code.html>`_

  * This helps to understand how to call C code from Cython code.

* `Python Documentation - Distributing Python Modules (Legacy version) - 2. Writing the Setup Script <https://docs.python.org/3/distutils/setupscript.html>`_

  * As I could not find any documentation about the ``setuptools.Extension`` class I assume it is working the same way the ``distutils.core.Extension`` works.
  * You may also have a look at `<https://docs.python.org/3/distutils/apiref.html#distutils.core.Extension>`_

Current State
-------------

* Tests are done locally with tox - using the package that got uploaded to TestPyPI

  * install tox with pip(x)

  * install all Python versions using pyenv

    * install pyenv: `<https://github.com/pyenv/pyenv#automatic-installer>`_

      * install on ubuntu: libffi-dev liblzma-dev zlib1g zlib1g-dev libssl-dev libbz2-dev libsqlite3-dev libncurses5-dev libncursesw5-dev libreadline-dev

      * further help on pyenv: `<https://realpython.com/intro-to-pyenv/>`_

    * download and build needed Python versions ``pyenv install 3.7 3.8 3.9``

    * activate the pyenv versions ``pyenv local 3.7 3.8 3.9``

  * run ``tox`` inside the tests directory to test the project against all specified Python versions.

  * Notes:

    * Check the available python versions: ``pyenv versions``

    * Run tox with refreshed virtual environments: ``tox -r`` 

Development Environment Set-Up
------------------------------

* Create a ``virtualenv`` named ``venv`` from your global Python interpreter.

* Install packages: ``cython`` ``sphinx``, ``build``, ``pytest``, ``tox``, ``myst-parser``

* Activate the ``virtualenv``.

* Create a makefile called ``Makefile`` in the root directory and add this code:

  .. code-block:: make

    build:
        python -m build
      
    clean: uninstall
        -rm -rf pysndbxbnjmnp.egg-info/
        -rm -rf src/pysndbxbnjmnp.egg-info/
        -rm -rf src/pysndbxbnjmnp/__pycache__
        -rm -rf src/pysndbxbnjmnp/pysndbxbnjmnp.cp*
        -rm src/pysndbxbnjmnp/pysndbxbnjmnp.c
        -rm -rf build/
        -rm -rf dist/
        -rm -rf tests/__pycache__
        -rm -rf .pytest_cache

    uninstall:
        python -m pip uninstall -y pysndbxbnjmnp

    install:
        python -m pip install -e .

    test: install
        python -m pytest -v

    .PHONY: build clean uninstall install test

* Now you are ready to run:

  * ``make test`` to build, install and test the project
  * ``make clean`` to uninstall and delete all compile and test artifacts

Docs
----

Specification
^^^^^^^^^^^^^

* Have documentation in the docs directory written in markdown.
* Use sphinx for document generation.
* Have the resulting html hosted on readthedocs.
* Let sphinx pull the API documentation from the source code.
* The creation of a release on GitHub should trigger the build and update of a new readthedocs site.

How to get There
^^^^^^^^^^^^^^^^

* Run ``sphinx-quickstart``.
* Add the ``myst_parser`` and ``sphinx.ext.autodoc`` to the ``config.py``'s ``extensions``.
* Create an ``index.md`` and fill it with content.
* Connect the rtd account with the GitHub account pysndbxbnjmnp is owned by.
* Import pysndbxbnjmnp into the rtd account.

Notes
^^^^^

Use this docstring style: `<https://www.sphinx-doc.org/en/master/usage/domains/python.html#info-field-lists>`_

In order to build the documentation `pysndbxbnjmnp` must be installed into the Python interpreter used.

With the default webhook enabled on Read the Docs, if I got it right:

* stable: represents the latest documentation from a release, when you tagged it using semantic versioning.
* latest: represents the latest documentation pushed to GitHub.
