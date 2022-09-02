# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

def GenericList(methods):
    def fromNative(native, destroy = False):
        arr = []
        n = methods['count'](native)

        # for (let i = 0; i < n; ++i) {
        for i in range(n):
            elementNative = methods['nth'](native, i)
            element = methods['fromNative'](elementNative)
            arr.append(element)

        if destroy:
            methods['destruct'](native)
        return arr

    def toNative(arr):
        native = methods['constructDefault']()
        # for (let i = 0; i < arr.length; ++i) {
        for i in range(len(arr)):
            element = arr[i]
            elementNative = element.toNative()
            methods['pushBack'](native, elementNative)
        return native

    def destruct(native):
        methods['destruct'](native)

    return dict(
        fromNative=fromNative,
        toNative=toNative,
        destruct=destruct
    )
