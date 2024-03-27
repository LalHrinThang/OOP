#try: except: else: finally: raise: ownErrorCreation:

class OwnExcept(Exception):
    pass

class Err404(OwnExcept):
    pass
class Err808(OwnExcept):
    pass


try:
    d = int(input("Enter a Number : "))

    if d == 20:
        raise Err404
    elif d == 10:
        raise Err808
    elif d == 0:
        raise ZeroDivisionError
    
except ZeroDivisionError:
    print("Zero Division Error")

except Err404:
    print("404 Error")

except Err808:
    print("808 Error")

except Exception as err:
    print(f"This is exception method : {err}")

finally:
    print("This is all methods of error handling")