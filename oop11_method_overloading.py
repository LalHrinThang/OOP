from abc import ABC, abstractmethod

class Price(ABC):
    def slip(self,amount):
        print(f"Payment Amount : {amount} $")

    @abstractmethod

    def payment(self):
        print("This is import from abstract method")


class CreditCard(Price):
    def payment(self,amount):
        super().payment()

        print(f"Payment with CreditCard : {amount} $")

class MobileBanking(Price):
    def payment(self,amount):
        """This is  Abstraction"""
        super().payment()
        print(f"Payment with MobileBanking : {amount}")

obj = CreditCard()
obj.slip(3000)

obj.payment(3500)

obj2 = MobileBanking()
print(obj2.payment.__doc__)
obj2.slip(5000)

obj2.payment(2500)    
