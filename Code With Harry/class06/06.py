# wap to calculate the grade of a marks in text exam

marks= int(input("enter the marks optian in the text "))

if marks>=90:
    grade="Ex"
elif marks>=80:
    grade="A"
elif marks>=70:
    grade="B"
elif marks>=60:
    grade="C"
elif marks>=50:
    grade="D"
else:
    grade="F"

print("the grade you have optain is "+ str(grade))