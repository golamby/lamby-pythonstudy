# 字符编码：文件头  '' 指定文件的读格式也就是解码格式为gbk
# coding：gbk


# 编码字符集
# Unicode（万国码），ASCII码，，

# 编码方式，指将内存中经字符集编码的数据，存入硬盘的格式

# unicode码起到一个中介作用，我们在输入不论什么字符，unicode码都有对应
# utf-8，我们将unicode字符集精简后形成的对应关系的编码格式
# gbk 中文编码
# GB2312，BIG-5


# 定长和非定长编码

# 文件头,指定解释器读取py文件的方式，也就是解码的方式
# python2 u''可以指定字符按照unicode的格式进行编码，而python2解释器的终端默认是按照gbk解码的，所以当我们按照utf-8编码时会出现乱码

# python3


print('123')

a = '人'
print(a)
res = a.encode('gbk')
print(res)
print(res.decode('gbk'))

# 打开文件
# 控制文件读写操作的模式
'''
    1.'r'只读
    2.'w'只写
    3.'a'只追加写
    4.'+'不能单独使用，配合'r+','w+','a+'作为扩展功能
'''
# 控制文件读写内容的模式
'''
    1.'t'模式
       读写都是以字符串(unicode)为单位
       encoding = 'utf-8'
       只针对文本文件
    2.'b'模式
        读写是以bytes/二进制为单位

'''
# python的转义字符的作用
'''
    1.续行符
    2.反斜杠符号 \\ \' \" \a响铃 \b退格 \v纵向制表 \t横向制表 \r回车 \n换行 \000空字符 \f换页
    3.
'''

# 续行符
print('line--\
      line2--\
      line3')

print('x\000y')
print('x\ryx')
print('\141\41')
print('\x40')
# 打开文件
f = open(r'/data/a.txt', mode='rt', encoding='utf-8')
print(f)

# 文件读写
res = f.read()
print(res)

# 文件关闭，资源回收（指操作系统），内存空间的回收由python的垃圾回收机制处理

f.close()
# 为了简化手动关闭文件使用了with语法(上下文管理器)
with open(r'/data/a.txt', mode='rt', encoding='utf-8') as f:
    res = f.read()
    print(res, type(res))

# t\b
# rt
# 每次文件指针跳到最开始，
with open('../data/a.txt', mode='rt', encoding='utf-8') as f:
    # pass
    # res = f.read()
    # print(res)

    # 这里的问题是，每次read()都读完，当文件很大的时候，内存会不够，需要分次读
    print('第一次读'.center(80, '-'))
    res1 = f.read()
    print(res1)
    print('第二次读'.center(80, '-'))
    res2 = f.read()

# username_in = input('请输入用户名：')
# password_in = input('请输入密码')

# 单账号
# with open('./data/a.txt',mode='rt',encoding='utf-8') as f:
#     res = f.read()
#     username,password = res.split('--')
# if(username == username_in and password == password_in):
#     print('登陆成功')
# else:
#     print('登陆失败')

# 多账号

# with open('./data/a.txt',mode='rt',encoding='utf-8') as f:
#     for line in f:
#         #print(line,end='')
#         username,password = line.strip().split('--')
#         if(username == username_in and password == password_in):
#             print('登陆成功')
#             break
#     else:
#         print('登陆失败')


# wt
# r模式在文件不存在时，报错而w模式在文件不存在时会创建一个文件
with open('../data/c.txt', mode='w', encoding='utf-8') as f:
    #
    f.write('heloo')
    f.write('hexx')
# 注意当使用w模式打开文件时，会删除原来的内容同时文件指针指向开头，切记不要随意使用w模式去打开重要文件


# at a模式在open之后文件指针指向末尾

with open('../data/d.txt', mode='a', encoding='utf-8') as f:
    f.write('hello\n')

# 注册功能
# username_in = input('输入用户名：')
# password_in = input('输入密码：')
# with open('./data/user_data.txt',mode='a',encoding='utf-8') as f:
#     f.write(f'{username_in}--{password_in}\n')


# 拷贝功能

# old_path = input('请输入文件的旧路径：')
# new_path = input('请输入新路径：')
# with open(fr'{old_path}',mode='r',encoding='utf-8') as f,\
#     open(fr'{new_path}',mode='w',encoding='utf-8') as f1:
#     res = f.read()
#     f1.write(res)


# +模式
# r+
with open('../data/a.txt', mode='r+', encoding='utf-8') as f:
    # res = f.read() #read读完之后会将文件指针指向末尾
    # print(res)
    f.write('hhh')  # 使用了+模式之后，就可以使用write()

