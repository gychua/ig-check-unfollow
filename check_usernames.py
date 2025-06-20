import json

# Read followers from followers_1.json
with open("followers_1.json") as f:
    followers_data = json.load(f)
    followers = set()
    for entry in followers_data:
        for sld in entry.get("string_list_data", []):
            followers.add(sld["value"].lower())

# Read following from following.json
with open("following.json") as f:
    following_data = json.load(f)["relationships_following"]
    following = set()
    for entry in following_data:
        for sld in entry.get("string_list_data", []):
            following.add(sld["value"].lower())

not_following_back = following - followers

with open("output.html", "w") as out:
    out.write("<html><body><h2>Instagram: Users You Follow Who Don't Follow You Back</h2><ul>\n")
    for username in sorted(not_following_back):
        url = f"https://instagram.com/{username}"
        out.write(f'<li><a href="{url}" target="_blank">{username}</a></li>\n')
    out.write("</ul></body></html>\n")

print("Done! See output.html for results.")
