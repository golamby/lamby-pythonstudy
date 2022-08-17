import time


from functools import wraps


from lib.common import logger

def auth(source):
    def outer(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            username_in = input('请输入你的用户名：').strip()
            password_in = input('请输入密码：').strip()
            if source == 'file':
            #从文件中读取
                print('从文件中读取')
                with open('data/a.txt',mode='rt',encoding='utf-8') as f:
                    for line in f:
                        username,password = line.strip().split('--')
                        if(username_in == username and password_in == password): 
                            res = func(*args,**kwargs)
                            logger(f'{username}登陆了')
                            return res
                    else:
                        print('登陆失败')
                        logger(f'{username_in}+{password_in}尝试登陆失败')
            elif source == 'mysql':
                print('进行mysql读取')
            elif source == 'ldap':
                print('进行ldap读取')
            else:
                print('不支持')
        return wrapper
    return outer





@auth('file')
def login():
    print('登录功能'.center(30,'*'))
    

def register():
    print('注册功能'.center(30,'*'))
    logger('注册了')


def recharge():
    x = input('请输入你要充值的金额')
    print(f'充值了{x}w'.center(30,'*'))
    logger(f'充值了{x}w')


def transfer():
    print('转账功能'.center(30,'*'))
    logger('转账了')


func_dic = {
    "0":('退出',exit),
    "1":('登录',login),
    "2":("注册",register),
    "3":("充值",recharge),
    "4":("转账",transfer)
}

def main():
    while True:
        for key in func_dic:
            print(f'{key}:{func_dic[key][0]}')
        opt = input('请输入你的操作：').strip()

        if opt == '0':
            break
        if opt not in func_dic:
            print('\033[033m没有这个功能\033[0m')
            continue
        func_dic[opt][1]()
    


