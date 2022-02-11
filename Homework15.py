import threading
import json
import requests


class MyHome():
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = {}

    def __json_read(self):
        with open(self.file_name, "r") as js:
            for k, v in json.load(js).items():
                self.data[k] = v

    def __photo_download(self):
        for k, v in self.data.items():
            image = requests.get(v)
            if image.status_code == 200:
                if v.endswith(".jpg") or v.endswith(".jpeg"):
                    with open(k + ".jpg", "wb") as ph:
                        ph.write(image.content)
                elif v.endswith(".png"):
                    with open(k + ".png", "wb") as pg:
                        pg.write(image.content)
                else:
                    raise ValueError("Unknown format")

    def download(self):
        first = threading.Thread(target=self.__json_read())
        second = threading.Thread(target=self.__photo_download())
        first.start()
        second.start()
        return "Download complete"


if __name__ == "__main__":
    req = MyHome("me_json.json")
    print(req.download())
