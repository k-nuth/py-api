|travis| |appveyor|

kth
=======

Bitcoin, Bitcoin Cash and Litecoin development platform for Python applications

Getting started
---------------

Stable version:

.. code-block:: bash

    $ pip install --upgrade kth

Development version:

.. code-block:: bash

    $ pip install --upgrade --index-url https://test.pypi.org/pypi/ kth

If you want a fully optimized binary for a specific microarchitecture, for example:

.. code-block:: bash

    $ pip install --upgrade --install-option="--microarch=skylake" kth

(use :code:`--index-url https://test.pypi.org/pypi/` for Dev version)

Reference documentation
-----------------------

For more detailed documentation, please refer to `<https://kth.cash/>`_.


.. |travis| image:: https://travis-ci.org/kth/kth-py.svg?branch=master
 		   :target: https://travis-ci.org/kth/kth-py

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/kth/kth-py?branch=master&svg=true
  		     :target: https://ci.appveyor.com/project/kth/kth-py?branch=master


