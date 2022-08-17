from turtle import end_fill


l = ['康师傅_老坛酸菜','统一_老坛酸菜','大今野_老坛酸菜','白象']

new_l = []

for name in l :
    if name.endswith('老坛酸菜'):
        new_l.append(name)
print(new_l)

#列表生成式 [结果 for i in 可迭代对象 if 条件]
new_l = [name for name in l if name.endswith('老坛酸菜')]

print(['aaa' for name in l if name.endswith('老坛酸菜')])

print([name for name in l if True])

print([name.replace('老坛酸菜','小鸡炖蘑菇') for name in l])

new_l = [i for i in range(10) if i > 6]


print(new_l)


#集合生成式
l = ['康师傅_老坛酸菜','统一_老坛酸菜','大今野_老坛酸菜','白象']
res = {name for name in l}
print(res)


#字典生成式
l = [('康师傅_老坛酸菜',5),('统一_老坛酸菜',5),('大今野_老坛酸菜',5),('白象',7)]
res = {k : v for k,v in l if not k.startswith('康师傅')}
print(res)

#生成器表达式（元组表达式）
l = ['康师傅_老坛酸菜','统一_老坛酸菜','大今野_老坛酸菜','白象']
res = (name for name in l )
print(res)
print(res.__next__())
# print(list(res))
print(res.send(10))
print(res.send(None))
print(res.send('1'))



#统计文件字符个数


#sum()函数
#它的参数是可迭代对象，本质上调用了for 循环去执行__next__()方法，每次得到一个数加进去
# >>> sum([1,2,3])  6
#



with open('../data/user.log', mode='rt', encoding='utf-8')as f:
    # size = 0
    # for line in f:
    #     size += len(line)
    # size = sum([len(line) for line in f])
    size = sum((len(line) for line in f))


print(size)









