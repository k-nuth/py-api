
REM ----------------------------------------------
REM  Bitprim Python (Windows, MSVC with NMake)
REM  ----------------------------------------------

git clone -b c-api https://github.com/bitprim/secp256k1.git
git clone -b c-api https://github.com/bitprim/bitprim-core.git
git clone -b c-api https://github.com/bitprim/bitprim-consensus.git
git clone -b c-api https://github.com/bitprim/bitprim-database.git
git clone -b c-api https://github.com/bitprim/bitprim-blockchain.git
git clone -b c-api https://github.com/bitprim/bitprim-network.git
git clone -b c-api https://github.com/bitprim/bitprim-node.git
git clone https://github.com/bitprim/bitprim-node-cint.git
    

REM  ----------------------------------------------
    cd secp256k1
    rd /s /q build
    mkdir build
    cd build
    cmake -G "NMake Makefiles" -DENABLE_MODULE_RECOVERY=ON -DENABLE_TESTS=OFF -DCMAKE_BUILD_TYPE=Release ..
    REM cmake -G "NMake Makefiles" -DENABLE_MODULE_RECOVERY=ON -DENABLE_TESTS=OFF  -DCMAKE_BUILD_TYPE=Debug ..
    REM cmake -G "Visual Studio 15 2017 Win64" -DENABLE_MODULE_RECOVERY=ON -DENABLE_TESTS=OFF  -DCMAKE_BUILD_TYPE=Release ..
    REM cmake -G "Visual Studio 15 2017 Win64" -DENABLE_MODULE_RECOVERY=ON -DENABLE_TESTS=OFF  -DCMAKE_BUILD_TYPE=Debug ..

    nmake
    cd ..\..
REM  ----------------------------------------------

REM  ----------------------------------------------
    cd bitprim-core
    rd /s /q build
    mkdir build
    cd build
    cmake -G "NMake Makefiles" -DWITH_TESTS=OFF -DCMAKE_BUILD_TYPE=Release ..
    REM  cmake -G "NMake Makefiles" -DWITH_TESTS=OFF -DCMAKE_BUILD_TYPE=Debug ..

    nmake
    cd ..\..
REM  ----------------------------------------------

REM  ----------------------------------------------
    cd bitprim-consensus
    rd /s /q build
    mkdir build
    cd build
    cmake -G "NMake Makefiles" -DWITH_TESTS=OFF -DCMAKE_BUILD_TYPE=Release ..
    REM  cmake -G "NMake Makefiles" -DWITH_TESTS=OFF -DCMAKE_BUILD_TYPE=Debug ..

    nmake
    cd ..\..
REM  ----------------------------------------------

REM  ----------------------------------------------
    cd bitprim-database
    rd /s /q build
    mkdir build
    cd build
    cmake -G "NMake Makefiles" -DWITH_TESTS=OFF -DCMAKE_BUILD_TYPE=Release ..
    REM  cmake -G "NMake Makefiles" -DWITH_TESTS=OFF -DCMAKE_BUILD_TYPE=Debug ..

    nmake
    cd ..\..
REM  ----------------------------------------------

REM  ----------------------------------------------
    cd bitprim-blockchain
    rd /s /q build
    mkdir build
    cd build
    cmake -G "NMake Makefiles" -DWITH_TESTS=OFF -DCMAKE_BUILD_TYPE=Release ..
    REM  cmake -G "NMake Makefiles" -DWITH_TESTS=OFF -DCMAKE_BUILD_TYPE=Debug ..

    nmake
    cd ..\..
REM  ----------------------------------------------

REM  ----------------------------------------------
    cd bitprim-network
    rd /s /q build
    mkdir build
    cd build
    cmake -G "NMake Makefiles" -DWITH_TESTS=OFF -DCMAKE_BUILD_TYPE=Release ..
    REM  cmake -G "NMake Makefiles" -DWITH_TESTS=OFF -DCMAKE_BUILD_TYPE=Debug ..

    nmake
    cd ..\..
REM  ----------------------------------------------

REM  ----------------------------------------------
    cd bitprim-node
    rd /s /q build
    mkdir build
    cd build
    cmake -G "NMake Makefiles" -DWITH_TESTS=OFF -DCMAKE_BUILD_TYPE=Release ..
    REM  cmake -G "NMake Makefiles" -DWITH_TESTS=OFF -DCMAKE_BUILD_TYPE=Debug ..

    nmake
    cd ..\..
REM  ----------------------------------------------

REM  ----------------------------------------------
    REM  master branch
    cd bitprim-node-cint
    rd /s /q build
    mkdir build
    cd build
    cmake -G "NMake Makefiles" -DWITH_TESTS=OFF -DCMAKE_BUILD_TYPE=Release ..
    REM  cmake -G "NMake Makefiles" -DWITH_TESTS=OFF -DCMAKE_BUILD_TYPE=Debug ..

    nmake
    cd ..\..
REM  ----------------------------------------------