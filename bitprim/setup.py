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
import platform
import bitprim

install_requires = [
    "conan >= 0.25.1",
    "conan_package_tools >= 0.5.4",
    "bitprim-native >= 1.0.36",
]

# install_requires = [
#     "tqdm >= 4.14",
#     "pkginfo >= 1.0",
#     "requests >= 2.5.0, != 2.15, != 2.16",
#     "requests-toolbelt >= 0.8.0",
#     "setuptools >= 0.7.0",
# ]

# if sys.version_info[:2] < (2, 7):
#     install_requires += [
#         "argparse",
#     ]


setup(
    name = bitprim.__title__,
    version = bitprim.__version__,
    description = bitprim.__summary__,
    long_description=open("../README.rst").read(),
    license = bitprim.__license__,
    url = bitprim.__uri__,
    author = bitprim.__author__,
    author_email = bitprim.__email__,

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

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)

