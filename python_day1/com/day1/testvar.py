

username="张三" #public
_age = 25 #protected
__sex = "男" #private

if username == "张三":
    print("welcome")
    print(True)
    if __sex == "男":
        print("帅哥")
    else:
        print("美女")
else:
    print("not welcome")
    print(False)

one = 100
two = 200
three =300
total = one+two+three

list1 = ["hello","the","world"]

print(total)
print(list1)
a,b,c = 1,2,"jhno"
print(a,b,c)