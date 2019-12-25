

def printHello(str): #自由变量
    def print2(str2): #内嵌函数
        return str + str2
    return print2#返回了内嵌函数

func = printHello("hello")
print(func("world"))

print("-------------装饰器-------------")

def demo():
    return "hello world"

def addb(func):
    def wrapper():
        return "<b>"+func()+"</b>"
    return wrapper
def addli(func):
    def wrapper():
        return  "<li>"+func()+"</b>"
    return wrapper

@addb
@addli
def demo():
    return "hello world"

print(demo())