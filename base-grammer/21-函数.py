def func1():
    print('func1')
    print(func2)
    func2()


def func2():
    print('func2')


func1()
print(func1)


# func代表函数内存地址，func(x)代表参数为x，func()运行后的返回值

# 有参函数
def func1(x, y):
    print(x, y, type(x), type(y))


func1(3, 4)
func1('3', ['4'])


# return 返回多个值返回一个元组,没有返回值为None
def func1(x, y):
    return x + y, x - y, [x, y], {f'{x}': y}


a, b, c, d = func1(1, 2)
print(a, b, c, d)

# 实参和形参
a = 3
b = 4
print(id(a))  # 2482078247280


def func1(a, b):
    print('enter func1')
    a = 4
    print(id(a))  # 2482078247312
    b = 3
    print('exit func1')


func1(a, b)
print(a, b)  # 3 4


# a和b的值并没有发生改变，显然我们在函数内部创建了一个新的变量a，将实参a的值传给了形参a

# 位置参数
# 位置形参，从左到右一次定义的形参，必须传值
def func1(a, b, c):
    print(a, b, c)


func1(1, 2, 3)

# 默认参数(默认形参)，函数定义阶段为参数设置初值
a = 3


def func(x, y=a):
    print(x, y)


a = 2
func(1)

# l = [1,2]
# def func(x,y=l):
#     print(x,y)
# l.append(4)
# func(1)


# Python里所有的值的传递，都是内存地址的传递，内存地址时值的引用

# 位置实参,调用函数时一次传入的参数
func1(3, 2, 1)

# 关键字参数，可以不按顺序，key=value传值，但必须在位置实参之后
func1(a=1, b=4, c=5)
func1(1, 4, c=5)


# 函数的默认参数虽然可以指定为任意类型，但是不建议设为可变类型

# def my_append(x,y,l=[]):
#     l.append(x)
#     l.append(y)
#     print(l)
def my_append(x, y, l=None):
    if l is None:
        l = []
    l.append(x)
    l.append(y)
    print(l)


l1 = [1, 2, 3]
my_append(4, 5, l1)


# 可变长参数
# 可变长的位置参数，前面加上*号，多出来的都的参数形成元组交给可变长参数
def func1(x, y, *z):
    print(x, y, z)


func1(1, 2, 3, 4, 5, 6)  # 1 2 (3, 4, 5, 6)


def sum(*args):
    res = 0
    for i in args:
        res += i
    return res


print(sum(1, 2, 3, 4, 5))


# 可变长的关键字参数 **kwargs,将这些关键字形参作为字典
def func1(x, y, **kwargs):
    print(x, y, kwargs)


func1(1, 2, a=1, b=2, c=3)  # 1 2 {'a': 1, 'bs4解析': 2, 'c': 3}


# 在实参前面加参数，可以将列表打散，传给形参
# def func1(x,y,z):
#     print(x,y,z)
# l = [1,2,3]

# func1(*l) #1 2 3

def func1(x, y, *args):
    print(x, y, [i for i in args])


func1(1, 2, *[4, 5, 6])  # 1 2 [4, 5, 6]
func1(*'我爱学python')


#
def func(a, b, c):
    print(a, b, c)


func(*{'a': 1, 'bs4解析': 2, 'c': 3})
func(**{'a': 1, 'bs4解析': 2, 'c': 3})  # 打散成func(a=1,bs4解析=2,c=3)


def func1(x, y, **kwargs):
    print(x, y, kwargs)


func1(**{'x': 1, 'y': 2, 'c': 3, 'd': 4})  # 1 2 {'c': 3, 'd': 4}


def func(x, y=2, *args, **kwargs):
    print(x, y, args, kwargs)


func(1, 4, 36, 9, a=7)


# ------------------------

def func1(x, y, z, m):
    print('func1>>>>>', x, y, z, m)


def func2(*args, **kwargs):
    func1(*args, **kwargs)


func2(1, 2, 3, 4)

# 名称空间
"""
    栈区的名称空间可以分为全局名称空间，局部名称空间，内置名称空间
    防止命名冲突
    
    内置名称空间:
    Python解释器内置的名字 像print,input之类的
        python解释器已启动，就会创建，解释器关闭，内置名称空间销毁
        作用范围是全局作用域

    全局名称空间
    Python文件(或模块)内定义的变量名，包括函数名，类名，模块名
    import os import time等等
    在python文件执行之前产生，执行之后销毁，凡是不在函数内部定义或python内置的变量都是全局的

    局部名称空间
    函数内部定义的变量
"""


