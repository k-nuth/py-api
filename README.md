# Bitprim Python-API <a target="_blank" href="http://semver.org">![Version][badge.version]</a> <a target="_blank" href="https://travis-ci.org/bitprim/bitprim-py">![Travis status][badge.Travis]</a> [![Appveyor Status](https://ci.appveyor.com/api/projects/status/github/bitprim/bitprim-py?svg=true&branch=master)](https://ci.appveyor.com/projects/bitprim/bitprim-py) <a target="_blank" href="https://gitter.im/bitprim/Lobby">![Gitter Chat][badge.Gitter]</a>

> Multi-Cryptocurrency _Python_ API.

*Bitprim Python-API* is a library written in the _Python_ which exposes an API that allows you to programmatically access all of the *Bitprim* node features:
  * Wallet
  * Mining
  * Full blockchain
  * Routing

Bitprim Python-API supports the following cryptocurrencies:
  * [Bitcoin Cash](https://www.bitcoincash.org/)
  * [Bitcoin](https://bitcoin.org/)
  * [Litecoin](https://litecoin.org/)

## Installation Requirements

- 64-bit machine.
- Python >= 3.4.x (64-bits) or Python >= 2.7.x (64-bits). Only CPython (reference implementation) is supported. PyPy, Jython, IronPython, ... are not supported for the moment.
- _pip_ package manager.

## Installation Procedure

The *Bitprim Python-API* installation is very easy using the _pip package manager_.

```sh
    $ pip install bitprim
```

This installs the Bitprim Python-API customized for _Bitcoin Cash_ cryptocurrency. If you want to use another currency, you have to specify it in the following way:

```sh
    # For Bitcoin Cash (default)
    $ pip install --install-option="--currency=BCH" bitprim

    # For Bitcoin Lecacy
    $ pip install --install-option="--currency=BTC" bitprim

    # For Litecoin
    $ pip install --install-option="--currency=LTC" bitprim
```

## Building from source Requirements

Bitprim Python-API is a thin library built on top of the Bitprim C-API, therefore it is sometimes necessary to have a C  compiler to use the library.

We have prebuilt binaries for macOS and Windows, so for both macOS and Windows it is not necessary for you to have a C compiler installed.
But, due to limitations of the pip package manager, pre-built binaries for Linux can not be provided, therefore, in Linux it is necessary to compile from source code, and therefore have a C language compiler.

## How to use it

### "Hello, Blockchain!" example:

```python
# hello_blockchain.py

import bitprim
import sys

def main():
    with bitprim.Executor("my_config_file", sys.stdout, sys.stderr) as ex:
        ex.init_chain()
        ex.run_wait()

        def last_height_handler(error, height):
            print(height)

        ex.chain.fetch_last_height(last_height_handler)

if __name__ == '__main__':
    main()
```

### Explanation:

```python
import bitprim
```

Needed to use the Bitprim Python-API features.

```python
with bitprim.Executor("my_config_file", sys.stdout, sys.stderr) as ex:
```

Construct a Bitprim _Executor_ object, which is necessary to run the node, interact with the blockchain, with the P2P peers and other components of the API.  

`"my_config_file"` is the path to the configuration file; in the [bitprim-config](https://github.com/bitprim/bitprim-config) repository you can find some example files.  
If you pass an empty string (`""`), default configuration will be used.

`stdout` and `stderr` are file objects corresponding to the Python interpreter’s standard output and error streams. These are used to tell the Bitprim node where to print the logs.   
You can use any file object, for example, you can make the Bitprim node redirect the logs to a file.  
If you pass `None`, there will be no logging information.

```python
ex.init_chain()
```

Initialize the filesystem database where the Blockchain will be stored.  
You need to have enough disk space to store the full Blockchain.

This is equivalent to executing: `bn -i -c my_config_file`.

```python
ex.run_wait()
```

Run the node.  
In this step, the connections and handshake with the peers will be established, and the initial process of downloading blocks will start. Once this stage has finished, the node will begin to receive transactions and blocks through the P2P network.

This is equivalent to executing: `bn -c my_config_file`.


```python
def last_height_handler(error, height):
    print(height)

ex.chain.fetch_last_height(last_height_handler)
```

Ask the Blockchain what is the height of the last downloaded block and print it in the standard output.
In order to get the _height_ a callback (or handler) have to be passed as a parameter of `fetch_last_height` function.

### Run:

```sh
python hello_blockchain.py
```
... and enjoy the Bitprim's programmable APIs:

## Advanced Installation

Bitprim is a high performance node, so we have some options and pre-built packages tuned for several platforms.
Specifically, you can choose your computer _microarchitecture_ to download a pre-build executable compiled to take advantage of the instructions available in your processor. For example:

```sh
# For Haswell microarchitecture and Bitcoin Cash currency
$ pip install --install-option="--currency=BCH" --install-option="--microarch=haswell" bitprim
```
So, you can manually choose the appropriate microarchitecture, some examples are: _x86_64_, _haswell_, _ivybridge_, _sandybridge_, _bulldozer_, ...  
By default, if you do not specify any, the building system will select a base microarchitecture corresponding to your _Instruction Set Architecture_ (ISA). For example, for _Intel 80x86_, the x86_64 microarchitecture will be selected.

### Automatic Microarchitecture selection

Our build system has the ability to automatically detect the microarchitecture of your processor. To do this, first, you have to install our _pip_ package called [cpuid](https://pypi.python.org/pypi/cpuid). Our build system detects if this package is installed and in such case, makes use of it to detect the best possible executable for your processor.

```sh
$ pip install cpuid
$ pip install bitprim
```

<!-- Links -->
[badge.Appveyor]: https://ci.appveyor.com/api/projects/status/github/bitprim/bitprim-py?svg=true&branch=dev
[badge.Gitter]: https://img.shields.io/badge/gitter-join%20chat-blue.svg
[badge.Travis]: https://travis-ci.org/bitprim/bitprim-py.svg?branch=master
[badge.version]: https://badge.fury.io/gh/bitprim%2Fbitprim-py.svg
