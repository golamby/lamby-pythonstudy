import urllib.request

base_url = 'http://www.baidu.com'

headers_dic = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/100.0.4896.127 Safari/537.36 '
}

request = urllib.request.Request(url=base_url, headers=headers_dic)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

from lxml import etree

tree = etree.HTML(content)

res = tree.xpath('//*[@id="su"]/@value')[0]
print(res)
