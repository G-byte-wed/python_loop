score=int(input("what did u score"))
if score<0:
    raise ValueError("less than 0 is not accepted in marking")
if score> 50:
    print ("pass")
print ("you tried your best")