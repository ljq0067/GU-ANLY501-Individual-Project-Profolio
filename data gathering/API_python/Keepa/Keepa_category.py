import requests


url = f'https://api.keepa.com/category?key=<Your Keepa API Key>&domain=1&category=0&parents=1'
req = requests.get(url)
with open(f'category.json', 'wb') as f:
    f.write(req.content)


