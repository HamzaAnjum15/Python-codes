a = int(input("enter marks of physics"))
b = int(input("enter marks of ics"))
c = int(input("enter marks of maths"))

# if(a<33):
#     print("fail")
# else:
#     print("pass")
# if(b<33):
#     print("fail")
# else:
#     print("pass")
# if(c<33):
#     print("fail")
# else:
#     print("pass")
#     f1 = a+b+c
# if(f1<120):
#     print("fail")
# else:
#     print("pass")
if(a<33 or b<33 or c<33):
    print("you are fail because of less passing marks")
elif(a+b+c)/3<40:
    print("you are fail due to less than 40%")
else:
    print("you are pass")