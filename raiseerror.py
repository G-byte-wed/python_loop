age=int(input("what is your age"))
if age <0:
    raise ValueError("Age cannot be  negative")
if age > 120:
    raise ValueError("Age seems unrealistic")
print(f"Age{age}is okey")