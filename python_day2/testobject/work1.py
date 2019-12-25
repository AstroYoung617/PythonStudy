

class Animal():
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
        print("姓名：",self.name,"体重：",self.weight)
    def eat(self):
        print(self.name+"吃")

    def speak(self):
        print(self.name+"说话")

    def walk(self):
        print(self.name+"走路")
