s = {1,23,2,1,1,2,33}
print(s,type(s))

a = set([2,2,22,2,3])
print(a,type(a))


#关系运算 &
hobbies1 = ['a','b','c','c','e','f']
hobbies2 = ['a','c','e']
both_hobbies = []
for i in hobbies1:
    if i in hobbies2 and i not in both_hobbies:
        both_hobbies.append(i)

#使用集合
hobbies1 = {'a','b','c','c','e','f'}
hobbies2 = {'a','c','e'}
both_hobbies = {}

#取交集
both_hobbies = hobbies1 & hobbies2
print(both_hobbies)

#取并集
all_hobbies = hobbies1 | hobbies2
print(all_hobbies)

#取差集
m_hobbies1 = hobbies1 - hobbies2
m_hobbies2 = hobbies2 - hobbies1


#对称差集
print(m_hobbies1 | m_hobbies2)
print(hobbies1^hobbies2)

#父子集

print(hobbies1 > hobbies2)
print(hobbies1 < hobbies2)
print(hobbies1 == hobbies2)

#内置方法
both_hobbies =  hobbies1.intersection(hobbies2)#交集
all_hobbies = hobbies1.union(hobbies2)#并集
m_hobbies1 = hobbies1.difference(hobbies2)#差集
m_hobbies2 = hobbies2.difference(hobbies1)

print(hobbies1.symmetric_difference(hobbies2))#对称差集
print(hobbies1.issuperset(hobbies2))#父集
print(hobbies2.issubset(hobbies1))#子集



#去重
l = [1,2,2,1,3,5,7]
print(set(l))

info = [
    ['jack',18],
    ['lucy',19],
    ['mike',20],
    ['jack',18]
]
info_new = []
for i in info:
    if i not in info_new:
        info_new.append(i)
print(info_new)


#len()
#in not in 
#循环遍历

#update
s = {1,2,3}
s.update([4,5,6])
print(s)
s1 = {1,4,5}
s.intersection_update(s1)
print(s)

#clear(),pop(),copy()
#remove(), discard()
s.remove(4)
s.discard(4)#没有这个元素也不报错
print(s)

#add()
s.add(6)
print(s)

#isdisjoint
s = {1,2,3}
s1 = {4,5,6}
print(s.isdisjoint(s1))