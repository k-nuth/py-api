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

from setuptools import setup, find_packages
from setuptools.extension import Extension
import platform
import glob

# sudo pip install conan_package_tools --upgrade --ignore-installed six
# sudo pip install conan --upgrade  --ignore-installed six
# sudo pip install conan_package_tools  --ignore-installed six
# sudo pip install astroid --upgrade  --ignore-installed six


from conans.client.conan_api import (Conan, default_manifest_folder)
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
        library_dirs=['bitprim/lib'],
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

setup(
    name='bitprim_native',
    version='1.0.8',

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

    packages=('bitprim', ),
    package_data={ 'bitprim': ['bitprim/lib/*bitprim-node-cint.*'] },



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


    data_files = [
        ('/usr/local/lib', glob.glob('bitprim/lib/*bitprim-node-cint.*'))
    ],


# tion="-I/home/fernando/dev/bitprim/bitprim-node-cint/include" --global-option="-L/home/fernando/dev/bitprim/build/bitprim-node-cint" -e .

    ext_modules = extensions
)
