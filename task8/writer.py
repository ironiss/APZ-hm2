import hazelcast
import argparse
import time


parser = argparse.ArgumentParser(description="Hazelcast Queue Writer")
parser.add_argument("--cluster_member", type=str, required=True, help="IP of cluster member")
args = parser.parse_args()

client = hazelcast.HazelcastClient(cluster_members=[args.cluster_member], cluster_name="apz_second_hm")
queue = client.get_queue("ten-bounded-version-queue").blocking()


def writing():
    retiries = 0

    for i in range(1, 101):
        while not queue.offer(str(i), timeout=1):
            print(f"Full queue, retrying in 2 seconds (Total Tetries {retiries})")
            retiries += 1
            time.sleep(2)

        print(f"[client write {args.cluster_member}] added value {i}")

if __name__ == "__main__":
    writing()

    print("Done writing")
    client.shutdown()
