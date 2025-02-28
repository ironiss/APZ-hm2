import subprocess

cluster_members = ["127.0.0.1:5701", "127.0.0.1:5702", "127.0.0.1:5703"]

writer = subprocess.Popen(["python3", "writer.py", "--cluster_member", cluster_members[0]])

reader = [
    subprocess.Popen(["python3", "readers.py", "--cluster_member", cluster_members[1]]),
    subprocess.Popen(["python3", "readers.py", "--cluster_member", cluster_members[2]]),
]

writer.wait()
for p in reader:
    p.wait()

print("The whole testing is done!")
