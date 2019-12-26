from com.farsight.day2.testobject.work1 import Animal


class Dog(Animal):


    def __init__(self, name, weight):
        super().__init__(name, weight)

    def eat(self):
        print(self.name+"吃屎")

    def speak(self):
        print(self.name+"讲话 wang,wang,wang")

    def walk(self):
        print(self.name+"四只脚走路")

class Duck(Animal):

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def eat(self):
        print(self.name+"吃饲料")

    def speak(self):
        print(self.name+"说话 ga,ga,ga")

    def walk(self):
        print(self.name+"两只脚走路")

class Cat(Animal):

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def eat(self):
        print(self.name+"吃猫粮")

    def speak(self):
        print(self.name+"说话 miao,miao,miao")

    def walk(self):
        print(self.name+"不喜欢走路")

dog = Dog("snuppy",50)
dog.eat()
dog.speak()
dog.walk()

duck=Duck("donald",30)
duck.eat()
duck.speak()
duck.walk()

cat=Cat("kitty",30)
cat.eat()
cat.speak()
cat.walk()


