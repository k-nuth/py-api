# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import kth_native as bn
import sys
import time

##
# Represents a binary filter
class Binary:
    def __init__(self, ptr):
        ##
        # @private
        self._ptr = ptr

    ##
    # Create an empty binary object
    # @return (Binary) New instance
    @classmethod
    def construct(self):
        return Binary(bn.binary_construct())


    ##
    # Creates a binary filter from a binary string
    # @param string_filter Binary string. Example: '10111010101011011111000000001101'
    # @return (Binary) Instance representing the given filter string
    @classmethod
    def construct_string(self, string_filter):
        return Binary(bn.binary_construct_string(string_filter))

    ##
    # Creates a binary filter from an int array
    # @param size (int) Filter length
    # @param blocks (int array) Filter representation. Example: '[186,173,240,13]'
    # @return (Binary) Instance representing the given filter
    @classmethod
    def construct_blocks(self, size, blocks):
        return Binary(bn.binary_construct_blocks(size, len(blocks), blocks))

    ##
    # Filter representation as uint array
    # @return (uint array)
    def blocks(self):
        return bn.binary_blocks(self._ptr)

    ##
    # Filter representation as binary string
    # @return (str)
    def encoded(self):
        return bn.binary_encoded(self._ptr)
