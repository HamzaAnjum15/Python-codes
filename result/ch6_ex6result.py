a = int(input("enter your marks"))
if(a>80):
    a = "excellent"
elif(a>70):
    a = "A"
elif(a>60):
    a = "B"
elif(a>50):
    a = "C"
elif(a>100):
    a = "error"
else:
    a= "fail"
print("your result is " + a )