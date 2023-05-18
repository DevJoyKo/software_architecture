# 추상화?
# 행동을 추상화 하여 캡슐화 한다.
# 코드를 데이터나 알고리즘이 아니라 행동을 중심으로.

# urllib
import json
from urllib.request import urlopen
from urllib.parse import urlencode

params = dict(q='Sausages', format='json')
handle = urlopen('http://api.duckduckgo.com' +"?" + urlencode(params))
raw_text = handle.read().decode('utf8')

parsed = json.loads(raw_text)

results = parsed["RelatedTopics"]
print("urllib use------------")
for r in results:
    if 'Text' in r:
        print(r['FirstURL'] + '-' + r["Text"])

print("=======================================")

# requests
import requests

params = dict(q="Sausages", format="json")
parsed = requests.get("http://api.duckduckgo.com/", params=params).json()

results = parsed["RelatedTopics"]
print("requests use------------")
for r in results:
    if 'Text' in r:
        print(r["FirstURL"] + ' - ' + r['Text'])

print("=======================================")
#duckduckgo
import duckduckgo
print("duckduckgo use------------")
for r in duckduckgo.query('Sausages').results:
    print(r.url + " - " + r.text)