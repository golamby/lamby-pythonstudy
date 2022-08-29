__all__ = ['name', 'get']

name = 'me'


def my_func1():
    print('module_func1')


def my_func2():
    global name
    name = 'yyy'
    print('module_func2')


def get():
    print(name)


print('module的__name__:', __name__)

if __name__ == '__main__':
    my_func1()
    my_func2()
    print('module 被执行')
else:
    print('module被导入')
