


print("-------------作用域概念-------------")
total =0
#total为全局变量
def computer(var1,var2,var3):#var1,var2,var3为局部变量
    sum=var1+var2+var3
    jian=var1-var2-var3
    mul = var1*var2*var3
    div=var1/var2/var3
    return sum,jian,mul,div

def computer2():
    print(total)
    #print(var1,var2,var3)

print(computer(10,20,30))

