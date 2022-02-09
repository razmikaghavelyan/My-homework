import json
import requests


class JsonReader:
    def __init__(self):
        self.image_list = []

    def json_to_list(self, json_file):
        with open(json_file, "r") as js:
            for k, v in json.load(js).items():
                self.image_list.append(v)

    def download_jpeg(self):
        if len(self.image_list) == 0:
            raise ValueError("At first call json_to_list function")

        for i in self.image_list:
            if i.endswith(".jpeg") or i.endswith(".jpg"):
                image = requests.get(i)
                with open(i.split("/")[-1], "wb") as jp:
                    jp.write(image.content)
        return "Download complete"

    def download_png(self):
        if len(self.image_list) == 0:
            raise ValueError("At first call json_to_list function")
        for i in self.image_list:
            if i.endswith(".png"):
                image = requests.get(i)
                with open(i.split("/")[-1], "wb") as pn:
                    pn.write(image.content)
        return "Download complete"


req = JsonReader()

req.json_to_list("me_json.json")
print(req.download_jpeg())
print(req.download_png())
