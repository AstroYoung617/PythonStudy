from com.farsight.day2.testobject.work2 import SchoolMember


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def tell(self):
        super().tell()
        print("薪水：",self.salary)

tea = Teacher("张三","20","8000")
tea.tell()

