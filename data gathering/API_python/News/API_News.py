# API Exercise with Python
import requests
import json
import csv

# use NewsAPI to find news related to Amazon
BaseURL1 = "https://newsapi.org/v2/everything?q=Amazon&apiKey=237d79255be746ca8b2a73cddddac68f"
URLPost1 = {' API_KEY ': ' 237d79255be746ca8b2a73cddddac68f ',
            ' sortBy ': ' top ',
            ' format ': ' application/json '}
# print(URLPost1)
response1 = requests.get(BaseURL1, URLPost1)
# print(response1)
jsontxt = response1.json()

# use json
t1 = requests.get(BaseURL1, URLPost1)
json_data1 = json.loads(t1.text)
json.dumps(json_data1, indent=4)

# write in files
f = open(' amazon-news.txt ', 'w', newline='')
writer = csv.writer(f)
header = [' published_at ', ' author ', ' title ']
writer.writerow(header)

# select needed data
for series in json_data1["articles"]:
    print(series["publishedAt"], " ", series["author"], " ", series["title"])
    published_at = series["publishedAt"]
    author = series["author"]
    title = series["title"]
    row = [published_at, author, title]
    writer.writerow(row)

# close the file
f.close()


