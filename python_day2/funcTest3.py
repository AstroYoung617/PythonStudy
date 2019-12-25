from functools import reduce

print("-------------排序：sorted函数------------")
li=[13,234,1213,23,12,3342,213]

def sortedTest(li):
    return li
print(sorted(li,key=sortedTest,reverse=True))

print("------------------映射：map函数------------------")
li2=[1,2,3,4,5,6,7,8]

def mapTest(x):
    return x*x
print(list(map(mapTest,li2)))

print("-------------------求和：reduce函数-------------------")

li3=[1,2,3,4,5,6,7,8,9,10]

def reduceTest(x,y):
    return x+y
print(reduce(reduceTest,li3))

print("-----------------过滤器:filter函数----------------")
li4=[15,354,84,241,56,7,152,478]

def filterTest(li):
    z=lambda x:x <=200 and x%2 ==0
    f=filter(z,li)
    return list(f)
print(filterTest(li4))