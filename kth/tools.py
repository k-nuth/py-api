# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.


import functools

##
# Converts a bytearray into a readable format (hex string)
# @param hash (bytearray): Hash bytes
# @return (str) Hex string
# Example: "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
def encode_hash(hash):
    return ''.join('{:02x}'.format(x) for x in hash[::-1])

##
# Converts a string into a workable format (byte array)
# @param hash_str (str): hash hex string
# @return (bytearray): Byte array representing hash. Example "00 00 00 00 00 19 D6 68 ... E2 6F"
def decode_hash(hash_str):
    h = bytearray.fromhex(hash_str)
    h = h[::-1]
    return bytes(h)

def hex_str_to_bytes(hexstr):
    # h = bytearray.fromhex(hexstr)
    # return bytes(h)
    h = bytes.fromhex(hexstr)
    return h

def bytes_to_hex_str(hash):
    return ''.join('{:02x}'.format(x) for x in hash)

@functools.cache
def nullHash():
    return decode_hash('0000000000000000000000000000000000000000000000000000000000000000')

def toSatoshisFactor():
    return 100000000

def toSatoshis(amount):
    return amount * toSatoshisFactor()

def fromSatoshis(satoshis):
    return satoshis / toSatoshisFactor()
