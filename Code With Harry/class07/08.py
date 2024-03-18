# WAP to find the sum of the given number enter by the User

num = int(input("Enter the number to  find the sum of natural numbers: "))
sum = 0
for i in range(1, num):
    sum = sum+i
print(f"the sum of natural numeber {num} is {sum}")