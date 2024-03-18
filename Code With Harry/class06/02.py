# write a program to find out wheaather 
s1 = int(input("Enter the marks of 1st subject : "))
s2 = int(input("Enter the marks of 2nd subject : "))
s3 = int(input("Enter the marks of 3rd subject : "))

if (s1+s2+s3)/3> 40 and s1 >33 and s2>33 and s3>33:
    print("the student is pass")
else:
    print("the student is fail")