import requests

quotes_giver = "https://zenquotes.io/api/random"


class Quotes():
    def __init__(self, url):
        self.url = url
        self.list_of_quotes = []

    def quotes_maker(self):
        res = requests.get(quotes_giver)

        data = res.json()
        list_of_quotes = []
        list_of_quotes.append((dict(data[0]).get("q"), dict(data[0]).get("a")))

        with open("text.txt", "a") as qu:
            qu.write(str(self.list_of_quotes))

        return list_of_quotes


res = Quotes(quotes_giver)
print(res.quotes_maker())
