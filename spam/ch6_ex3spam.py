comment = input("enter text")
if("this is me" in comment):
    spam = True
elif("he is good" in comment):
    spam = True
elif("my bad" in comment):
    spam = True
else:
    spam = False
if(spam):
    print("this is spam")
else:
    print("this is not spam")
