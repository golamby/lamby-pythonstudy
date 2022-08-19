name = 'jack'
print(name, type(name))

# 实质上在赋值过程中调用了str()

s = str(['a', 'bs4解析'])
print(s, type(s))

# 字符串的内置方法

# 索引取值

s = 'hello world'
print(s[2])  # 'l'
print(s[-1])  # 'd'负号表示倒数
# 字符串不能根据索引更改值

# 切片，左闭右开，顺序，倒序，步长

print(s[0:5])
print(s[0:])
print(s[0:5:2])
res = s[::-1]
print(res)
print(s[-1:-3:-1])

# strip去除空格或者其它字符，参数：去除的字符串/字符

name = '  jack  '
print(name.strip())
s = '+-*  sdad  -*/'
print(s.strip('+-*'))
print(s.strip('+-*/ '))
print(s.lstrip('+-'))

# split拆分,参数有1.根据什么字符拆分，2.拆分次数

name = '李白 杜甫 王维 李商隐'
res = name.split()
print(res, type(res), res[0])

name1 = '李白-杜甫-王维-李商隐'
res = name1.split('-', 1)
print(res)

# 循环遍历


# 长度len

s = 'hello world'
print(len(s), type(len(s)))

# 成员运算in  not in

print('hello' in 'hellwlehello')

# 常见方法：
# 1.strip , lstrip, rstrip
s = '  jack  '
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# 2.split, rsplit
name = 'zhang-san-li-si'
print(name.split('-', 1))
print(name.rsplit('-', 1))

# 3.lower, upper

name = 'ZhangSan'
print(name.lower())
print(name.upper())

# 4.startswith endswith

print('hello'.startswith('he'))
print('hello'.endswith('lo'))

# 5.join
name = ['李白', '杜甫', '王维', '李商隐']
print('-'.join(name))

# 6.replace

name = 'zhangsan-xlisi'
print(name.replace('-x', ','))

# 7.isdigit

print('22'.isdigit())
print('88a'.isdigit())

# while True:
#     num = input('请输入要猜的数字：')
#     if num.isdigit():
#         num = int(num)
#     else:
#         print('请输入纯数字')
#         continue
#     if num > 36:
#         print('猜大了')
#     elif num < 36:
#         print("猜小了")
#     else:
#         print('猜中了')
#         break


s = 'hello world'
print(s.find('wo'))
print('1aa2'.islower())

# 字符串需要了解的操作
# 1 capitalize()  将字符串的第一个字符转换为大写
# 2 center(width, fillchar) 返回个指定的宽度 width居中的字符串， fillchar为填充的字行默认为空格 。
# 3 count(str, beg= 0, end=Len(string)) 返回str在string 里面出现的次数，如果beg或者end指定则返回指定
# 4 expandtabs(tabsize=8) 把字符串string 中的tab符号转为空格， tab符号默认的空格数是 8
# 5 find(str, beg=0, end=Len(string)) 检测str是否包含在字符串中，如果指定范围beg 和end，则检查是否包含在扑
# 6 rfind(str, beg=0, end=Len(string))类似于find()函数， 不过是从右边开始查找.
# 7 index(str, beg=0， end=Len(string)) 跟find()方法一样，只不过如果str不在字符串中会报一个异常。
# 8 rindex( str, beg=0, end=Len(string))类似于index(), 不过是从右边开始.
# 9 isalnum() 如果字符串至少有一个字符并且所有字符都字母或数字则返回True, 否则返回False
# 10 isalpha() 如果字符串至少有一个字符并且所有字符都是字母或中文字则返回True, 否则返回False
# 11 islower() 如果字符串中包含至少一个区分大小写的字符，并且所有这些字符都是小写，则返回True, 否则返回False
# 12 isupper() 如果字符串中包含至少一个区分大小写的字符，并且所有这些字符都是大写，则返回True, 否则返回False 
# 13 isspace()如果字符串中只包含空白，则返回True, 否则返回False.
# 14 ljust(width, fillchar) 返回一个原字符串左对齐，并使用fillchar 填充至长度width 的新字符串，fillchar 默认为
# 15 rjust(width, filLchar)返回一个原字符串右对齐，并使用filLchar(默认空格)填充至长度width 的新字符串
# 16 max(str) 返回字符串str 中最大的字母。
# 17 min(str) 返回字符串str中最小的字母。
# 18 swapcase() 将字符串中大写转换为小写，小写转换为大写
# 19 title() 返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写
# 20 istitle()如果字符串是标题化的，则返回True, 否则返回False
