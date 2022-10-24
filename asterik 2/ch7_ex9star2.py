n = 3
for i in range(3):
    print("*" * (i+1), end="")
    print(" " * "*" * (n-i-2) * " ", end="")
    print("*" * (i+1))