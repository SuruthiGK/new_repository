import requests
import json

print ('#'*30)
print ("Most popular Videos on yotube")
print ('#'*30)

r=requests.get("http://gdata.youtube.com/feeds/api/standardfeeds/top_rated?v=2&alt=jsonc")
r.text
data=json.loads(r.text)
for item in data['data']['items']:
	print (item['title'])