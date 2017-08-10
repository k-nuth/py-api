#!/bin/bash
sudo pip install --upgrade conan_package_tools
sudo pip install --upgrade wheel
sudo pip install --upgrade twine

conan user

conan remote add bitprim_temp https://api.bintray.com/conan/bitprim/bitprim

cd /home/conan/project
conan install .
sudo pip install  -e .

# python setup.py sdist

# twine upload -u ${PYPI_USER_NAME} -p ${PYPI_PASSWORD} dist/*

# /bin/bash
