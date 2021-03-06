
=============
pysndbxbnjmnp
=============

My Python sandbox project to try and learn some technologies, including

* Cython
* cibuildwheel
* GitHub Actions
* later maybe: `scikit-build <https://scikit-build.readthedocs.io/en/latest/index.html>`_

Note
----

* we cannot do it without a setup.py because of the extra Cython build step, but they might work on this: `<https://github.com/pypa/setuptools/issues/2220>`_

Resources
---------

* `Python Packaging User Guide - Packaging Python Projects <https://packaging.python.org/tutorials/packaging-projects/>`_
* `Python Packaging User Guide - Packaging binary Extensions <https://packaging.python.org/guides/packaging-binary-extensions/>`_

  * This led me to `cibuildwheel <https://packaging.python.org/key_projects/#cibuildwheel>`_

* `Setuptools User Guide <https://setuptools.pypa.io/en/latest/userguide/index.html>`_

  * There is a tip for when using Cython in combination with setuptools: `Distributing Extensions compiled with Cython <https://setuptools.pypa.io/en/latest/userguide/distribution.html#distributing-extensions-compiled-with-cython>`_

* `Scikit HEP - On Packaging <https://scikit-hep.org/developer/packaging>`_

  * There is also useful information on how to use GitHub Actions
    
    * `<https://scikit-hep.org/developer/gha_basic>`_
    * `<https://scikit-hep.org/developer/gha_wheels>`_

* `Cython - Interfacing with External C Code <https://cython.readthedocs.io/en/latest/src/userguide/external_C_code.html>`_

  * This helps to understand how to call C code from Cython code.