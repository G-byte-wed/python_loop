import csv

with open ("user.csv","w",newline="",encoding="utf-8")as f :
    writer=csv.writer(f)
    writer.writerow(["name","city","age","month"])
    writer.writerow(["Tolu","Ibadan","22","january"])
    writer.writerow(["Dara","Ibadan","18","february"])
    writer.writerow(["Gideon","Akwaibom","14","january"])   