@echo off

REM Requirements --------------------------------------
REM pip install wheel
REM pip install twine
REM ---------------------------------------------------

pip install  -e .
python setup.py bdist_wheel --universal
twine upload dist/*
