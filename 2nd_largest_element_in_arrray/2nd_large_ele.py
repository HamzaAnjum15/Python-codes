my_array = [1,5,6,2,7,3,10,11,8,12,80,79]
# input_ = input(my_array)
largest_element = second_largest_element = float('-inf')
i = 0
for i in my_array:
    if i > largest_element:
        second_largest_element =largest_element
        largest_element = i
    elif i > second_largest_element and i < largest_element:
        second_largest = i
print(second_largest_element)

