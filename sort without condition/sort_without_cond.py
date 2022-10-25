# Write a Python program to sort three integers without using conditional statements and loops.
a = int(input("enter 1st number "))
b = int(input("enter 2nd number "))
c = int(input("enter 3rd number "))
x = min(a, b, c)
y = max(a, b, c)
z = (a+b+c)-x-y
print("the numbers in sorted  ", x, z, y)
