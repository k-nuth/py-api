#!/bin/bash
sudo pip install --upgrade conan_package_tools
conan user

conan remote add bitprim_temp https://api.bintray.com/conan/bitprim/bitprim

conan install .
pip install  -e .

/bin/bash
