********
pynflate
********

Pure Python implementation of Deflate data compression algorithm.

Development
===========

Development environment bootstrapping
-------------------------------------

You need only ``virtualenv`` to start developing:

.. code-block:: sh
    cd $PYNFLATE_HOME_DIR

    virtualenv --python=python3 venv
    . venv/bin/activate

    pip install -r requirements_develop.txt
    pip install -e .

    pytest

Dependency management
---------------------
For the development needs, there are two requirement files in the project's root directory:

- ``requirements_test.txt`` contains all the dependencies needed to run the unit tests;
- ``requirements_develop.txt`` contains the testing dependencies and all the additional
  tools used in the development process.

The requirement files mentioned above are not intended for manual editing. Instead they are
managed using `pip-tools`_. The process of updating the requirements is as follows:

#. Add, remove or update a dependency in one of the ``reqs_*.dep`` files:

   - Update ``reqs_install.dep`` if the dependency is needed for the regular installation by
     the end user;
   - Update ``reqs_test.dep`` if the dependency is needed to run the unit tests but is not
     necessary for the regular installation;
   - Update ``reqs_develop.dep`` if the dependency is not in one of the previous categories.

#. Generate the requirements file running ``pip-compile``. The exact command is documented in
   the beginning of each ``requirements_*.txt`` file.
#. Consider running ``pip-sync requirements_develop.txt`` to update the development virtualenv.

Notice that there is no need to edit ``setup.py`` - it will pull the dependencies by itself
from ``reqs_install.dep``.

.. _pip-tools: https://github.com/jazzband/pip-tools


References
==========

* `DEFLATE Compressed Data Format Specification version 1.3 <https://tools.ietf.org/html/rfc1951>`_
* `An Explanation of the Deflate Algorithm <https://zlib.net/feldspar.html>`_
* `LZ77 Specification <https://www.cs.duke.edu/courses/spring03/cps296.5/papers/ziv_lempel_1977_universal_algorithm.pdf>`_
