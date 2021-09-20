import requests
import json


url = f'https://api.keepa.com/query?domain=1&key=<Your Keepa API Key>'
queryJSON = {
    "page": 10,
    "perPage": 900,
    "singleVariation": False,
    "productType": 0,
    "isSNS": False
}
queryJSON = json.dumps(queryJSON)
req = requests.post(url, data=queryJSON)
with open(f'product.json', 'wb') as f:
    f.write(req.content)




