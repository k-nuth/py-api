from conans import ConanFile, CMake
# import os

class BitprimTestForPy(ConanFile):
    name = "bitprim-test-for-py"
    version = "0.1"
    license = "http://www.boost.org/users/license.html"
    url = "https://github.com/bitprim/bitprim-py"
    description = "Bitcoin Full Node Library with Python interface"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    # exports_sources = "src/*", "CMakeLists.txt", "cmake/*", "bitprim-node-cintConfig.cmake.in", "include/*", "test/*", "console/*"
    # package_files = "build/lbitprim-node-cint.so"
    # build_policy = "missing"

    # TODO(fernando): queda pendiente seleccionar el default Shared=False
    requires = (("bitprim-node-cint/0.1@bitprim/stable"))
    # default_options = "bitprim-node-cint:shared=False" #, "OpenSSL:shared=True"


    # conan install bitprim-node-cint/0.1@bitprim/stable -o shared=True
    # conan install -o Pkg:shared=True -o OtherPkg:option=value

    def imports(self):
        # self.copy("*.h", "./bitprim/include/bitprim", "include/bitprim")
        # self.copy("*.hpp", dst="./bitprim/include/bitprim", src="include/bitprim")
        # self.copy("*.dylib", dst="./bitprim/lib", src="lib")
        # self.copy("*.so", dst="./bitprim/lib", src="lib")
        # self.copy("*.lib", dst="./bitprim/lib", src="lib")
        # self.copy("*.dll", dst="./bitprim/lib", src="lib")
        self.copy("*.h", "./bitprim/include/bitprim", "include/bitprim")
        self.copy("*.hpp", dst="./bitprim/include/bitprim", src="include/bitprim")
        
        self.copy("*.lib", dst="./bitprim/lib", src="lib")
        self.copy("*.a", dst="./bitprim/lib", src="lib")
        self.copy("*.dylib", dst="./bitprim/lib", src="lib")
        self.copy("*.so", dst="./bitprim/lib", src="lib")
        self.copy("*.dll", dst="./bitprim/lib", src="lib")

        # self.copy("*.h", dst="/Users/fernando/fertest", src="include/bitprim")
        # self.copy("*.hpp", dst="/Users/fernando/fertest", src="include/bitprim")
        # self.copy("*.dylib", dst="/Users/fernando/fertest", src="lib")

    # def build(self):
    # def package(self):
    # def package_info(self):
