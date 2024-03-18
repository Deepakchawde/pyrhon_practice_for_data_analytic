# WAP to right the function   to print a multlipacation table


def multiply(number):
    for i in range(1,11):
        print(f"{number} x {i} = {number*i}")
    return 


a = int(input("Enter the numnber to print the table of the number "))
z= multiply(a)
print(z)
