# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import kth

def hash_to_hex(hash):
    hash_hex = ''.join('{:02x}'.format(x) for x in hash[::-1])
    return hash_hex

def test_default_mainnet_settings():
    setts = kth.config.getDefault(kth.config.Network.mainnet)

    assert setts.chain.cores == 0
    assert setts.chain.priority == True
    assert setts.chain.byte_fee_satoshis >= 0.1
    assert setts.chain.byte_fee_satoshis <= 0.11
    assert setts.chain.sigop_fee_satoshis == 100.0
    assert setts.chain.minimum_output_satoshis == 500
    assert setts.chain.notify_limit_hours == 24
    assert setts.chain.reorganization_limit == 256
    assert len(setts.chain.checkpoints) == 64
    assert setts.chain.checkpoints[0].height == 0
    assert hash_to_hex(setts.chain.checkpoints[0].hash) == "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
    assert setts.chain.fix_checkpoints == True
    assert setts.chain.allow_collisions == True
    assert setts.chain.easy_blocks == False
    assert setts.chain.retarget == True
    assert setts.chain.bip16 == True
    assert setts.chain.bip30 == True
    assert setts.chain.bip34 == True
    assert setts.chain.bip66 == True
    assert setts.chain.bip65 == True
    assert setts.chain.bip90 == True
    assert setts.chain.bip68 == True
    assert setts.chain.bip112 == True
    assert setts.chain.bip113 == True
    assert setts.chain.bch_uahf == True
    assert setts.chain.bch_daa_cw144 == True
    assert setts.chain.bch_pythagoras == True
    assert setts.chain.bch_euclid == True
    assert setts.chain.bch_pisano == True
    assert setts.chain.bch_mersenne == True
    assert setts.chain.bch_fermat == True
    assert setts.chain.bch_euler == True
    # assert setts.chain.bch_gauss == False
    assert setts.chain.gauss_activation_time == 1652616000
    assert setts.chain.descartes_activation_time == 1684152000
    assert setts.chain.asert_half_life == 2 * 24 * 60 * 60 #two days
    #  ------------------------------------------------------------------------------------
    assert setts.database.directory == 'blockchain'
    assert setts.database.flush_writes == False
    assert setts.database.file_growth_rate == 50
    assert setts.database.index_start_height == 0
    assert setts.database.reorg_pool_limit == 100
    assert setts.database.db_max_size == 600 * 1024 * 1024 * 1024
    assert setts.database.safe_mode == True
    assert setts.database.cache_capacity == 0
    # ------------------------------------------------------------------------------------
    assert setts.network.threads == 0
    assert setts.network.protocol_maximum == 70015
    assert setts.network.protocol_minimum == 31402
    assert setts.network.services == 1
    assert setts.network.invalid_services == 0
    assert setts.network.relay_transactions == True
    assert setts.network.validate_checksum == False

    assert setts.network.identifier == 3908297187

    assert setts.network.inbound_port == 8333
    assert setts.network.inbound_connections == 0
    assert setts.network.outbound_connections == 8
    assert setts.network.manual_attempt_limit == 0
    assert setts.network.connect_batch_size == 5
    assert setts.network.connect_timeout_seconds == 5
    assert setts.network.channel_handshake_seconds == 6000
    assert setts.network.channel_heartbeat_minutes == 5
    assert setts.network.channel_inactivity_minutes == 10
    assert setts.network.channel_expiration_minutes == 60
    assert setts.network.channel_germination_seconds == 30
    assert setts.network.host_pool_capacity == 1000
    assert setts.network.hosts_file == 'hosts.cache'
    # assert setts.network.self.ip == '0.0.0.0'
    assert setts.network.self.port == 0
    assert len(setts.network.blacklist) == 0
    assert len(setts.network.peers) == 0
    assert len(setts.network.seeds) == 6
    assert setts.network.seeds[0].scheme == ''
    assert setts.network.seeds[0].host == 'seed.flowee.cash'
    assert setts.network.seeds[0].port == 8333
    assert setts.network.debug_file == 'debug.log'
    assert setts.network.error_file == 'error.log'
    assert setts.network.archive_directory == 'archive'
    assert setts.network.rotation_size == 0
    assert setts.network.minimum_free_space == 0
    assert setts.network.maximum_archive_size == 0
    assert setts.network.maximum_archive_files == 0

    # _expected: "0.0.0.0"
    # _received: "[::ffff:0:0]"
    # assert setts.network.statistics_server.ip == '0.0.0.0'

    assert setts.network.statistics_server.port == 0
    assert setts.network.verbose == False
    assert setts.network.use_ipv6 == True
    assert len(setts.network.user_agent_blacklist) == 1
    assert setts.network.user_agent_blacklist[0] == '/Bitcoin SV:'
    # ------------------------------------------------------------------------------------
    assert setts.node.sync_peers == 0
    assert setts.node.sync_timeout_seconds == 5
    assert setts.node.block_latency_seconds == 60
    assert setts.node.refresh_transactions == True
    assert setts.node.compact_blocks_high_bandwidth == True

