import urllib.request
import urllib.parse

base_url = r'https://www.baidu.com/s?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/100.0.4896.127 Safari/537.36 '
}

# # 将中文编码
# name = urllib.parse.quote('周杰伦')
# print(name)

data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾省'
}

url_data = urllib.parse.urlencode(data)

print(url_data)

url = base_url + url_data
print(url)
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
content = response.read().decode('utf-8')

print(content)
