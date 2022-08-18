import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

import json

with open('../../data/douban1.json', mode='wt', encoding='utf-8') as f:
    f.write(content)

with open('../../data/douban1.json', mode='rt', encoding='utf-8') as f:
    res = json.load(f)

print(res[0])