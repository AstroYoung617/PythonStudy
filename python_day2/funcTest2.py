

print("----------值传递（数字、字符串、元组）相当于只对副本做了修改,对其值本身未作修改------------")
number = 100
tuple1 = (1,2,3)
string = "hello world"

def changeNumber(n):
    n=100
    return n

result=changeNumber(number)
print(result)
print(number)

def changeString(str):
    str=str+" nihao"
    return str

result=changeString(string)
print(result)
print(string)

result=changeNumber(tuple1)
print(result)
print(tuple1)

print("-----------引用传递（数组、列表）会修改其引用的数据-----------")

li=["hello"]

def changelist(list1):
    list1.append("world")
    return list1

changelist(li)
print(li)

