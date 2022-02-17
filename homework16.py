import requests

quotes_giver = "https://zenquotes.io/api/random"


class Quotes():
    def __init__(self, url):
        self.url = url

    def quotes_maker(self, amount):
        for i in range(amount):
            res = requests.get(quotes_giver)
            data = res.json()[0]

            with open("text.txt", "a") as qu:
                for k, v in data.items():
                    if not v.startswith("<") and not v.endswith(">"):
                        qu.write(str(v) + "\n")
                qu.write("________" + "\n")


res = Quotes(quotes_giver)
print(res.quotes_maker(5))
