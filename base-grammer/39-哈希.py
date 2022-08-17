import hashlib

h1 = hashlib.md5()
h1.update('aaa'.encode('utf-8'))
h1.update('bbb'.encode('utf-8'))

res = h1.hexdigest()  # aaabbb

print(res)

import os

path = r'D:\桌面\python-3.7.3.exe'

filelen = os.path.getsize(path)
print(filelen)

# https://registry.npmmirror.com/binary.html,淘宝的镜像网站


# 大型文件的完整性校验

m = hashlib.md5()

with open(path, 'rb') as f:
    f.seek(2, 0)
    pos = f.tell()
    print(pos)

    one_length = filelen // 10
    for i in range(10):
        f.seek(one_length * i, 0)
        res = f.read(100)
        m.update(res)
    print(m.hexdigest())

# 密码加盐

m = hashlib.md5()

pwd = 'h1h1h1*'

m.update('heloo'.encode('utf-8'))
m.update(pwd.encode('utf-8'))
m.update('worlld'.encode('utf-8'))

print(m.hexdigest())
