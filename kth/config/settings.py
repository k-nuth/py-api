# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import kth_native as nat

def getDefault(network):
    return nat.config_settings_default(int(network))

def getFromFile(file):
    return nat.config_settings_get_from_file(file)
