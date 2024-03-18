# WAP to find the factorial of the given number

num = int(input("enter the number to find the factorial : "))
factorial=1
for i in range(1,num):
    factorial= factorial * i

print(f"the factorial of the number {num} is {factorial}")
