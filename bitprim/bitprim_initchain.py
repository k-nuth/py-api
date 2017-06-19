import sys
import bitprim_native

executor = bitprim_native.construct("/home/fernando/execution_tests/btc_mainnet.cfg", sys.stdin, sys.stdout, sys.stderr)

res = bitprim_native.initchain(executor)

print(res)

bitprim_native.destruct(executor)