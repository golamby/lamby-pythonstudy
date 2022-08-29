from re import sub
import subprocess

# 执行终端命令

obj = subprocess.Popen('tree',
                       shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       encoding='utf-8')

stdout_res = obj.stdout.read()
print(stdout_res.decode('utf-8'))

err_res = obj.stderr.read()
print(err_res)
