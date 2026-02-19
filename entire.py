with open ("notes,txt","r",encoding="utf-8")as my__file__:
    content=my__file__.read()
    print(content)
    #line by line
    for line in my__file__:
        print(line.strip())