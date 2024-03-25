class Price():
    def payment(self,type,*args):
        if type == "int":
            data = 0

            count = 0
            for i in args:
                data = data + i
                count += 1
            print("This is interger type")

            print(f"There are {count} parameters in this function")

            return data

        else:
            data = ""

            count = 0
            for i in args:
                data = data + i
                count += 1
            print("This is String type")

            print(f"There are {count} parameters in this function")

            return data
        
obj = Price()
print(obj.payment("int",10))
print(obj.payment("int",1,2,3,4,5))

print(obj.payment("int",10,20,30,40,50,60,70))

print(obj.payment("str","Aung Aung ","Zaw Zaw"))