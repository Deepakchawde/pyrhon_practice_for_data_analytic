letter = ''' Dear <|Name|>
        you are selected !
        <|Date|>'''

name = input("enter your name :  ")
date = input("enter todays date :  ")

letter= letter.replace("<|Name|>",name)
letter= letter.replace("<|Date|>",date)

print(letter)