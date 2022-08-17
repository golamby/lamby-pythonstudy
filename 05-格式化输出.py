#格式化字符串

#1.占位符%s
#按位置传值


str = 'my name is %s, I am from %s'%('jack','america')
print(str)

str = 'my name is %s'%'jack'
print(str)
#通过字典按key传值

str = 'my name is %(name)s, I am from %(hometown)s'%{'name':'jack','hometown':'america'}
print(str)


str = 'my name is %s'%'jack'
str = 'my name is %s'%18
print(str)
str = 'my name is %s'%['a','b']
print(str)


#2.%d
str = 'my age is %d'%18
print(str)



#python内置的str的方法format

str = 'my name is{},my age is{}'.format('jack',18)
print(str)
str = 'my name is{0}{0}{0},my age is{1}'.format('jack',18)
print(str)
str = 'my name is{name},my age is{age}'.format(name='jack',age=18)
print(str)


#format格式化填充

print('{0:*^10}'.format('开始'))
print('{num:.2f}'.format(num=12.235))

#f
name = input('your name is')
hometown = input('your hometown is')
str = f'name is {name}, hometown is {hometown}'
print(str)




