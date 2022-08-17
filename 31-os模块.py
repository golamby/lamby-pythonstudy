import os
"""
    os.getcwd()
    # 获取当前工作目录
    os.chdir("dirname") # 改变当前脚本工作目录；相当于终端里面的cd命令
    os.listdir('dirname') # 获取指定目录下的所有文件和文件夹，包括隐藏文件，并返回列表
    os.mkdir('dirname') # 创建文件夹；相当于终端里面的mkdir dirname
    os.makedirs('dirname1/dirname2') # 递归创建多层目录
    os.remove()
    # 删除一个文件
    os.rmdir('dirname') # 删除单级空目录，若目录不为空则无法删除,则报错
    os.rename('oldname','newname') # 重命名文件/目录
    os.system("rm -rf /") # 运行终端命令
    os.environ
    # 获取系统环境变量
    os.environ.get('KEY') # 获取系统环境变量的某一个值
    os.getenv('KEY')
    # 获取系统环境变量的某一个值
    os.stat('path/filename')# 获取文件/目录信息
    os.name
    # 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
    os.path.split(path) # 将path分割成目录和文件名,返回元组
    os.path.dirname(path) # 返回path的父级目录。其实就是os.path.split(path)的第一个元素
    os.path.basename(path) # 返回path最后的文件名。如path以／或\结尾，那么就会返回空值。即
    os.path.split(path)的第二个元素
    os.path.exists(path) # 如果path存在，返回True；如果path不存在，返回False
    os.path.isabs(path) # 如果path是绝对路径，返回True
    os.path.isfile(path) # 如果path是一个存在的文件，返回True。否则返回False
    os.path.isdir(path) # 如果path是一个存在的目录，则返回True。否则返回False
    os.path.join(path1[, path2[, ...]]) # 将多个路径组合后返回，第一个绝对路径之前的参数将被
    忽略
    os.path.getatime(path) # 返回path所指向的文件或者目录的最后读取时间
    os.path.getmtime(path) # 返回path所指向的文件或者目录的最后修改时间
    os.path.getctime(path) # # 返回path所指向的文件或者目录的创建时间(windows平台中)
    os.path.getsize(path) # 返回path的大小

"""


print(os.getcwd())

os.chdir('./data')
print(os.getcwd())

print(os.listdir(os.getcwd()))

os.mkdir()





