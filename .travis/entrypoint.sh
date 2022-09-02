# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

set -e
set -x

/root/opt/bin/python3 --version

echo $PATH
export PATH="$HOME/.local/bin/:$PATH"
export PATH="$HOME/opt/bin/:$PATH"
echo $PATH

pip3 install --upgrade setuptools --user
pip3 install --upgrade kthbuild --user
pip3 install --upgrade conan_package_tools --user
pip3 install --upgrade twine --user
pip3 install --upgrade wheel --user
# pip3 install auditwheel


conan --version
conan user

conan profile list
conan profile new default --detect || true
conan profile list

# conan remote add kth_temp https://knuth.jfrog.io/artifactory/api/conan/knuth
conan config install https://github.com/k-nuth/ci-utils/raw/master/conan/config.zip
conan profile list
conan profile update settings.compiler.libcxx=libstdc++11 default

cd /home/conan/project

pip3 install  -e .

python3 setup.py sdist
python3 setup.py bdist_wheel --universal
