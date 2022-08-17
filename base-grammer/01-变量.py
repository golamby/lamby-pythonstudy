# 创建变量，以及变量的引用计数的概念
# 变量的命名规则，注意python的关键字

a = 100
b = a
c = a

del a
del b

c = 123
# 此时100的内存单元引用计数为0，触发垃圾回收机制

# id,变量的内存地址
print(id(c))

# type，变量类型
print(type(c))

# is 和 == 的区别

a = 123
b = 123
c = 12
print(id(a))
print(id(b))
print(id(c))
print(a is b)
print(a == b)

# 小整数池 解释器会将-5~256的整数放到池子里，同样的数值就不再回收之后重新开辟内存空间，这样较少了cpu与内存的交互，加快了速度
# 这里vscode里相等但是cmd终端里不等，因为vs里做了优化
a = -6
b = -6
print(id(a))
print(id(b))
