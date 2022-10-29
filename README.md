# Python API

> Bitcoin Cash full node as a Python library

[![PyPi Version](https://img.shields.io/pypi/v/kth?logo=npm&style=for-the-badge)](https://pypi.org/project/kth/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAHYcAAB2HAY%2Fl8WUAAAAZdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuMTCtCgrAAAADB0lEQVR4XtWagXETMRREUwIlUAIlUAodQAl0AJ1AB9BB6AA6gA6MduKbkX%2BevKecNk525jHO3l%2Fp686xlJC70%2Bl0C942vjV%2Bn9FreVQbBc0wWujfRpW8Z78JaIb53hhJ1ygTA80w9PQ36duBMjHQHPCuoQZfutSjeqU1PAJN4E3j2pN7aVKv6pnWcgGawNfGa5N6prVcgGZBn8yvVXZXQbOgPXokXaPMNZwoc41D%2FaHZ8b7hpBrKjnCizIjD%2FaHZ8aPR6%2BeZXqqh7Agnyow43B%2BaZz40qnQ36a6rlsYgnChDLOkPzTN1z%2B9PafU0N3OAcaIMsaQ%2FNBufG1X9JyrtDMr0Y4xwokxlWX%2BPjAYdemhPrWeDvYcPJ8r0LO3v4oszNfivQQuTp2u9qJGKE2V6lvZ38UVj9q3t3oqEE2U2lvfXF4t6qPjTqDUV1fRyhw8nymws768vfOr2NtqOqFY4UUZE%2BusL6VDRX7%2FGzOHDiTIi0t9WMPsUKzNPx4kysf62gmuHir3sPXw4USbWny485ZOc2PsJ7VTro%2F3pwp5DxV7qHq2xa41TrY%2F2J7PfJkaHir3UwwdtU061PtqfTP0CUaYm2v3LxCtoDI2lMWk8p1of7Y8K0jhRJgaaYZwoE0P%2FpFUndZqtP6T4BE2zC5qtP6T4BE2zC5qtPyRN8OvhZUQae3ZBtT7anyb49PA6Ivp5wKnWR%2FvbJkncZXr6wokysf62CXRCWjmJxhqd2JwoE%2BuvTqS37JGJlB39GLzhRJmN5f31gz8XTpSJgWYYJ8rEQDOME2VioBnGiTIx0AzjRJkYaIZxokwMNMM4USYGmmGcKBMDzTBOlImBZhgnysRAM4wTZWKgGcaJMjHQDONEmRhohnGiTAw0wzhRJgaaYZwoEwPNME6UiYFmGCfKxEAzjBNlYqAZxokyMdAMoL%2FO%2BNi4bzjpT1e%2BNFb8V7gFzUXMLHqk%2BM1A8wArFj1S5GagOUly0SMtuxloTnJrUU%2B7QXOSW4t62g2ak9xa1NNu0Jzk1qKednK6%2Bw9roIB8keT%2F3QAAAABJRU5ErkJggg%3D%3D)](LICENSE.md)
[![py-standard-style](https://img.shields.io/badge/python-standard%20code%20style-green.svg?style=for-the-badge)](https://github.com/feross/standard)
<a target="_blank" href="https://t.me/knuth_cash">![Telegram][badge.telegram]</a>

<p align="center"><img width="800px" src="https://raw.githubusercontent.com/k-nuth/py-api/master/misc/kth-py.jpeg" /></p>

[Knuth Python API](https://pypi.org/project/kth/) is a high performance implementation of the Bitcoin Cash protocol focused on users requiring extra performance and flexibility. It is a Bitcoin Cash node you can use as a library.

## Getting started with Python

1. Create a new Python console project:
```
$ mkdir HelloKnuth
$ cd HelloKnuth
```

2. Add a reference to our Python API package:

```
$ pip install kth
```

3. Create a new file called `index.py` and write some code:

```Python
import kth
import signal
import asyncio

running_ = False

def shutdown(sig, frame):
    global running_
    print('Graceful shutdown ...')
    running_ = False

async def main():
    global running_
    signal.signal(signal.SIGINT, shutdown)
    config = kth.config.getDefault(kth.config.Network.mainnet)

    with kth.node.Node(config, True) as node:
        await node.launch(kth.primitives.StartModules.all)
        print("Knuth node has been launched.")
        running_ = True

        (_, height) = await node.chain.getLastHeight()
        print(f"Current height in local copy: {height}")

        if await comeBackAfterTheBCHHardFork(node):
            print("Bitcoin Cash has been created!")

        # node.close()
        print("Good bye!")

async def comeBackAfterTheBCHHardFork(node):
    hfHeight = 478559
    while running_:
        (_, height) = await node.chain.getLastHeight()
        if height >= hfHeight:
            return True
        await asyncio.sleep(10)

    return False

asyncio.run(main())

```

4. Enjoy Knuth node as a Python library:

```
$ python index.py
```



## Issues

Each of our modules has its own Github repository, but in case you want to create an issue, please do so in our [main repository](https://github.com/k-nuth/kth/issues).


<!-- Links -->
[badge.Travis]: https://travis-ci.org/k-nuth/py-api.svg?branch=master
<!-- [badge.Appveyor]: https://ci.appveyor.com/api/projects/status/github/k-nuth/py-api?svg=true&branch=master -->
[badge.Appveyor]: https://img.shields.io/appveyor/ci/Knuth/py-api.svg?style=for-the-badge&label=build&logo=appveyor&logoColor=white
[badge.Cirrus]: https://api.cirrus-ci.com/github/k-nuth/py-api.svg?branch=master
[badge.version]: https://badge.fury.io/gh/k-nuth%2Fkth-py-api.svg
[badge.release]: https://img.shields.io/github/release/k-nuth/py-api.svg
[badge.c]: https://img.shields.io/badge/C-11-blue.svg?style=flat&logo=c
[badge.telegram]: https://img.shields.io/badge/telegram-badge-blue.svg?logo=telegram&style=for-the-badge
[badge.slack]: https://img.shields.io/badge/slack-badge-orange.svg?logo=slack&style=for-the-badge



<!-- [![Downloads](https://img.shields.io/nuget/dt/kth-bch.svg?style=for-the-badge&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAHYcAAB2HAY%2Fl8WUAAAAZdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuMTnU1rJkAAABrUlEQVR4XuXQQW7DMAxE0Rw1R%2BtN3XAjBOpPaptfsgkN8DazIDB8bNu2NCxXguVKsFwJlrJs6KYGS1k2dFODpSwbuqnBUpYN3dRgKcuGbmqwlGVDNzVYyrKhmxosZdnQTQ2WsmzopgZLWTZ0U4OlLBu6qcFSlg3d1GApy4ZuarCUZUM3NVjKsqGbGixl2dBNDZaybOimBktZNnRTg6UsG7qpwVKWDd3UYPnB86VKfl5owx9YflHhCbvHByz%2FcecnHBofsNzhjk84PD5gudOdnnBqfMDygDs84fT4gOVBVz4hNT5gecIVT0iPD1ieNPMJyviAZcKMJ2jjA5ZJI5%2Bgjg9YCkY8QR8fsJSYTxgyPmApMp4wbHzAUpZ5wtDxAcsBzjxh%2BPiA5SBHnjBlfMByoD1PmDY%2BYDnYtydMHR%2BwnICeMH18wHKS9ydcMj5gOVE84bLxAcuVYLkSLDvVQ5saLDvVQ5saLDvVQ5saLDvVQ5saLDvVQ5saLDvVQ5saLDvVQ5saLDvVQ5saLDvVQ5saLDvVQ5saLDvVQ5saLDvVQ5saLFeC5UqwXAmW69gev7WIMc4gs9idAAAAAElFTkSuQmCC)](https://www.nuget.org/packages/kth-bch/)
-->

<!-- [![Latest Pre-Release](https://img.shields.io/nuget/vpre/kth-bch?logo=nuget&color=yellow&label=pre-release&style=for-the-badge)](https://www.nuget.org/packages/kth-bch/absoluteLatest) -->
