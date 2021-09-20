import requests
import json

with open('asin.json', 'r') as load_f:
    amazon_id = json.load(load_f)
asinList = amazon_id['asinList']
asinStr = ','.join(asinList).replace(' [ ', ' ').replace(' ] ', ' ')
ASIN = asinStr[241241:242241]
print(len(ASIN))

# March 19 — California Issues Statewide Stay-at-Home Order
url = f'https://api.keepa.com/product?key=7shsdsmam3tg745bicbo6eek3l0h9hf0a7i06a1otjpsb05d188kslln8h0jtsds&domain=1&asin={ASIN}&stat=2020-03-19,2022-01-01&history=1'
req = requests.post(url)
with open(f'product/product241.json', 'wb') as f:
    f.write(req.content)
