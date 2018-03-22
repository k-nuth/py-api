#!/usr/bin/env python

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


# python -m pip install --no-cache-dir -t out -i https://devpi.yougov.net/root/yg/ zope.interface
# pip install --no-cache-dir --index-url https://test.pypi.org/pypi/ -v -e .

from setuptools import setup
from setuptools.command.install import install
from setuptools.command.develop import develop

__title__ = "bitprim"
__summary__ = "Bitcoin development platform"
__uri__ = "https://github.com/bitprim/bitprim-py"
# __version__ = "1.1.6"
__author__ = "Bitprim Inc"
__email__ = "dev@bitprim.org"
__license__ = "MIT"
__copyright__ = "Copyright 2017 Bitprim developers"


install_requires = [
    "conan >= 1.1.1",
    "conan_package_tools >= 0.5.4",
    "bitprim-native >= 1.1.55",
]

class InstallCommand(install):
    user_options = install.user_options + [
        ('microarch=', None, 'CPU microarchitecture'),
        ('currency=', None, 'Cryptocurrency')
    ]

    def initialize_options(self):
        install.initialize_options(self)
        self.microarch = None
        self.currency = None

    def finalize_options(self):
        install.finalize_options(self)

    def run(self):
        global microarch
        microarch = self.microarch

        global currency
        currency = self.currency

        print('*********************************** (BITPRIM-idiomatic) InstallCommand run microarch')
        print(microarch)
        print(currency)

        install.run(self)

class DevelopCommand(develop):
    user_options = develop.user_options + [
        ('microarch=', None, 'CPU microarchitecture'),
        ('currency=', None, 'Cryptocurrency')
    ]

    def initialize_options(self):
        develop.initialize_options(self)
        self.microarch = None
        self.currency = None

    def finalize_options(self):
        develop.finalize_options(self)

    def run(self):
        global microarch
        microarch = self.microarch

        global currency
        currency = self.currency

        print('*********************************** (BITPRIM-idiomatic) DevelopCommand run microarch')
        print(microarch)
        print(currency)

        develop.run(self)


exec(open('./version.py').read())
setup(
    name = __title__,
    version = __version__,
    description = __summary__,
    long_description=open("./README.rst").read(),
    license = __license__,
    url = __uri__,
    author = __author__,
    author_email = __email__,

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: BSD",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
    ],    

    # What does your project relate to?
    keywords='bitcoin litecoin money bitprim',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    # packages=['bitprim'],

    py_modules=["bitprim"],

    install_requires=install_requires,
    # setup_requires=setup_requires,
    

    dependency_links=[
        'https://testpypi.python.org/pypi',
        'https://testpypi.python.org/pypi/bitprim-native/',
    ],

    # extras_require={
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },

    cmdclass={
        # 'build': BuildCommand,
        'install': InstallCommand,
        'develop': DevelopCommand,
        # 'egg_info': EggInfoCommand,
        
    },
    
)

