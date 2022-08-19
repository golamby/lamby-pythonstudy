import urllib.request

url = r'http://www.baidu.com'
# url的组成，协议，主机，端口，路径，参数，锚点

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/100.0.4896.127 Safari/537.36 '
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)
