def sum(n):
    if (n==1):
        return 1
    else:
        return n + sum(n-1)
s= sum(76)
print("the sum of first n natural no is "+ str(s))