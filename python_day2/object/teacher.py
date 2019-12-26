

class Teacher():
    username = "张老师" #public
    _age = "35" #protected
    __money = 8000 #private

    def printUserName(self):
        print("姓名：",self.username)
        self.__printMoney()
    def _printAge(self):
        print("年龄：",self._age)
        self.__printMoney()
    def __printMoney(self):
        print("薪水：",self.__money)

t=Teacher() #实例不能调用它的私有变量
print(t.username)
print(t._age)
#print(t.__money)
t.printUserName()
t._printAge()
#t.__printMoney() 可以用
