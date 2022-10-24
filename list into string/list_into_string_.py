# Write a Python program to concatenate all elements in a list into a string and return it.


def convo(list):
    result = ''
    for element in list:
        result += str(element)
    return result


print(convo([1, 5, 12, 24,55]))

