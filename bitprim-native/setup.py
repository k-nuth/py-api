# 
# Copyright (c) 2017 Bitprim developers (see AUTHORS)
# 
# This file is part of Bitprim.
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 






#!/usr/bin/env python
# Python binding for Keystone engine. Nguyen Anh Quynh <aquynh@gmail.com>

# upload TestPyPi package with: $ python setup.py sdist upload -r pypitest
# upload PyPi package with: $ python setup.py sdist upload -r pypi

import glob
import os
import platform
import shutil
import stat
import sys

from setuptools import setup, find_packages
from setuptools.extension import Extension

from distutils import dir_util, file_util
from distutils import log
# from distutils.command.build_clib import build_clib
# from distutils.command.install_lib import install_lib
# from distutils.command.sdist import sdist
# from distutils.core import setup

from setuptools.command.install_lib import install_lib
from setuptools.command.install import install
from setuptools.dist import Distribution

from conans.client.conan_api import (Conan, default_manifest_folder)




# # prebuilt libraries for Windows - for sdist
# PATH_LIB64 = "prebuilt/win64/keystone.dll"
# PATH_LIB32 = "prebuilt/win32/keystone.dll"

# # package name can be 'keystone-engine' or 'keystone-engine-windows'
# PKG_NAME = 'keystone-engine'
# if os.path.exists(PATH_LIB64) and os.path.exists(PATH_LIB32):
#     PKG_NAME = 'keystone-engine-windows'
# VERSION = '0.9.1-3'

PKG_NAME = 'bitprim_native'
VERSION = '1.0.25'
SYSTEM = sys.platform

print('SYSTEM')
print(SYSTEM)

SETUP_DATA_FILES = []

# if SYSTEM in ("win32", "cygwin"):
if SYSTEM == "win32":
    SETUP_DATA_FILES.append("bitprim/lib/bitprim-node-cint.dll")
elif SYSTEM == "darwin":
    SETUP_DATA_FILES.append("bitprim/lib/libbitprim-node-cint.dylib")
else:  # Non-OSX
    SETUP_DATA_FILES.append("bitprim/lib/libbitprim-node-cint.so")


# # adapted from commit e504b81 of Nguyen Tan Cong
# # Reference: https://docs.python.org/2/library/platform.html#cross-platform
# is_64bits = sys.maxsize > 2 ** 32


class CustomInstall(install_lib):
    def install(self):
        print('CustomInstall.install')
        install_lib.install(self)
        bitprim_install_dir = os.path.join(self.install_dir, 'bitprim/')
        
        if not os.path.exists(bitprim_install_dir):
            os.makedirs(bitprim_install_dir)

        log.info("bitprim_install_dir: %s" % (bitprim_install_dir, ))
        log.debug("bitprim_install_dir: %s" % (bitprim_install_dir, ))
        print("bitprim_install_dir: %s" % (bitprim_install_dir, ))

        for lib_file in SETUP_DATA_FILES:
            log.info("lib_file: %s" % (lib_file, ))
            log.debug("lib_file: %s" % (lib_file, ))
            print("lib_file: %s" % (lib_file, ))

            filename = os.path.basename(lib_file)
            log.info("filename: %s" % (filename, ))
            log.debug("filename: %s" % (filename, ))
            print("filename: %s" % (filename, ))

            dest_file = os.path.join(self.install_dir, 'bitprim', filename)

            log.info("dest_file: %s" % (dest_file, ))
            log.debug("dest_file: %s" % (dest_file, ))
            print("dest_file: %s" % (dest_file, ))

            # file_util.copy_file(lib_file, bitprim_install_dir)
            file_util.copy_file(lib_file, dest_file)

# class CustomInstallCommand(install):
#     """Customized setuptools install command - prints a friendly greeting."""
#     def run(self):
#         print("Hello, developer, how are you? :)")
#         install.run(self)


# def dummy_src():
#     return []


# setup(
#     provides=['keystone'],
#     packages=['keystone'],
#     name=PKG_NAME,
#     version=VERSION,
#     author='Nguyen Anh Quynh',
#     author_email='aquynh@gmail.com',
#     description='Keystone assembler engine',
#     url='http://www.keystone-engine.org',
#     classifiers=[
#         'License :: OSI Approved :: BSD License',
#         'Programming Language :: Python :: 2',
#         'Programming Language :: Python :: 3',
#     ],
#     requires=['ctypes'],

#     # cmdclass=dict(
#     #     build_clib=custom_build_clib,
#     #     sdist=custom_sdist,
#     #     install_lib=CustomInstall,
#     # ),
#     cmdclass=dict(
#         install_lib=CustomInstall,
#     ),


#     libraries=[(
#         'keystone', dict(
#             package='keystone',
#             sources=dummy_src()
#         ),
#     )],
# )

# ------------------------------------------------


# sudo pip install conan_package_tools --upgrade --ignore-installed six
# sudo pip install conan --upgrade  --ignore-installed six
# sudo pip install conan_package_tools  --ignore-installed six
# sudo pip install astroid --upgrade  --ignore-installed six


