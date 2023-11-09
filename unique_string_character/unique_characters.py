#Write a function to determine if a given string has all unique characters.
# That is, check if the string doesn't have any repeated characters. 
#You can assume that the input string only contains lowercase letters. 
#Please provide your solution.
str1 = str(input("enter string: "))
str2 = ""
for char in str1:
    if char in str2:
        print("Not unique characters")
        break
    else:
        str2 += char
print("All characters are unique")