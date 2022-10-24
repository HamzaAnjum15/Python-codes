sum=0
while(True):
    n=int(input("enter number"))
    if(n!=0):
        sum=sum+int(n)
        print(f"your total so far {sum}")
    else:
        print(f'your total is: {sum}')
