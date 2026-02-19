try:
    number=int(input("enter number:"))
    result= 100/number
    print(f"100/{number}={result}")
except ValueError:
    print("that is not a valid number")
except ZeroDivisionError:
    print(f"cannot be divided by {number}")
except Exception as e:
    print(f"something went wrong:{e}")
else:
    print("calculator sucessful")
finally:
    print("Tis always runs")