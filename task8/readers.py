import hazelcast
import argparse
import time

parser = argparse.ArgumentParser(description="Hazelcast Queue Reader")
parser.add_argument("--cluster_member", type=str, required=True, help="IP of cluster member")
args = parser.parse_args()

client = hazelcast.HazelcastClient(cluster_members=[args.cluster_member], cluster_name="apz_second_hm")
queue = client.get_queue("ten-bounded-version-queue").blocking()

def reading():
    counter = 0

    while counter < 50:
        head = queue.take() 
        print(f"[client read {args.cluster_member}] read value {head}")
        counter += 1
    
    print(f"Totally [client read {args.cluster_member}] read {counter} values")
            

if __name__ == "__main__":
    reading()

    time.sleep(1)
    print("Done reading")
    client.shutdown()
