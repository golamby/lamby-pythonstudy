import json
import urllib.request
import urllib.parse

url = r'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/100.0.4896.127 Safari/537.36 '
}

data = {
    'kw': 'spider'
}
data = urllib.parse.urlencode(data).encode('utf-8')
print(data)

request = urllib.request.Request(url=url, headers=headers, data=data)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')
print(content)
dic = {}
dic = json.loads(content)

print(dic)
result = dic['data']
for trans in result:
    print(trans['k'],trans['v'])
