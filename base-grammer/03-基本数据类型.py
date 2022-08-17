# Number 数字类型

# 1.整型 int
# -21, 0, 100, 2000


a = 122
print(type(a))

# 2.浮点型 float
price = 34.11
print(type(price))

# 同种类型可以使用+，比如number类型之间，list之间

a = 3
b = 1.2
c = a + b
print(c, type(c))

# 字符串类型str,下面这三个都可以
s1 = 'abc'
s2 = "abc"
s3 = '''abc'''

a = 'hello world'
print(a, type(a))
print(s1, s2, s3, type(s1), type(s2), type(s3))

# 如果想要在字符串中再出现单双引号，可以交叉着使用，避免错误的配对
s4 = 'my name is "hello"'
print(s4)
# 也可以使用转义字符
s4 = 'my name is \'ss\''
print(s4)
# 字符串拼接
print(s4 + s1)

print('-' * 50)

# python处理字符串前面加上r表示原生字符串（rawstring）
print('a\nb')
print(r'a\nb')

# 列表
l = ['lucy', 18, 22.2, ['aa', 'bb']]
print(l)
print(l[0], type(l[0]))
print(l[-1][0])

person = [['张大仙', 20, 12, ['可乐', '厕所', '游戏']],
          ['于谦', 45, 20, ['抽烟', '喝酒', '烫头']]
          ]
print(person[1][3][1])

# 字典

dic = {
    'name': '张大仙',
    'age': 18,
    'height': 150,
    'dimension': [60, 80, 99]
}

print(dic['age'])

# 布尔类型bool

a = True
b = False
print(type(a))

c = None
print(type(c))

# 0,None,'',[],{}都代表False

# 直接引用和间接引用

name = '张大仙'
l = ['a', 'b', name]  # 直接引用
print(l[2])  # 间接引用
print(id(name))
print(id(l[2]))

# 列表在内存中的存储方式
# 内存中开辟一块存放真正内容的地址的区域，也就是说列表存放了一系列引用
# gc机制：引用计数，标记清除，分代回收

name = '李白'
print(l[2])
print(name)

# 循环引用引起的内存泄漏

l1 = ['a', 'b']
l2 = ['x', 'y']
l1.append(l2)
print(id(l1[2]), id(l2))
l2.append(l1)
print(id(l2[2]), id(l1))
# 此时如果运行了一下两行代码会清除直接引用，会导致l1,l2的内存引用次数因为间接引用永远不为零，导致了这两块区域一直占用内存空间，造成内存泄漏
# del l1
# del l2


# 内存空间分布，标记清除机制，栈区和堆区，内存空间不够时，通过扫描栈区，重新找到那些内存泄漏的区域再清除掉

# 分代回收机制，以优秀的学生检查作业次数降低来降低垃圾回收时扫描栈区频繁的情况发生，提高了扫描效率
