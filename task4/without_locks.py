import hazelcast
import argparse


def incrementing_without(map):
    map.put_if_absent(f"key", 0)
    
    for _ in range(10_000):
        value = map.get("key")
        value+=1
        map.put("key", value)

    
if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Hazelcast Client")
    parser.add_argument("--cluster_member", type=str, required=True, help="IP of cluster member")

    args = parser.parse_args()
    client = hazelcast.HazelcastClient(cluster_members=[args.cluster_member], cluster_name="apz_second_hm")
    distributed_map = client.get_map("test_maps").blocking()

    incrementing_without(distributed_map)
