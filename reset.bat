
@echo off

rd /s /q bitprim.egg-info
rd /s /q __pycache__
del bitprim_native.so
rd /s /q build
rd /s /q dist

rd /s /q blockchain
del debug.log
del error.log
rd /s /q blockchain

del bitprim.pyc 
del setup.cfg.py 
del setup.cfg