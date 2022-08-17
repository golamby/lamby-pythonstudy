'''
while True:
    username = input('用户名：')
    password =  input('密码：')

    if username == 'admin' and password == '123456':
        print('登陆成功')
        break

    elif username != 'admin':
        print('用户名错误')
    else:
        print('密码错误')
'''

'''
condition = True
while condition:
    username = input('用户名：')
    password =  input('密码：')

    if username == 'admin' and password == '123456':
        print('登陆成功')
        while True:
            action = input('输入你要进行的操作：')
            if action == 'q':
                break
            print(f'正在{action}')
        print('退出')
        condition = False

    elif username != 'admin':
        print('用户名错误')
    else:
        print('密码错误')

'''


#continue

# num = 0
# while num < 10:
#     if num == 4:
#         num += 1
#         continue
#     print(num)
#     num += 1


#while + else
#只有当while条件不满足时，才会执行else，当while中出现break时，不会执行else的内容
num = 0
while num < 3:
    username = input('用户名：')
    password =  input('密码：')

    if username == 'admin' and password == '123456':
        print('登陆成功')
        while True:
            action = input('输入你要进行的操作：')
            if action == 'q':
                break
            print(f'正在{action}')
        print('退出')
        break

    elif username != 'admin':
        print('用户名错误')
        num += 1
    else:
        print('密码错误')
        num += 1
else:
    print('用户名或密码输出三次，请等待10s后重新输入')  
    







