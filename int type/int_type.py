#  Write a Python program to add two objects if both objects are an integer type.
a = input()
b = input()


if not (isinstance(a,int) and isinstance(b,int)):
    print("must be integer")
else:
    print(a+b)
