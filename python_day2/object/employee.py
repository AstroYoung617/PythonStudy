

#object是java里面最大的类也是python中的
class Employee(object):
    employCount = 100 #类变量
    def __init__(self,username,money): #构造器
        self.username = username
        self.money = money
        self.employCount += 100

    def printEmploy(self): #实例方法（self代表一个类的实例）
        print("职员号：",self.employCount,"职员姓名：",self.username,"职员薪水：",self.money)

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)

    def __str__(self) -> str: #重写的方法
        return super().__str__()


if __name__=="__main__": #主函数为程序入口
    employee = Employee("张三",8000)
    e2=Employee("李阳",20000)
    employee.printEmploy()
    e2.printEmploy()
    print(employee.__eq__(e2))
    print(employee.__str__())
    print(e2.__doc__)    #文档字符串
    print(e2.__dict__)   #取出所有的成员变量
    print(e2.__module__) #打印出主函数名称