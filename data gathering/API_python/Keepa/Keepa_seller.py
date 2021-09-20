import requests
import json

with open('topseller.json', 'r') as load_f:
    amazon_id = json.load(load_f)
asinList = amazon_id['sellerIdList']
asinStr = ','.join(asinList).replace(' [ ', ' ').replace(' ] ', ' ')
sellerId = asinStr[44253: 45728]
print(len(sellerId))

# March 19 — California Issues Statewide Stay-at-Home Order
url = f'https://api.keepa.com/seller?key=<Your Keepa API Key>&domain=1&seller={sellerId}'
req = requests.post(url)
with open(f'seller/seller29.json', 'wb') as f:
    f.write(req.content)