# 名称空间查找优先级：
#   局部名称空间>全局名称空间>内置名称空间

# input = 1 #1
def func():
    # input = 'hhh'  #hhh
    print(input)


func()  # 都注释之后是 <built-in function input>


# 内部->全局->内置

def func():
    print(x)


x = 10
func()  # 10

# 名称空间的查找顺序是以定义阶段为基准的，和调用的位置没有任何关系
# 被调用函数的参数就是先从该函数内部然后到外包到全局再到内置。跟调用者函数内部定义没有关系。
x = 10


def func1():
    print(x)


def func2():
    x = 20
    func1()


func2()  # 10

# input = 10
# def func1():
#     input = 20
#     def func2():
#         #input = 30
#         print(input)

#     func2()

# func1()


# 作用域
# 全局作用域和局部作用域
# 全局作用域：全局名称空间和内置名称空间
# 全局存活，全局有效


# 局部作用域：局部名称空间

# 名称空间顺序是定义阶段（def func():）的：LEGB (local,enclosing,global,buit-in)


# global

x = 20


def func():
    global x  # 加了这个变成10
    x = 10


func()
print(x)

# 不可变类型通过global在局部名称空间声明即可改变全局名称空间的变量值。可变类型例如list可通过append在局部名称空间改变。
l = [1, 2, 3]


def func():
    l.append(4)


func()
print(l)

# nonlocal
# 声明了变量为nonlocal之后,就不在该层找到变量，去上一层找
x = 10


def fun():
    x = 20

    def fun1():
        nonlocal x
        x = 30

    print('调用fun1之前的x:', x)
    fun1()
    print('调用fun1之后的x:', x)


fun()
print(x)


# 函数传递,函数名可以作为参数传递
# #--------------------------------------------电子钱包
# def login():
#     print('执行登录功能')
# def scan():
#     print('执行扫码支付功能')
# def transfer():
#     print('执行转账功能')
# def query():
#     print('执行查询功能')
# def recharge():
#     print('执行充值功能')
# fun_dic = {'a':(login,'登录'),
#            'bs4解析':(scan,'扫码支付'),
#            'c':(transfer,'转账'),
#            'd':(query,'查询'),
#            'e':(recharge,'充值')}
# while True:
#     for key in fun_dic:
#         print(f'{key}:',fun_dic[key][1])
#     opt = input('请输入你要进行的操作')
#     if opt == 'z':
#             break
#     # if opt == '0':
#     #     break
#     # elif opt == '1':
#     #     login()
#     # elif opt == '2':
#     #     scan()
#     # elif opt == '3':
#     #     transfer()
#     # elif opt == '4':
#     #     query()
#     # elif opt == '5':
#     #     recharge()
#     # else:
#     #     print('没这个功能')
#     # -----------------------------------------------------优化
#     #     if opt in fun_dic:
#     #         fun_dic[opt]()
#     #     elif opt == '0':
#     #         break
#     #     else:
#     #         print('没这个功能')
#     if opt not in fun_dic:    
#         print('没这个功能')
#         continue

#     fun_dic[opt][0]()
# #-------------------------------------------


# 闭包函数
# 闭函数，函数是封闭的，比如函数内部定义函数
# 包函数，函数内部包含对外部函数作用域名字的引用

# 闭包函数通过返回内部函数的内存地址得以在enclosing 函数（）调用以后被找到闭包内部函数的内存地址，并且可以通过（）调用。
def f1():
    x = 10

    def f2():
        print(x)

    return f2


res = f1()  # f1的返回值是f2的内存地址
print(res)


def f1(x):
    def f2():
        print(x)

    return f2


res = f1(100)
res()

from opcode import hascompare
from operator import mod
import time
from tracemalloc import start


# 装饰器
# 一个函数 用来给其他函数增添功能注意不是修改

# def func1(group,sec,z):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}方阵营')
#     print(f'敌军还有{sec}s到达战场')
#     time.sleep(sec)
#     print(f'{z}出击')

