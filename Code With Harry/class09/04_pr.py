# WAP to find the text and replace it by ####

with open("sam.txt",'r') as f:
    content= f.read()

content= content.replace("donkey","#$%^&&*")


with open("sam.txt",'w')as f:
    content=f.write(content)