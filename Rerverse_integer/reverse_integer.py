num = int(input("Ente a value: "))
ans = 0
while(num!=0):
    digit = int(num % 10)
    
    ans =int( (ans * 10) + digit)
    num =int( num / 10)
print(ans)
# n = int(1 / 10)
# print(n)