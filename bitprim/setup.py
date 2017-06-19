# -------------------------------------------
# Ubuntu
# sudo apt-get install python-dev
# python setup.py build
# sudo python setup.py install
# export LD_LIBRARY_PATH=/home/fernando/dev/bitprim/bitprim-node-cint/cmake-build-debug:$LD_LIBRARY_PATH
# -------------------------------------------


from distutils.core import setup, Extension

# module1 = Extension('bitprim_native',
#                     sources = ['bitprimmodule.c'])
#
# module1 = Extension('demo',
#                     define_macros = [('MAJOR_VERSION', '1'),
#                                      ('MINOR_VERSION', '0')],
#                     include_dirs = ['/usr/local/include'],
#                     libraries = ['tcl83'],
#                     library_dirs = ['/usr/local/lib'],
#                     sources = ['demo.c'])


# ---------------------------------------------------
# Hardcoded paths for Ubuntu version -- TODO
# ---------------------------------------------------

module1 = Extension('bitprim_native',
                    include_dirs = ['/home/fernando/dev/bitprim/bitprim-node-cint/include'],
                    libraries = ['bitprim-node-cint'],
                    library_dirs = ['/home/fernando/dev/bitprim/bitprim-node-cint/cmake-build-debug'],
                    sources = ['bitprimmodule.c'])

# ---------------------------------------------------
# Hardcoded paths for Windows version -- TODO
# ---------------------------------------------------

# module1 = Extension('bitprim_native',
#                     include_dirs = ['C:/development/bitprim/bitprim-node-cint/include'],
#                     libraries = ['bitprim-node-cint'],
#                     library_dirs = ['/home/fernando/dev/bitprim/bitprim-node-cint/cmake-build-release'],
#                     sources = ['bitprimmodule.c'])


# ---------------------------------------------------

#cgo CFLAGS: -I -IC:/development/bitprim/bitprim-core/include
#cgo LDFLAGS: -LC:/development/bitprim/bitprim-node-cint/cmake-build-release -lbitprim-node-cint


# setup (name = 'PackageName',
#        version = '1.0',
#        description = 'This is a demo package',
#        author = 'Martin v. Loewis',
#        author_email = 'martin@v.loewis.de',
#        url = 'https://docs.python.org/extending/building',
#        long_description = '''
# This is really just a demo package.
# ''',
#        ext_modules = [module1])


setup (name = 'Bitprim',
       version = '1.0',
       description = 'Bitprim Full-Node Bitcoin library',
       ext_modules = [module1])


