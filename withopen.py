import csv

with open ("user.csv","r",encoding="utf-8") as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)