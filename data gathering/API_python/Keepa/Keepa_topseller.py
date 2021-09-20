import requests


def get_data():
    url = f'https://api.keepa.com/topseller?key=<Your Keepa API Key>&domain=1'
    req = requests.get(url)
    with open(f'topseller.json', 'wb') as f:
        f.write(req.content)


get_data()
