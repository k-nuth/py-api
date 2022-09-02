# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.


"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
import re
import os

from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open

def get_requires(filename):
    requirements = []
    with open(filename, 'rt') as req_file:
        for line in req_file.read().splitlines():
            if not line.strip().startswith("#"):
                requirements.append(line)
    return requirements


def load_version():
    """Loads a file content"""
    filename = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                            "kth", "__init__.py"))
    with open(filename, "rt") as version_file:
        conan_init = version_file.read()
        version = re.search("__version__ = '([0-9a-z.-]+)'", conan_init).group(1)
        return version


project_requirements = get_requires("kth/requirements.txt")

setup(
    name='kth',
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=load_version(),

    description='Bitcoin Cash development platform for Python applications',

    # The project's main homepage.
    url='https://github.com/k-nuth/py-api',

    # Author details
    author='Knuth Prokect',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
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
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        "Programming Language :: Python :: Implementation :: CPython",
    ],

    # What does your project relate to?
    keywords=['bitcoin', 'cash', 'bch', 'money', 'knuth', 'kth'],

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=project_requirements,

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'kth': ['*.txt'],
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],

    # # To provide executable scripts, use entry points in preference to the
    # # "scripts" keyword. Entry points provide cross-platform support and allow
    # # pip to create the appropriate form of executable for the target platform.
    # entry_points={
    #     'console_scripts': [
    #         'run_create_in_docker=cpt.run_in_docker:run',
    #     ],
    # },
)


# #!/usr/bin/env python

# # Copyright (c) 2016-2022 Knuth Project developers.
# # Distributed under the MIT software license, see the accompanying
# # file COPYING or http://www.opensource.org/licenses/mit-license.php.

# # python -m pip install --no-cache-dir -t out -i https://devpi.yougov.net/root/yg/ zope.interface
# # pip install --no-cache-dir --index-url https://test.pypi.org/pypi/ -v -e .

# from setuptools import setup
# from setuptools.command.install import install
# from setuptools.command.develop import develop

# __title__ = "kth"
# __summary__ = "Bitcoin Cash development platform for Python applications"
# __uri__ = "https://github.com/k-nuth/py-api"
# __author__ = "Knuth Prokect"
# __license__ = "MIT"
# __copyright__ = "Copyright 2022 Knuth Project developers"

# install_requires = [
#     "conan >= 1.51.3",
#     "conan_package_tools >= 0.5.4",
#     "kth-py-native >= 0.7.0",
# ]

# class InstallCommand(install):
#     user_options = install.user_options + [
#         ('microarch=', None, 'CPU microarchitecture'),
#         ('currency=', None, 'Cryptocurrency')
#     ]

#     def initialize_options(self):
#         install.initialize_options(self)
#         self.microarch = None
#         self.currency = None

#     def finalize_options(self):
#         install.finalize_options(self)

#     def run(self):
#         global microarch
#         microarch = self.microarch

#         global currency
#         currency = self.currency

#         print('*********************************** (Knuth-idiomatic) InstallCommand run microarch')
#         print(microarch)
#         print(currency)

#         install.run(self)

# class DevelopCommand(develop):
#     user_options = develop.user_options + [
#         ('microarch=', None, 'CPU microarchitecture'),
#         ('currency=', None, 'Cryptocurrency')
#     ]

#     def initialize_options(self):
#         develop.initialize_options(self)
#         self.microarch = None
#         self.currency = None

#     def finalize_options(self):
#         develop.finalize_options(self)

#     def run(self):
#         global microarch
#         microarch = self.microarch

#         global currency
#         currency = self.currency

#         print('*********************************** (Knuth-idiomatic) DevelopCommand run microarch')
#         print(microarch)
#         print(currency)

#         develop.run(self)


# exec(open('./version.py').read())
# setup(
#     name = __title__,
#     version = __version__,
#     description = __summary__,
#     long_description=open("./README.rst").read(),
#     license = __license__,
#     url = __uri__,
#     author = __author__,

#     classifiers=[
#         # How mature is this project? Common values are
#         #   3 - Alpha
#         #   4 - Beta
#         #   5 - Production/Stable
#         'Development Status :: 3 - Alpha',

#         "Intended Audience :: Developers",
#         'License :: OSI Approved :: MIT License',
#         "Natural Language :: English",
#         "Operating System :: MacOS :: MacOS X",
#         "Operating System :: POSIX",
#         "Operating System :: POSIX :: BSD",
#         "Operating System :: POSIX :: Linux",
#         "Operating System :: Microsoft :: Windows",

#         "Programming Language :: Python",
#         'Programming Language :: Python :: 3',
#         'Programming Language :: Python :: 3.7',
#         'Programming Language :: Python :: 3.8',
#         'Programming Language :: Python :: 3.9',
#         'Programming Language :: Python :: 3.10',
#         "Programming Language :: Python :: Implementation :: CPython",
#     ],

#     # What does your project relate to?
#     keywords='bitcoin cash bch money knuth kth',

#     # You can just specify the packages manually here if your project is
#     # simple. Or you can use find_packages().
#     # packages=find_packages(exclude=['contrib', 'docs', 'tests']),
#     # packages=['kth'],

#     py_modules=["kth"],

#     install_requires=install_requires,
#     # setup_requires=setup_requires,


#     dependency_links=[
#         'https://testpypi.python.org/pypi',
#         'https://testpypi.python.org/pypi/kth-py-native/',
#     ],

#     # extras_require={
#     #     'dev': ['check-manifest'],
#     #     'test': ['coverage'],
#     # },

#     cmdclass={
#         # 'build': BuildCommand,
#         'install': InstallCommand,
#         'develop': DevelopCommand,
#         # 'egg_info': EggInfoCommand,

#     },

# )

