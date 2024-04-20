# Python in VS Code

import requests
import json

url = requests.get("https://api.ampifymusic.com/packs")
text = url.text
data = json.loads(text)
genres = []
hiphop_pack_numbers = []
hiphop_packs = []
packs = data["packs"]
for pack in packs:
    for genre in pack["genres"]:
        if genre not in genres:
            genres.append(genre)
        if genre == "hip-hop":
            hiphop_pack_numbers.append(packs.index(pack))
            hiphop_packs.append(pack)
print("\nGenres:\n")
print(genres)
print("\nHip-hop track pack numbers:\n")
print(hiphop_pack_numbers)
print("\nHip-hop track packs:\n")
print(hiphop_packs)