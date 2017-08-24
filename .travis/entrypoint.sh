#!/bin/bash

python --version


if [[ $TRAVIS_PYTHON_VERSION == 2.7 ]]; then
    echo "2.7 -- 1"
    export BITPRIM_PYTHON=python
    export BITPRIM_PIP=pip
else
    echo "2.7 -- 1 -- ELSE"
    sudo apt-get update
    sudo apt-get --yes install python3.6
    wget https://bootstrap.pypa.io/get-pip.py
    sudo python3.6 get-pip.py
    export BITPRIM_PYTHON=python3.6
    export BITPRIM_PIP=pip3.6
fi


sudo $BITPRIM_PIP install --upgrade pip
sudo $BITPRIM_PIP install --upgrade conan_package_tools
sudo $BITPRIM_PIP install --upgrade wheel
sudo $BITPRIM_PIP install --upgrade twine
sudo $BITPRIM_PIP install --upgrade setuptools 

conan user

conan remote add bitprim_temp https://api.bintray.com/conan/bitprim/bitprim

cd /home/conan/project

sudo $BITPRIM_PIP install -v -e .
sudo $BITPRIM_PYTHON setup.py sdist
sudo $BITPRIM_PYTHON setup.py bdist_wheel --universal

$BITPRIM_PYTHON --version
$BITPRIM_PYTHON test/test_1.py
