#
l1 = ['jack', 'lucy',['mary','jimmy']]
l2 = l1
l1[0] = 'jacck'
print(l2[0])

#浅拷贝

l3 = l1.copy()
print(id(l1),id(l3))
print(id(l1[0]),id(l1[1]),id(l1[2]))
print(id(l3[0]),id(l3[1]),id(l3[2]))

#浅拷贝只是重新开辟了一块空间，但实际存放的内容仍是原来内容的引用

l3[0] = 'mark'
l3[1] = 'mask'

l3[2][0] = 'alone'
l3[2][1] = 'lonely'

print(l1)#['jacck', 'lucy', ['alone', 'lonely']]
print(l3)#['mark', 'mask', ['alone', 'lonely']]
#因为第一层引用直接指向了字符串，是不可变类型，所以导致直接开辟新的内存空间，改变了l3的引用
#第二层是间接引用，改变了第二层引用，但l1与l3通过同一个一级引用找到了这片内存区域所以l1与l3的第二层列表值是一样的

l1 = ['jack', 'lucy',['mary','jimmy']]
import copy

l3 = copy.deepcopy(l1)
print(id(l1),id(l3))
print(id(l1[0]),id(l1[1]),id(l1[2]))
print(id(l3[0]),id(l3[1]),id(l3[2]))


l3[0] = 'mark'
l3[1] = 'mask'

l3[2][0] = 'alone'
l3[2][1] = 'lonely'

print(l1)#['jack', 'lucy', ['mary', 'jimmy']]
print(l3)#['mark', 'mask', ['alone', 'lonely']]


