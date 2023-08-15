oldname=input("enter the old name")
new=input("enter new")
with open(oldname,"r") as f:
    text=f.read()
with open(new,"w") as f:
    f.read(text)
    