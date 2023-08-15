#l=[1,3,5,7,]
#for i in l:
#print(i)
#print("\n")
#for i in range(1,30,2):
 #   print(i)
n=int(input("enter your number"))
for i in range(1,n):
    for j in range(0,n-i-1):
        print(" ",end="")
    for k in range(0,2*i-1):
        print("*",end="")
    for l in range(0,n-i):
        print(" ",end="")
    print("\n",end="")