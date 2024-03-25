class Price():
    def payment(self,*args):

        total = 0
        count = 0

        for x in args:
            total = total + x

            count+=1

        print(f"There are {count} paramenters in this function")

        return total


obj = Price()

print(obj.payment(10))
print(obj.payment(1,2,3,4,5))

print(obj.payment(10,20,30,40,50,60,70))

print(obj.payment("Aung Aung","Zaw Zaw"))