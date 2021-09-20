import requests
import json

url = f'https://api.keepa.com/deal?key=<Your Keepa API Key>'
queryJSON = {
    "page": 65,
    "domainId": 1,
    "priceTypes": [0],
    "salesRankRange": [0, -1],
    "isRangeEnabled": True,
    "isFilterEnabled": False,
    "hasReviews": False,
    "sortType": 3,
    "dateRange": 3}
queryJSON = json.dumps(queryJSON)

req = requests.post(url, queryJSON)

with open(f'browsing/browsing65.json', 'wb') as f:
    f.write(req.content)

