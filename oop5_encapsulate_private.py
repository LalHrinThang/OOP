class Parent():
    def __init__(self,age) -> None:
        self.__age = age

class Child(Parent):
    def modify(self,age):
        self.__age = age
        return self.__age
    
    def printdata(self):
        print(self.__age)

obj = Child(100)

print(obj.__dict__)
###########################
#print(obj.__age)
###########################
obj.modify(20)
print("After Modification : {0}".format(obj.__dict__))
obj.printdata()



class Animal():
    def __init__(self,name,age,color) -> None:
        self.__name = name
        self.__age = age
        self.__color = color

class Dog(Animal):
    def dmodify(self,name,age,color):
        self.__name = name
        self.__age = age
        self.__color = color

    
    def printdata(self):
        print(self.__name,self.__age,self.__color)

obj = Dog("Chito",3,"Black")

print(obj.__dict__)

obj.dmodify("Blacky",4,"Black")

print(obj.__dict__)

obj.printdata()