total=1500
t=0
n=int(input('how many members? '))
while(t!=n):
    a=str(input("whats your name"))
    b=int(input("whats your age"))
    t=t+1
    if(t==n):
        if(b>60):
            total=750
        else:
            total=1500
        print(f"your amount is {n*total}")
    

        

