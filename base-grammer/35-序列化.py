# 序列化与反序列化
# 将内存中的数据转化为一种特定的格式，这个格式可以用于存储，传输给其他平台


# 内存中的数据 -- > 序列化 --> json/pickle
# 内存中的数据 -- > 反序列化 <-- json/pickle


# 用途：
# 1.存档，将内存数据保存到硬盘
# 2.跨平台数据交互    java程序的数据 --> python程序， 只能用json，pickle是python独有的格式

import json

# 序列化
dic = {
    'name': 'jack',
    'age': 18,
    'salary': 12.1,
    'married': False,
    'hobbies': ['吃', '喝', '睡']
}

# json_res = json.dumps(dic,ensure_ascii=False) 
# #ensure_ascii这个参数为True表示序列化之后所有的字符都可以用ascii码表示，不加反序列化也没问题
# print(json_res)

# with open('data/test.json',mode='wt',encoding='utf-8') as f:
#     f.write(json_res)


with open('../data/test.json', mode='wt', encoding='utf-8') as f:
    json.dump(dic, f, ensure_ascii=False)

# with open('data/test.json',mode='rt',encoding='utf-8') as f:
#     json_res = f.read()
# dic = json.loads(json_res)


with open('../data/test.json', mode='rt', encoding='utf-8') as f:
    dic = json.load(f)

print(dic, type(dic))

# python3.6之后，二进制读取的文件也可以被反序列化


# pickle模块

dic = {
    'name': 'jack',
    'age': 18,
    'salary': 12.1,
    'married': False,
    'hobbies': ['吃', '喝', '睡'],
    's': {1, 2, 3, 4}
}

import pickle

# pickle_res = pickle.dumps(dic,protocol=0)
# print(pickle_res,type(pickle_res))

# with open('data/test2.pickle',mode='wb') as f:
#     f.write(pickle_res)


with open('../data/test2.pickle', mode='wb') as f:
    pickle.dump(dic, f, protocol=0)
