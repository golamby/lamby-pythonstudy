#可变类型，值改变，id不变，改变的是原值
#不可变类型，值改变，id同时改变

name = 'jack'
print(id(name))
name = 'lucy'
print(id(name))

#说明str类型是不可变的，改变值，会导致引用指向新的内存空间
#在python中str，int，float，tuple不可变
# list，dict,set都是不可变类型