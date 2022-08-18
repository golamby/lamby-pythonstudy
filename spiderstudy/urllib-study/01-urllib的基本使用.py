import urllib.request

# urllib使用的基本过程
url = r'http://www.baidu.com'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

print(content)