# 最原始的装饰器
# def wrapper():
#     start = time.time()
#     func('蓝色',3)
#     end = time.time()
#     print(end - start)
# 1.直接修改原函数
# 2.抽取出来在每个func前后加上统计时间
# 3.抽象为函数wrapper
# 4.参数更改时，wrapper参数使用*args和kwargs
# 5.当要装饰不同函数的时候，利用闭包传递函数


# 4.当inside参数变化时，wrapper参数需要变化
# def wrapper(*args,**kwargs):
#     start = time.time()
#     func1(*args,**kwargs)
#     end = time.time()
#     print(end - start)

# wrapper('蓝色',3)

# 当原函数有返回值时
def count_timer(functionName):
    func = functionName

    def wrapper(*args, **kwargs):
        start = time.time()
        response = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return response

    return wrapper


@count_timer  # func1 = count_timer(func1)
def func1(group, sec, z):
    print('欢迎来到王者荣耀')
    print(f'你出生在{group}方阵营')
    print(f'敌军还有{sec}s到达战场')
    time.sleep(sec)
    print(f'{z}出击')


@count_timer  # recharge = count_timer(recharge)
def recharge(num):
    for i in range(num, 101):
        time.sleep(0.05)
        print(f'目前电量{"▮" * i} {i}%\r', end='')
    print()
    print('充满了')
    return 100


# res = recharge(50)
# print(res)


# 装饰器模板

# def outer(func):
#     def wrapper(*args,**kwargs):
#         res = func(*args,**kwargs)
#         return res
#     return wrapper


# 统计时间的装饰器

def count_timer1(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return res

    return wrapper


# @count_timer1
# def home():
#     time.sleep(2)
#     print('welcome')
from functools import wraps


def auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        username = input('请输入你的用户名：')
        password = input('请输入密码：')
        if (username == 'jack' and password == '123'):
            res = func(*args, **kwargs)
            return res
        else:
            print('账号或密码错误')

    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__
    return wrapper


@auth
def home():
    '''---------
     这是home函数
    '''
    print('hello')


print(home)
# <function auth.<locals>.wrapper at 0x000001C74105DDC0>,
# 不加auth装饰器，<function home at 0x0000016FFF7DDD30>

# 我们可以将原函数的这些方法属性比如说，__name__,__doc__赋值给wrapper
# python为我们提供了方法来进行封装  from functools import wraps


# 这里涉及到方法的属性
print(home.__name__)
print(home.__doc__)


# 在不更改func的参数条件下，再向func传入参数
def g_outer(name):
    def outer(func):
        def wrapper(*args, **kwargs):
            print(name)
            res = func(*args, **kwargs)
            return res

        return wrapper

    return outer


@g_outer('hhh')
def home():
    '''---------
     这是home函数
    '''
    print('hello')


# -----------------------有参装饰器的应用
def auth(source):
    def outer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            username_in = input('请输入你的用户名：').strip()
            password_in = input('请输入密码：').strip()
            if source == 'file':
                # 从文件中读取
                print('从文件中读取')
                with open('../data/a.txt', mode='rt', encoding='utf-8') as f:
                    for line in f:
                        username, password = line.strip().split('--')
                        if username_in == username and password_in == password:
                            res = func(*args, **kwargs)
                            return res
                    else:
                        print('登陆失败')
            elif source == 'mysql':
                print('进行mysql读取')
            elif source == 'ldap':
                print('进行ldap读取')
            else:
                print('不支持')

        # wrapper.__name__ = func.__name__
        # wrapper.__doc__ = func.__doc__
        return wrapper

    return outer


# 现在不同的功能用户名的验证方式不一样
@auth('file')
def home():
    print('home功能')


@auth('mysql')
def walk():
    print('walk功能')


@auth('ldap')
def run():
    print('run功能')


# 装饰器的叠加
def outer1(func):
    def wrapper(*args, **kwargs):
        print('outer1进入')
        res = func(*args, **kwargs)
        print('outer1退出')
        return res

    return wrapper


def outer2(x):
    def outer(func):
        def wrapper(*args, **kwargs):
            print('outer2进入')
            res = func(*args, **kwargs)
            print('outer2退出')
            return res

        return wrapper

    return outer


def outer3(func):
    def wrapper(*args, **kwargs):
        print('outer3进入')
        res = func(*args, **kwargs)
        print('outer3退出')
        return res

    return wrapper


# 很像递归/堆栈
@outer3
@outer2(10)
@outer1
def home():
    print('home功能')


home()
