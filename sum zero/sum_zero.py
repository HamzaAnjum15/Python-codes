# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
def sum(x,y,z):
    if x==y or x==z or y==z:
        return 0
    else:
        return x+y+z
print(sum(1,2,3))
print(sum(1,2,2))
print(sum(2,2,3))