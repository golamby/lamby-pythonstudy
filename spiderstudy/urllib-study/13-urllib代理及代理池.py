import urllib.request

base_url = 'http://www.baidu.com'

headers_dic = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/100.0.4896.127 Safari/537.36 '
}

proxies_pool = [
    {'http': '118.24.219.151:16817'},
    {'http': '118.24.219.151:2252'}
]
import random

proxies = random.choice(proxies_pool)

request = urllib.request.Request(url=base_url, headers=headers_dic)

handler = urllib.request.ProxyHandler(proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)

content = response.read().decode('utf-8')

with open('../../data/proxy.html',mode='w',encoding='utf-8') as f:
    f.write(content)