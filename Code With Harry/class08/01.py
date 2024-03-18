# WAP to find the greatest of three number

def maximun(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c

a= int(input("Enter the value of a :  "))
b= int(input("Enter the value of b :  "))
c= int(input("Enter the value of c :  "))

z=maximun(a,b,c)

print("the maximum of the given is " , str(z))
