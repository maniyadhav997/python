with open("file.txt","r") as f:
    text=f.read()
    text.replace("mankey","###")
    f.write(text)