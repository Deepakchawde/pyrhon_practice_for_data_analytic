# wap to find the factorial of a  given numeber

num= int(input("Enter the number to find the factorial of :  "))
factorial=1
for i in range(1, num+1):
    factorial= factorial*i

print(f"the factorial of {num} is {factorial}")