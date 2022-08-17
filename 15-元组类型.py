#不可变类型

x = (1,'a',1.2,['d','c','b'])
print(x)
x[3][0]= 'e'
print(x)

#类型转换
print(tuple('a'))
print(tuple([1,2,3]))
print(tuple({'a':1,'b':2}))
print(tuple(range(0,5)))

#元组一般适用只读场景
#内置方法有index和count


