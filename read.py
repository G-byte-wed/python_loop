with open("notes.txt","r+",encoding="utf") as doc:
    content=doc.read()
    doc.seek(0) #GOTO line one
    doc.write("UPDATED:"+content)