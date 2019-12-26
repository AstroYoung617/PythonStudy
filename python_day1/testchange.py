

string = "abc"
string2 = "123"

print(int(string2)) #变量为数字型字符串才能转型
#print(int(string)) 不能转型

list1 = [1,2,3,4,5,6]
list2 = ["11","22","33","44"]
tuple1 = ("aa","bb","cc")
dic = {1:"hello",2:"the",3:"world"}

print(tuple(list1)) #数组转元祖

print(list(tuple1)) #元祖转数组

print(dict(list2))  #数据转字典

print(dict(tuple1)) #元祖转字典

if"11" in list2:
    print("11在序列中")
else:
    print("11不在序列中")
if"aa" not in tuple1:
    print("aa在序列中")
else:
    print("aa不在xuliez")

string1 = "aaa"
string2 = "aaa"
if string1 is string2:
    print("两者引用相同")
else:
    print("两者引用不同")

