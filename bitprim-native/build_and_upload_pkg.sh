# Requirements --------------------------------------
# pip install wheel
# pip install twine
# ---------------------------------------------------

# pip install --global-option=build_ext --global-option="-I/home/fernando/dev/bitprim/bitprim-node-cint/include" --global-option="-L/home/fernando/dev/bitprim/build/bitprim-node-cint" -e .
pip install  -e .

# python setup.py sdist                       # Source Distribution
# python setup.py bdist_wheel --universal     # Universal Wheels, Pure Python, for py2 and py3
# python setup.py bdist_wheel                 # Pure Python Wheels, Pure Python, but don’t natively support both Python 2 and 3.

# python setup.py bdist_wheel                 # Platform Wheels, with compiled extensions.

/home/fernando/.local/bin/twine upload dist/*
