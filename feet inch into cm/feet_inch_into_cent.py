# Write a Python program to convert height (in feet and inches) to centimeters.
ft=int(input("enter feet: "))
inch=int(input("enter inches "))
cent1=ft*30.48
cent2=inch*2.54
height=cent1+cent2
print(f"the height in centimeter is {height}cm")
