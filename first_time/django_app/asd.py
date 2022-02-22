import json

with open("django.json", "r") as we:
   res = json.load(we)

print(res)