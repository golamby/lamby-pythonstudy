import time

#监控程序
path = input('请输入你要监控的文件路径')
with open(fr'{path}',mode='rb') as f:
    f.seek(0,2)
    while True:
        res = f.readline()
        if res:
            print(res.decode('utf-8'),end='')
        time.sleep(0.2)