def test_default_testnet4_settings():
    setts = kth.config.getDefault(kth.config.Network.testnet4)

    assert setts.chain.cores == 0
    assert setts.chain.priority == True
    assert setts.chain.byte_fee_satoshis >= 0.1
    assert setts.chain.byte_fee_satoshis <= 0.11
    assert setts.chain.sigop_fee_satoshis == 100.0
    assert setts.chain.minimum_output_satoshis == 500
    assert setts.chain.notify_limit_hours == 24
    assert setts.chain.reorganization_limit == 256
    assert len(setts.chain.checkpoints) == 18
    assert setts.chain.checkpoints[0].height == 0
    assert hash_to_hex(setts.chain.checkpoints[0].hash) == "000000001dd410c49a788668ce26751718cc797474d3152a5fc073dd44fd9f7b"
    assert setts.chain.fix_checkpoints == True
    assert setts.chain.allow_collisions == True
    assert setts.chain.easy_blocks == True
    assert setts.chain.retarget == True
    assert setts.chain.bip16 == True
    assert setts.chain.bip30 == True
    assert setts.chain.bip34 == True
    assert setts.chain.bip66 == True
    assert setts.chain.bip65 == True
    assert setts.chain.bip90 == True
    assert setts.chain.bip68 == True
    assert setts.chain.bip112 == True
    assert setts.chain.bip113 == True
    assert setts.chain.bch_uahf == True
    assert setts.chain.bch_daa_cw144 == True
    assert setts.chain.bch_pythagoras == True
    assert setts.chain.bch_euclid == True
    assert setts.chain.bch_pisano == True
    assert setts.chain.bch_mersenne == True
    assert setts.chain.bch_fermat == True
    assert setts.chain.bch_euler == True
    # assert setts.chain.bch_gauss == False
    assert setts.chain.gauss_activation_time == 1652616000
    assert setts.chain.descartes_activation_time == 1684152000
    assert setts.chain.asert_half_life == 60 * 60 # one hour
    # ------------------------------------------------------------------------------------
    assert setts.database.directory == 'blockchain'
    assert setts.database.flush_writes == False
    assert setts.database.file_growth_rate == 50
    assert setts.database.index_start_height == 0
    assert setts.database.reorg_pool_limit == 100
    assert setts.database.db_max_size == 20 * 1024 * 1024 * 1024 # 20 _gi_b
    assert setts.database.safe_mode == True
    assert setts.database.cache_capacity == 0
    # ------------------------------------------------------------------------------------
    assert setts.network.threads == 0
    assert setts.network.protocol_maximum == 70015
    assert setts.network.protocol_minimum == 31402
    assert setts.network.services == 1
    assert setts.network.invalid_services == 0
    assert setts.network.relay_transactions == True
    assert setts.network.validate_checksum == False

    assert setts.network.identifier == 2950346722

    assert setts.network.inbound_port == 28333
    assert setts.network.inbound_connections == 0
    assert setts.network.outbound_connections == 8
    assert setts.network.manual_attempt_limit == 0
    assert setts.network.connect_batch_size == 5
    assert setts.network.connect_timeout_seconds == 5
    assert setts.network.channel_handshake_seconds == 6000
    assert setts.network.channel_heartbeat_minutes == 5
    assert setts.network.channel_inactivity_minutes == 10
    assert setts.network.channel_expiration_minutes == 60
    assert setts.network.channel_germination_seconds == 30
    assert setts.network.host_pool_capacity == 1000
    assert setts.network.hosts_file == 'hosts.cache'
    # assert setts.network.self.ip == '0.0.0.0'
    assert setts.network.self.port == 0
    assert len(setts.network.blacklist) == 0
    assert len(setts.network.peers) == 0
    assert len(setts.network.seeds) == 3
    assert setts.network.seeds[0].scheme == ''
    assert setts.network.seeds[0].host == 'testnet4-seed-bch.bitcoinforks.org'
    assert setts.network.seeds[0].port == 28333
    assert setts.network.debug_file == 'debug.log'
    assert setts.network.error_file == 'error.log'
    assert setts.network.archive_directory == 'archive'
    assert setts.network.rotation_size == 0
    assert setts.network.minimum_free_space == 0
    assert setts.network.maximum_archive_size == 0
    assert setts.network.maximum_archive_files == 0

    # _expected: "0.0.0.0"
    # _received: "[::ffff:0:0]"
    # assert setts.network.statistics_server.ip == '0.0.0.0'

    assert setts.network.statistics_server.port == 0
    assert setts.network.verbose == False
    assert setts.network.use_ipv6 == True
    assert len(setts.network.user_agent_blacklist) == 1
    assert setts.network.user_agent_blacklist[0] == '/Bitcoin SV:'
    # ------------------------------------------------------------------------------------
    assert setts.node.sync_peers == 0
    assert setts.node.sync_timeout_seconds == 5
    assert setts.node.block_latency_seconds == 60
    assert setts.node.refresh_transactions == True
    assert setts.node.compact_blocks_high_bandwidth == True
