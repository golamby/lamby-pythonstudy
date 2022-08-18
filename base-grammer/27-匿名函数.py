def func(x, y):
    return x + y


res = (lambda x, y=1: x + y)(1, 3)
print(res)

info = {
    'jack': 1200,
    'lucy': 2000,
    'mike': 20000,
    'mary': 5000
}

res = max(info, key=lambda k: info[k])
print(res)

l = [1, 4, 3, 5, 8]
l.sort(reverse=True)
print(l)

l = [(1, 2), (3, 4), (2, 1), (4, 3)]
l.sort(key=lambda item: item[1])
print(l)

# sorted()

l = ['康师傅', '白象', '统一']
new_l = [name + '_老坛酸菜' for name in l]
print(new_l)
# 列表太长用生成器表达式[]换成()


res = map(lambda i: i + '_老坛酸菜1', l)
print([item for item in res])


# python是一门解释型强类型的动态语言

# 类型提示，当不满足时不会报错
def fun(name: str, age: int) -> int:
    print(name)
    print(age)
    return 10


res = fun('hh', [1, 2])
print(res)
