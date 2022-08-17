#显式布尔值False
#隐式布尔值0,None，空值('',[],{})

#  and 与
#  or 或
#  not 非

# girl_friend = 'human'
# gender = input('性别：')
# age = 18


# print(16 < age < 88)
# print(age > 17 and gender == 'male')
# print(not 0)
# print(not ())

#优先级 not > and > or


#成员运算符 in
print('1'in'123')

l = [12,24,36]
print(12 in l)

dic = {
    'name':'jack',
    'age':19
}
print('name' in dic)
print('12'not in'3655156123654')
print(not '12' in '335422442199')



is_human = input('是不是人：是就写human')
gender = input('your gender: male or female')
age = int(input('your age:'))

if is_human == 'human' and gender == 'female' and 16 < age < 88:
    print('结婚')
else:
    print('结不了')

score=int(input('your score is:'))

if score < 60:
    print('failed')
elif score <= 70:
    print('good')
else:
    print('excellent')
