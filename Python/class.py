class Employee:
    name="harry"
    marks=34
    def printObj(self):
        print(f"this is class{self}")
o=Employee()
s=Employee()
print(o.marks)
o.printObj()
s.printObj()