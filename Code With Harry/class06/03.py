# spam detector in python

txt = input("Enter the text to check wheater it is spam or not \n")

if ("make a lots of money" in txt):
    spam=True
elif ("Buy now" in txt):
    spam=True
elif ("suscribe now "in txt):
    spam=True
elif ("click this"in txt):
    spam=True
else:
    spam=False

if spam==True:
    print("there is a spam in the text be alert  ")
else:
    print("Just chill there is no spam in the text")