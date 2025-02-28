import hazelcast
import json

client = hazelcast.HazelcastClient(cluster_name="apz_second_hm")

new_map = client.get_map("distributed_example").blocking()

with open("uk.json", "r", encoding="utf-8") as file:
    data = json.load(file)

english_words = [word["englishWord"] for word in data["words"]]

for i in range(0, 1000):
    new_map.set(str(i),english_words[i])

