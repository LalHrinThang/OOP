class Price:
    def payment(self,x = None,y = None):
        if x != None and y != None :
            return x * y
        elif x!=0:
            return x * x
        else:
            return None
        

obj = Price()

print(obj.payment(10))

print(obj.payment(20,20))

print(obj.payment(1,2,3,4,5))