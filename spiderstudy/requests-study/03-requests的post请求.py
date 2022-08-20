import json

import requests

url = r'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/100.0.4896.127 Safari/537.36 '
}

data_dic = {
    'kw': 'spider'
}

proxy = {
    'http': ''
}
# application/x-www-form-urlencoded; charset=UTF-8,决定了参数data/json
# requests的post方法
# 不需要定制Request对象
# 不需要参数的编解码
# 请求参数是data 或 json

resp = requests.post(url=url, data=data_dic, headers=headers, )  # proxies=proxy

content = resp.json()
print(content, type(content))

content = resp.text
print(content)
content = resp.content
print(content)
res_obj = json.loads(content)
print(res_obj)
