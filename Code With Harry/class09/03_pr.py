# wap to genrate a table of 5 and print it on another file 
f= open("table.txt","w")

for i in range(1,11):
    f.write(f"5 X {i} = {5*i}\n")
    

# f.write(a)

f.close()