# w+
# a+


# x模式，只写不可读，相比于w模式来说，x模式当文件不存在时创建文件，当文件存在时报错

# 回车和换行
# 不同操作系统不太一样 windows:\r\n,linux:\n,mac os 9:\r,mac os 9之后:\n,
# python作为跨平台的语言，对于不同操作系统，它的\n进行了对应的调整

# b模式

# with open('./data/img1.jpg','rb') as f:
#     res = f.read()
#     print(res)
#     print(type(res))
print('-' * 50)
with open('../data/a.txt', mode='rb') as f:
    res = f.read()
    print(res)
    print(res.decode('utf-8'), type(res.decode('utf-8')))

with open('../data/e.txt', 'wb') as f:
    f.write('天下'.encode('utf-8'))

# 通用拷贝功能

# old_path = input('请输入文件的旧路径：')
# new_path = input('请输入新路径：')
# with open(fr'{old_path}',mode='rb') as f,\
#     open(fr'{new_path}',mode='wb') as f1:
#     for line in f:
#         f1.write(line)
# 当一行的文件很长的时候使用分次读取的功能
# with open(fr'{old_path}',mode='rb') as f,\
#     open(fr'{new_path}',mode='wb') as f1:
#     while 1:
#         res = f.read(1024)
#         if not res:
#             break
#         f1.write(res)    
#     print('复制完毕')

# with open('data/a.txt',mode='rb') as f:
#     for line in f:
#         print(line)

# #分次读取
# with open('data/img1.jpg',mode='rb') as f:
#     while True:
#         res = f.read(1024)
#         if not res:
#             break
#         print(res)
#         print(len(res))

# readline 读一行数据
# readlines 读文件，返回列表，一行一个元素

with open('../data/a.txt', mode='rt', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line, end='')

with open('../data/a.txt', mode='rt', encoding='utf-8') as f:
    print('8' * 50)
    lines = f.readlines()
    print(lines, end='')

# writelines

# with open('data/f.txt',mode='wt',encoding='utf-8') as f:
#         f.writelines(['aa\n','bb\n'])


# with open('data/f.txt',mode='wb') as f:
#         f.writelines([
#             'aa\n'.encode('utf-8'),
#             'bb\n'.encode('utf-8'),
#             b'dd\n',
#             bytes('啊',encoding='utf-8'),
#             f'{str(32)}\n'.encode('utf-8')
#             ])

print('-' * 50)
print('12das'.encode('utf-8'))
print('12das'.encode('gbk'))
print('我'.encode('utf-8'))
print(bytes('我', encoding='utf-8'))  # encode方法的本质上是调用了这个

# flush缓存的概念

# with open('./data/f.txt','wt',encoding='utf-8')as f:
#     print(f.readable())
#     print(f.writable())
#     print(f.closed)
#     print(f.encoding)
#     print(f.name)
# print(f.closed)


# #文件指针移动
# with open('data/f.txt',mode='rt',encoding='utf-8') as f:
#     res = f.read(5) #读5个字符
#     print(res)

# #f.seek(n,参照位置),从参照位置开始移动5个字节
# #模式0：从开头位置移动
# f.seek(3,0)
# f.seek(5,0)

# #模式1
# f.seek(4,1)
# f.seek(2,1)

# #模式2
# f.seek(-2,2)
# f.seek(-4,2)


# with open('data/f.txt',mode='rb') as f:
#     f.seek(2,0)
#     print(f.tell())
#     res = f.read()
#     print(res.decode('utf-8'))


# 写日志
# with open('data/user.log','at',encoding='utf-8') as f:
#     while True:
#         money = input('请输入充值的钱数')
#         if(money == 'q'):
#             break
#         f.write(f'用户充值了{money}w\n')

# 修改文件

# with open('data/f.txt',mode='rt',encoding='utf-8') as f:
#     res = f.read()
#     l = list(res)
#     print(l)
#     l.insert(3,'不')
#     new_res  = ''.join(l)
#     print(new_res)
# with open('data/f.txt',mode='wt',encoding='utf-8') as f:
#     f.write(new_res)

import os

with open('../data/g.txt', mode='rt', encoding='utf-8') as f, \
        open('data/g.txt.swap', mode='wt', encoding='utf-8') as f1:
    for line in f:
        res = line.replace('一会', '一年')
        f1.write(res)
os.remove('../data/g.txt')
os.rename('data/g.txt.swap', '../data/g.txt')
