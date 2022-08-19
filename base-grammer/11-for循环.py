# for 变量名 in 可迭代对象：
#   子代码块
#可迭代对象可以是列表，字符串，字典，元组，集合

l = ['a','bs4解析','c','d']
for item in l:
    print(item)

#使用while循环
i = 0
while i < 4:
    print(l[i])
    i += 1


#循环遍历字典：
dic = {'name':'jack',
       'age':18,
       'height':180
}
for i in dic:
    print(i,type(i),dic[i])


#遍历字符串
str = 'jackhhh'

for i in str:
    print(i + '*')

i = 0
while i < len(str):
    print(i,str[i])
    i+=1

#python3的range函数返回了一个可迭代对象
#打印的时候会直接打印range这个对象而不是一个list
l = list(range(1,9))
print(l)
l = list(range(9))
print(l)
l = list(range(1,9,2))
print(l)



# for i in range(10):
#     print('外层循环--',i)
#     for j in range(3):
#         print('内层循环---',j)

for i in range(1,10):
    for j in range(1,i+1):
        #print('{0}*{1}={2}'.format(i,j,i*j),end=' ')
        print(f'{i}*{j}={i*j}',end=' ')
        #print(i,'*',j,'=',i*j ,end=' ')
    print()