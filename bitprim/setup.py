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
    "bitprim-native >= 1.0.1",
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
    # name='bitprim',
    # version='1.0.2',

    # description='Bitprim Platform',
    # long_description=open("../README.md").read(),
    # url='https://github.com/bitprim/bitprim-py',

    # # Author details
    # author='Bitprim Inc',				#TODO!
    # author_email='dev@bitprim.org',		#TODO!
    # license='MIT',    					#TODO!

    name = bitprim.__title__,
    version = bitprim.__version__,
    description = bitprim.__summary__,
    long_description=open("../README.md").read(),
    license = bitprim.__license__,
    url = bitprim.__uri__,
    author = bitprim.__author__,
    author_email = bitprim.__email__,


    # # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    # classifiers=[
    #     # How mature is this project? Common values are
    #     #   3 - Alpha
    #     #   4 - Beta
    #     #   5 - Production/Stable
    #     'Development Status :: 3 - Alpha',

    #     # Indicate who your project is intended for
    #     'Intended Audience :: Developers',
    #     'Topic :: Software Development :: Build Tools',

    #     # Pick your license as you wish (should match "license" above)
    #     'License :: OSI Approved :: MIT License',

    #     # Specify the Python versions you support here. In particular, ensure
    #     # that you indicate whether you support Python 2, Python 3 or both.
    #     'Programming Language :: Python :: 2',
    #     'Programming Language :: Python :: 2.7',
    #     'Programming Language :: Python :: 3',
    #     'Programming Language :: Python :: 3.3',
    #     'Programming Language :: Python :: 3.4',
    #     'Programming Language :: Python :: 3.5',
    # ],

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


    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],
    py_modules=["bitprim"],

    # install_requires=['bitprim-native'],
    install_requires=install_requires,


    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    # # If there are data files included in your packages that need to be
    # # installed, specify them here.  If using Python 2.6 or less, then these
    # # have to be included in MANIFEST.in as well.
    # package_data={
    #     'sample': ['package_data.dat'],
    # },

    # # Although 'package_data' is the preferred approach, in some case you may
    # # need to place data files outside of your packages. See:
    # # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],




    # # To provide executable scripts, use entry points in preference to the
    # # "scripts" keyword. Entry points provide cross-platform support and allow
    # # pip to create the appropriate form of executable for the target platform.
    # entry_points={
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },

    # ext_modules = cythonize(extensions)
    # ext_modules = extensions
)



# # ----------------------------------------------------------------------------------
