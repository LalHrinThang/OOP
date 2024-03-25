#Encapsulate Protected


class Parent():
    def __init__(self,age) -> None:
        self._age = age

class Child(Parent):
    def getAge(self):
        print(self._age)


obj = Child(100)

obj.getAge()