c = Conan.factory()


try:
    # c.remote_add(remote, url, verify_ssl, args.insert)
    c.remote_add('bitprim', 'https://api.bintray.com/conan/bitprim/bitprim')
except:
    print ("Conan Remote exists, ignoring exception")

# refe = "bitprim-node-cint/0.1@bitprim/stable"
refe = "."
# c.install(refe, verify=None, manifests=None)
c.install(refe, verify=None, manifests_interactive=None, manifests=None)




extensions = [
	Extension('bitprim_native',

    	sources = ['chain/header.c', 'chain/block.c', 'chain/merkle_block.c', 'bitprimmodule.c',
        'utils.c', 'chain/chain.c', 'binary.c', 'chain/point.c', 'chain/history.c', 'chain/word_list.c', 
        'chain/transaction.c', 'chain/output.c', 'chain/output_list.c',  'chain/input.c', 'chain/input_list.c', 
        'chain/script.c', 'chain/payment_address.c', 'chain/compact_block.c', 'chain/output_point.c'],
        include_dirs=['bitprim/include'],
        # library_dirs=['bitprim/lib'],
        library_dirs=['.'],
        libraries = ['bitprim-node-cint'],
        # runtime_library_dirs = ['lib/site-packages'],

        # define_macros=list(EXTRA_DEFINES.iteritems()),
        # extra_compile_args=conf["CXXFLAGS"],
        # extra_link_args=conf["LDFLAGS"],

    	# extra_link_args= ['-Wl,-rpath,'+lib_path]
    ),
    # Extension(
    #     "myPackage.myModule",
    #     ["myPackage/myModule.pyx"],
    #     include_dirs=['/some/path/to/include/'], # not needed for fftw unless it is installed in an unusual place
    #     libraries=['fftw3', 'fftw3f', 'fftw3l', 'fftw3_threads', 'fftw3f_threads', 'fftw3l_threads'],
    #     library_dirs=['/some/path/to/include/'], # not needed for fftw unless it is installed in an unusual place
    # ),
]

# print(platform.system())

# if platform.system() == 'Darwin':
# 	lib_path = '/usr/local/lib'
# 	extensions[0].extra_link_args.append('-Wl,-rpath,'+lib_path)

# print(extensions[0].extra_link_args)

class MyDist(Distribution):
     def has_ext_modules(self):
         return True



setup(
    # name='bitprim_native',
    # version='1.0.14',
    name=PKG_NAME,
    version=VERSION,

    description='Bitprim Platform',
    long_description='Bitprim Platform',
    url='https://github.com/bitprim/bitprim-py',

    # Author details
    author='Bitprim Inc',				#TODO!
    author_email='dev@bitprim.org',		#TODO!

    # Choose your license
    license='MIT',    					#TODO!

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        'Programming Language :: C++',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='bitcoin litecoin cash money bitprim',

    # # You can just specify the packages manually here if your project is
    # # simple. Or you can use find_packages().
    # packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    # packages=['bitprim-node-cint'],
    # # package_dir={'bitprim-node-cint': 'src/mypkg'},
    # package_dir={'bitprim-node-cint': './'},
    # package_data={'bitprim-node-cint': ['bitprim/lib/*bitprim-node-cint.*']},
    # packages=('bitprim', ),
    # package_data={ 'bitprim': ['bitprim/lib/*bitprim-node-cint*'] },

    packages=['bitprim'],
    package_data={ 'bitprim': ['libbitprim-node-cint.so'] },

    # distclass = MyDist,

    # eager_resources=['bitprim/lib/libbitprim-node-cint.so'],

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # # List run-time dependencies here.  These will be installed by pip when
    # # your project is installed. For an analysis of "install_requires" vs pip's
    # # requirements files see:
    # # https://packaging.python.org/en/latest/requirements.html
    # install_requires=['peppercorn'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

#   data_files = [('lib\\site-packages',['C:\\development\\bitprim\\build\\bitprim-node-cint\\bitprim-node-cint.dll'])],

	# data_files = [('lib\\site-packages', ['bitprim-node-cint\\lib\\bitprim-node-cint.dll'])],
    # data_files = [
    #     ('lib/site-packages', ['bitprim-node-cint/lib/bitprim-node-cint.*'])
    # ],

    # data_files = [
    #     ('lib/site-packages', glob.glob('bitprim-node-cint/lib/*bitprim-node-cint.*'))
    # ],


    # data_files = [
    #     ('/usr/local/lib', glob.glob('bitprim/lib/*bitprim-node-cint.*'))
    # ],


# tion="-I/home/fernando/dev/bitprim/bitprim-node-cint/include" --global-option="-L/home/fernando/dev/bitprim/build/bitprim-node-cint" -e .

    # cmdclass=dict(
    #     install_lib=CustomInstall,
    #     # install=CustomInstallCommand,
    # ),

    ext_modules = extensions
)
