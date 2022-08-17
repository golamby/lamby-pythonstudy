#函数嵌套
#1.定义时嵌套(装饰器)
#2.调用时嵌套，递归

sum = 0
i = 10

def func():
    global sum,i
    sum += i
    i -= 1
    if i == 0:
        return
    func()
print(func)

def func(i):
    if i == 0:
        return i
    return i + func(i - 1)

print(func)
print(func(10))


l = [1,2,[3,[4,[5,[6,[7,[8,[9,[10,[11,12]]]]]]]]]]
#打印出l中所有的数字
#这个时候写for循环再判断，会发现逻辑代码一直重复

def fun(li):
    for i in li:
        if type(i) is list:
            fun(i)
        else:
            print(i)

fun(l)


#'abcd'全排列
s = 'abcd'
l = list(s)

def permutation(l,level):
    if level == len(l):
        print(l)
    for i in range(level,len(l)):
        l[level],l[i] = l[i],l[level]
        permutation(l,level+1)
        l[level],l[i] = l[i],l[level]

permutation(l,0)

#冒泡排序的过程
def mao_pao(num_list):
    num_len = len(num_list)

    for i in range(num_len):
        sign = False
        
        for j in range(num_len - 1 - i):
            if num_list[j] > num_list[j+1]:
                num_list[j],num_list[j+1] = num_list[j+1],num_list[j]
                sign = True

        print(num_list)
        if not sign:
            break 
a = [2,213,43,34,65,98,1,34,6,22,22]
mao_pao(a)


