# Requirements --------------------------------------
# pip install wheel
# pip install twine
# ---------------------------------------------------

sudo ./reset.sh
conan install .

# pip install --global-option=build_ext --global-option="-I/home/fernando/dev/bitprim/bitprim-node-cint/include" --global-option="-L/home/fernando/dev/bitprim/build/bitprim-node-cint" -e .
sudo pip install -v -e .

# Linux
# sudo python setup.py sdist                       # Source Distribution

# python setup.py bdist_wheel --universal     # Universal Wheels, Pure Python, for py2 and py3
# python setup.py bdist_wheel                 # Pure Python Wheels, Pure Python, but don’t natively support both Python 2 and 3.
# python setup.py bdist_wheel                 # Platform Wheels, with compiled extensions.

# No se que garcha es esto!
# sudo python setup.py bdist_egg --plat-name=abc
# sudo python setup.py bdist_egg


# /home/fernando/.local/bin/twine upload dist/*

# sudo ./reset.sh



# --------------------------------------------------
# Luego, para el que instala

# pip install bitprim-native --no-cache-dir