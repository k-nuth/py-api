# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.


set -e
set -x

python --version

if [[ $TRAVIS_PYTHON_VERSION == 2.7 ]]; then
    export KTH_PYTHON=python
    export KTH_PIP=pip
else
    sudo apt-get update
    sudo apt-get --yes install python3.6
    sudo apt-get --yes install python3.6-dev

    wget https://bootstrap.pypa.io/get-pip.py --no-check-certificate
    sudo python3.6 get-pip.py
    export KTH_PYTHON=python3.6
    export KTH_PIP=pip3.6
fi

sudo $KTH_PIP install --upgrade pip
sudo $KTH_PIP install --upgrade conan_package_tools
sudo $KTH_PIP install --upgrade wheel
sudo $KTH_PIP install --upgrade twine
sudo $KTH_PIP install --upgrade setuptools

conan user
conan remote add kth_temp https://knuth.jfrog.io/artifactory/api/conan/knuth


if [[ "${TRAVIS_BRANCH}" == "dev" ]]; then
    # Just for dev branch
    sudo $KTH_PIP install --upgrade --index-url https://test.pypi.org/pypi/ kth-py-native
fi

cd /home/conan/project

# sudo $KTH_PIP install -v -e .
sudo $KTH_PIP install -e .

if [[ "${UNIT_TESTS}" == "true" ]]; then
    $KTH_PYTHON test/test_chain.py
fi

if [[ "${UPLOAD_PKG}" == "true" ]]; then
    sudo $KTH_PYTHON setup.py sdist
    sudo $KTH_PYTHON setup.py bdist_wheel --universal
fi
