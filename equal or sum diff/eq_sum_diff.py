# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
a=int(input("enter 1st number "))
b=int(input("enter second number "))
def diff(a,b):
    if a==b or a+b==5 or abs(a-b==5):
        return True
    else:
        return a+b
print(diff(a,b))