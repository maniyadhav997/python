n=int(input("enter the number"))
def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)
a=factorial(n)
print(a)

