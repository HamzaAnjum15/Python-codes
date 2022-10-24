from tkinter import N


num=int(input("enter a number "))
def near_thousand(num):
    return (abs(1000-num) <=100) or (abs(2000-num)<=100)
# print(near_thousand(1000))
# print(near_thousand(900))
# print(near_thousand(700))
# print(near_thousand(22000))
print(near_thousand(num))