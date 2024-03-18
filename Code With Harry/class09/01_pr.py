f= open("poem.txt")
a=f.read()
if "twinkle " in a :
    print("is present ")
else:
    print("not present")
f.close()
