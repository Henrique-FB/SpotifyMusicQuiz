import re

fields = "id, images, name, tracks(next, items(track(name, id, artists(name, id))))"
sub_fields = re.search(r'.*tracks\((.*)\)', fields).group(1)

print(sub_fields)