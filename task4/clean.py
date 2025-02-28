import hazelcast

client = hazelcast.HazelcastClient(cluster_name="apz_second_hm")

new_map = client.get_map("test_maps").blocking()

new_map.remove("key")