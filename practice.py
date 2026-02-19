try:
    number=int(input("enter number"))
    resilt=20/number
    print(f"20/{number}={result}")
except ValueError:
    print("this number is invalid ")
except ZeroDivisionError:
    print (f"cannot be duvuded by {number}")
except Exception as e:
    print(f"something went wrong")
except SyntaxError:
    print("value cannot be calculated")
else:
    print("calculation successful")
finally:
    print("GG,u can do this")
