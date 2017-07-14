@echo off

REM Requirements --------------------------------------
REM pip install wheel
REM pip install twine
REM ---------------------------------------------------

pip install --global-option=build_ext --global-option="-IC:/development/bitprim/bitprim-node-cint/include" --global-option="-LC:/development/bitprim/build/bitprim-node-cint/" -e .
python setup.py bdist_wheel
twine upload dist/*
