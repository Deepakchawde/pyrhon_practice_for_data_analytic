# wap to find the number is prime or not

num = int(input("Enter a number to find the number is prime or not : "))
prime= True
for i in range(2,num):
    if(num%i==0):
        prime= False
        break

if  prime:
    print("The numeber is prime:  ")
else:
    print("The numebr is not primw")