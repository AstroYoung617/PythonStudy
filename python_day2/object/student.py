from com.farsight.day2.object.person import Person
from com.farsight.day2.object.user import User

#多重继承的应用
class Student(User,Person):
    def __init__(self,username,userage,usersex,phone,address):
        #self.username = username
        #self.userage = userage
        #self.usersex = usersex
        User.__init__(self,username,userage,usersex)#调用父类的构造器
        Person.__init__(self,phone,address)#调用父类的构造器

    def printUser(self):#重写方法
        super().printUser()

    def printPerson(self):#重写方法
        super().printPerson()


if __name__ == "__main__":
    s = Student("jack",25,"男","1564*****","西华大学")
    s.printUser()
    s.printPerson()

