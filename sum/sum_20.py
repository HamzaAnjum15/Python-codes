# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20. 
a=int(input("enter first number "))
b=int(input("enter second number "))
def sum(a,b):
    c=a+b
    if c>=15 and c<=20:
        return 20
    else:
        return a+b
print(sum(a,b))