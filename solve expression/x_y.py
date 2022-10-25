# Write a Python program to solve (x + y) * (x + y).
x=int(input("input first number "))
y=int(input("input second number "))
def x_y(x,y):
    result= (x+y)*(x+y)
    b=str(f"({x}+{y})*({x}+{y})={result}")
    return b
print(x_y(x,y))