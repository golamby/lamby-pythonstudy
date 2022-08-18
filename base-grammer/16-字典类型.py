from re import T

dic = {'a': 1, 'b': 2, 'c': 3}
# 实际上是调用了如下函数
dict({'a': 1, 'b': 2, 'c': 3})

print(dic, type(dic))

dic = dict(a=1, b=2, c=3)
print(dic)
print(dic['a'], type(dic['a']))

keys = ['name', 'gender', 'age']
# 现在有一个需求让建一个字典，value为None
for key in keys:
    dic[key] = None
print(dic)

dic = {}.fromkeys(keys, 1)
print(dic)

# 类型转换

l = [('name', '1'), ['age', 2]]  # 成对出现
t = (('name', 'jack'), ['age', 2])
print(dict(l))

# 添加元素
dic = {'a': 1, 'b': 2, 'c': 3}
dic['d'] = 4
print(dic)

# 获取value ,中括号和get方法，get方法在没有该key时返回None，而[]直接报错
# print(dic['e'])
print(dic.get('e'))

# 删除，del，pop(),popitem()

del dic['a']
print(dic)
dic.pop('b')
print(dic)

print(dic.popitem())

print(len(dic))
dic.clear()

dic = {'a': 1, 'b': 2, 'c': 3}

print('a' in dic)

print(type(dic))
# 内置方法

print(dic.keys())
print(dic.values())
print(dic.items())

# for key in dic.keys():
#     print(key)

for value in dic.values():
    print(value)
for item in dic.items():
    print(item)

# 解压赋值

for key, value in dic.items():
    print(key, value)

# update 和 setdefalut

dic1 = {'name': '张三',
        'age': 18,
        'gender': 'male'
        }
dic2 = {
    'school': 'pku',
    'salary': 112,
    'age': 20
}
dic1.update(dic2)
print(dic1)

print(dic1.setdefault('age'))
print(dic1.setdefault('hobby', 'play'))
print(dic1.setdefault('home'))
print(dic1)
