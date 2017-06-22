#

# export LD_LIBRARY_PATH=/home/fernando/dev/bitprim/bitprim-node-cint/cmake-build-debug:$LD_LIBRARY_PATH

del build
python setup.py build
sudo python setup.py install

#pip install .