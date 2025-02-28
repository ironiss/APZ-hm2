import subprocess
import time
import argparse

parser = argparse.ArgumentParser(description="Tests")
parser.add_argument("--test_type", type=str, required=True, help="Name of the Python script to run")
args = parser.parse_args()


cluster_members = ["127.0.0.1:5701", "127.0.0.1:5702", "127.0.0.1:5703"]

start_time = time.time()

processes = [
    subprocess.Popen(["python3", args.test_type, "--cluster_member", cluster_members[0]]),
    subprocess.Popen(["python3", args.test_type, "--cluster_member", cluster_members[1]]),
    subprocess.Popen(["python3", args.test_type, "--cluster_member", cluster_members[2]]),
]

for p in processes:
    p.wait()

end_time = time.time()

total_time = end_time - start_time
print(f"Total time: {total_time:.4f} seconds")