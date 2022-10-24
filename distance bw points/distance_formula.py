#  Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
import math

x1=int(input("enter x1 "))
y1=int(input("enter y1 "))
x2=int(input("enter x2 "))
y2=int(input("enter y2 "))
def distance(x1,y1,x2,y2):
    result=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return result
print(distance(x1,y1,x2,y2))

    
