# 迭代器：不依赖于索引的取值方式

# 列表，字符串，元组等可以按照索引取值
# 字典，集合，文件等都不能以索引方式取值

from operator import ne
from tkinter.tix import Tree
from turtle import end_fill

num = 0
l = ['a', 'bs4解析', 'c']
while num < len(l):
    print(l[num])
    num += 1

# 可迭代对象，可以转换为迭代器的对象
# 内置有__iter()__方法
# l = ['a','bs4解析','c']
# l.__iter__()

# str = 'abc'
# str.__iter__()

# t = ('a','bs4解析',1)
# t.__iter__()

# s = {1,2,'a'}
# s.__iter__()


# with open('data/a.txt',mode='rt',encoding='utf-8')as f:
#     f.__iter__()
#     f.__next__()


dic = {'a': 1, 'bs4解析': 2, 'c': 3}
print(dic.__iter__())

it = dic.__iter__()

# print(it.__next__()) #a
# print(it.__next__()) #bs4解析
# print(it.__next__()) #c

# 使用while循环和next方法遍历字典

while True:
    try:
        print(it.__next__())
    except StopIteration:
        break

# 迭代器对象内置有__next__()方法，和__iter__()方法的对象
# 迭代器对象调用__next__()方法，取到迭代器的下一个值

it = dic.__iter__()
print(it is it.__iter__())

# 对于for循环，主要做了以下的事情：
# 1.调用可迭代对象的__iter__()方法得到它的迭代器版本
# 2.调用迭代器对象的__next__()方法取得每一个值，赋值给key
# 3.循环执行第二步，直到抛出异常，就捕获异常，结束循环
for key in dic:
    print(dic[key])

# list,和tuple方法传入了可迭代对象，就是利用了for循环，将每一个取到的值放入了列表或者元组

print(list('hello'))
print(tuple('hello'))

print(dic.values())
print(dic.items())
print(dic.keys())
for item in dic:
    print(item, type(item))

print([1, 2, 3].__iter__())


# l1 = [1, 2, 3, 4, 5]
# print(l1.__iter__())


# 生成器

def func():
    print('11')
    yield 1
    print('22')
    yield 2
    print('33')
    yield 3
    print('44')
    yield 4


res = func()
print(res)  # <generator object func at 0x00000266FF85A6D0>

print(iter(res) is res)
print(res.__next__())
print(next(res))

l = [1, 2, 3]
# len(l)本质上时调用了如下方法__len__()
print(l.__len__())


# 生成器实际上就是迭代器
# 生成器对象调用__next__()方法，执行函数

# yield表达式
# 获取生成器对象
#
# 1.yield表达式可以暂停函数的执行
def func(x):
    print(f'{x}开始执行')
    while True:
        y = yield 3  # yield是执行玩这句话后返回的值，并不是y的值，y的值是有yield赋予的，通过send()传值，不传默认为None
        print(x, y)


res = func(10)  # 得到生成器对象
next(res)
res.send(100)
print(next(res))

# yield可以使得我们在两端代码间切换，实现一个'通信'的功能，协程的雏形
# 并发编程，爬虫下载图片（发送请求获取图片，获取到本地需要4s，发送0.01s），
# 我们可以将多个请求交给多个生成器，这样就会几乎同时执行，4s多就会获取到多张
