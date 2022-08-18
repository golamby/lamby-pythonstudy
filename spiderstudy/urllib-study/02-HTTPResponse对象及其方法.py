import urllib.request

url = r'http://www.baidu.com'

response = urllib.request.urlopen(url)

# <class 'http.client.HTTPResponse'>
print(type(response))

# read方法读取字节，使用decode转为unicode字符串,注意使用read之后，就读到了文件尾，再读就读不到数据了
# content = response.read().decode('utf-8')

# res = response.readline()
# print(res)

# res = response.readlines()
# print(res, len(res))

res = response.getcode()

res = response.geturl()

res = response.getheaders()

