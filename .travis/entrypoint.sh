#!/bin/bash
sudo pip install --upgrade conan_package_tools
sudo pip install --upgrade wheel
sudo pip install --upgrade twine

conan user

conan remote add bitprim_temp https://api.bintray.com/conan/bitprim/bitprim

cd /home/conan/project

sudo pip install -v -e .
sudo python setup.py sdist
sudo python setup.py bdist_wheel --universal

