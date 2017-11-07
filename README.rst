|travis| |appveyor|

bitprim
=======

Bitcoin, Bitcoin Cash and Litecoin development platform for Python applications

Getting started 
---------------

Stable version:

.. code-block:: bash

    $ pip install --upgrade bitprim

Development version:

.. code-block:: bash

    $ pip install --upgrade --index-url https://test.pypi.org/pypi/ bitprim

If you want a fully optimized binary for a specific microarchitecture, for example:

.. code-block:: bash

    $ pip install --upgrade --install-option="--microarch=skylake" bitprim

(use :code:`--index-url https://test.pypi.org/pypi/` for Dev version)

Reference documentation
-----------------------

For more detailed documentation, please refer to `<https://www.bitprim.org/>`_.


.. |travis| image:: https://travis-ci.org/bitprim/bitprim-py.svg?branch=master
 		   :target: https://travis-ci.org/bitprim/bitprim-py
 		   
.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/bitprim/bitprim-py?branch=master&svg=true
  		     :target: https://ci.appveyor.com/project/bitprim/bitprim-py?branch=master


