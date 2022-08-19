import requests

url = r'https://www.baidu.com'

resp = requests.get(url=url)

# 一个类型和六个属性
print(type(resp))  # <class 'requests.models.Response'>

resp.encoding = 'utf-8'

# 以字符串的形式返回响应的结果
print(resp.text)
print(resp.url)  # 请求地址
print(resp.status_code)  # 状态码
print(resp.content)  # 以字节形式返回信息
print(resp.headers)  # 响应头信息
