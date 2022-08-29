# 模块是一些列功能的集合体
# python内置模块
# 第三方模块
# 自定义模块

import os

import time

'''
模块:许多功能的集合体
包:把文件夹作为模块使用，但必须有__init__.py文件存在
'''

# 模块导入规范，内置，第三方，自定义

# 模块名和函数名一样可以被传递，当作返回值返回，作为容器的元素
# import time
# import os

# import pymysql
# import requests

# import module as m
# m.my_func1()


# __name__  ,当模块被导入时为模块名，当在本文件中执行时__name__为__main__
# 当模块被导入之后，会自动执行模块内的代码，里面可能会有一些函数执行，为了避免导入模块后，模块内部代码对被执行文件的干扰，我们使用
# if __name__ == '__main__':  来执行功能


# from模块导入
# 使用from导入，对应名称空间直接指向模块内部的变量的内存地址，而import则是通过module这个模块名再找到的
# as取别名

# from module import my_func1
# from module import my_func2
# from module import name
# from module import get

# name = 'hhh' #更改本文件的name的内存地址为hhh的内存地址
# my_func2() #module里的name: me->yyy 
# get() #取module里的name：yyy
# print(name) #hhh


# from module import *
# #__all__模块向外暴露的内部名称空间的列表

# my_func1()


# 循环导入

# 模块的查找顺序
# sys.path展示了模块的查找顺序

# 内存
# 硬盘

import sys

print(sys.path)

# sys.path.append(r'D:\pythonstudy\pythonbase\28-package\mm')  这种方式不太好，后续有解决方案
# import module

# print(module.name)


# 包
# 不论是导包还是模块，流程如下：
# 1.创建名称空间
# 2.执行python文件
# 3.在执行文件的名称空间中创建一个名字，指向刚刚创建的名称空间


# import pack
# print(pack.name)      
# print(pack.__name__)  #pack

import game

game.chat()
print(game.brilliant)

game.sell()
