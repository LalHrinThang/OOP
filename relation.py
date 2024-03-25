class Parent:
    pass
class Child(Parent):
    pass

print(issubclass(Child,Parent))

objofChild = Child()

print(isinstance(objofChild,Child))

print(isinstance(objofChild,Parent))