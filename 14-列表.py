

msg = ['jack',18,190,False]
#实际上时调用了：
list(['jack',18,190,False])
print(msg,type(msg))

#list(可迭代对象)，这里和for循环需要遍历的内容是一致的，range那里也提到过，凡是可迭代对象均可以使用list(),转为列表

print(list('hello'))
print(list({'name':'jack','age':18,'height':1.88}))

person = {'name':'jack','age':18,'height':1.88}
#列表的内置方法：
#按索引取值，追加，插入，extend，
l = ['李白','杜甫','王维','李商隐']

l.append('王安石')
print(l)

l.insert(0,'ybc')
print(l)

l2 = ['赵云','马超','关羽']
#l.append(l2)#['ybc', '李白', '杜甫', '王维', '李商隐', '王安石', ['赵云', '马超', '关羽']]整体嵌套
#print(l)
# for i in l2:
#     l.append(i)
# print(l)
print(id(l+l2),l+l2)
l.extend(l2)
print(id(l),l)


l.extend('he')
l.extend(person)
print(l)

#删除

name =['jack','lucy','mike','jason']
del name[0]
print(name)

#不传参默认删除最后一个
res = name.pop(0)
print(res,name)

#count,index,clear
l = [1,1,2,3,1,3,36,1]
print(l.index(1,2))

#sort
l=[74,95,66,34,88]
l.sort(reverse = True)
print(l)


#模拟数据结构，队列和堆栈

#队列,入队append(),出队pop(0)

l = [12,35,54,13,16,88]
l.append(22)
l.append(11)

print(l)

l.pop(0)
l.pop(0)
print(l)

#堆栈
#入栈操作一致，出栈使用pop()
l.pop()
print(l)




