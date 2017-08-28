pip install Sphinx
cd bitprim-py
sphinx-apidoc -f -o doc/source .

# doc/make html



sphinx-build -b html doc/source doc/build
sphinx-build -b singlehtml doc/source doc/build

