import random
import re


#random() -- 返回0——1之间的float
print(random.random())

print(random.uniform(9,10))  #左闭右开,float
print(random.randint(-100,100)) #左闭右闭 int
print(random.randrange(1,4))  #左闭右开 int
l = ['hhh',12,('ss','aa',22),{'a':1,'b':2}]
print(random.choice(l)) #随机选一个
print(random.sample(l,2)) #随机选k个

l = [1,35,46,98,66,77,2,0]
random.shuffle(l)
print(l)
#

#相同种子保证每次实验生成固定的随机数，使每次实验结果一致。不同种子生成不一样的随机数。
random.seed(1)


#随机生成一个16为密码，包含大写字母，小写字母，数字，特殊字符
import string

src_upp = string.ascii_uppercase #大写字母
src_lower = string.ascii_lowercase #小写字母
src_num = string.digits #数字

print(src_upp,type(src_upp))

print(chr(65))
print(chr(33))

def pwd_generator(length = 16):
    pwd = ''
    for _ in range(length):
        random_list = random.choice([[97,122],[65,90],[48,57],[33,47]])
        rand_char = random.randint(*random_list)
        pwd += chr(rand_char)
    return pwd


def pwd_generator1(length = 16):
    digits_num = random.randint(2,6)
    upper_num = random.randint(1,8-digits_num)
    lower_num = length-digits_num-upper_num

    pwd_list = random.sample(src_num,digits_num)+random.sample(src_upp,upper_num)+random.sample(src_lower,lower_num)

    random.shuffle(pwd_list)

    new_pwd = ''.join(pwd_list)

    return new_pwd


def pwd_generator2(length=16):
    if length < 4:
        return ''
    while True:
        pwd = ''
        for _ in range(length):
            char_list = [[97, 122], [65, 90], [48, 57], [33, 47]]
            random_list = random.choice(char_list)
            random_char = chr(random.randint(*random_list))
            pwd += random_char
        l = [False for i in range(4)]   # 创建4个值都为False的列表
        # 遍历前面生成的密码,判断密码是否包含四种类型的字符,
        # 因为可能16次循环完了,碰巧缺少某一种或多种字符
        for word in pwd:
            if 97 <= ord(word) <= 122:
                l[0] = True
            if 65 <= ord(word) <= 90:
                l[1] = True
            if 48 <= ord(word) <= 57:
                l[2] = True
            if 33 <= ord(word) <= 47:
                l[3] = True
        if l[0] and l[1] and l[2] and l[3]:  # 如果四个值都为True,则返回密码
            return pwd
        print('密码不合法:', pwd)    # 如果密码没有包含4种字符,则重新生成


# pwd = pwd_generator(6)
# print(pwd)


def pwd_generator3(length=16):
    pwd = []
    for _ in range(length//4+1):
        char_list = [chr(random.randint(97, 122)),
                     chr(random.randint(65, 90)),
                     chr(random.randint(48, 57)),
                     chr(random.randint(33, 47))]
        pwd.extend(char_list)
    pwd = pwd[:length]
    random.shuffle(pwd)
    return ''.join(pwd)



print(pwd_generator(16))