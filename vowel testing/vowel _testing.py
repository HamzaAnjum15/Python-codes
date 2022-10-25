# Write a Python program to test whether a passed letter is a vowel or not.
from re import U


v='aeiou'
p=str(input("enter an alphabet "))
if p in v:
    print("vowel")
else:
    print("not a vowel")