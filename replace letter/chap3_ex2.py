letter = ''' Dear <|NAME|>\n your are selected!\n <|DATE|>'''
print(letter)
name = input("enter your name\n")
date = input("enter date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)