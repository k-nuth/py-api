# Requirements --------------------------------------
# pip install wheel
# pip install twine
# ---------------------------------------------------

pip install --global-option=build_ext --global-option="-I/home/fernando/dev/bitprim/bitprim-node-cint/include" --global-option="-L/home/fernando/dev/bitprim/build/bitprim-node-cint" -e .

python setup.py sdist
# python setup.py bdist_wheel

/home/fernando/.local/bin/twine upload dist/*
