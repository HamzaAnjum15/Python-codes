def reverse_list(input_list):
    reversed_list = []
    for item in input_list:
        reversed_list.insert(0,item)
    return reversed_list

# Example usage:
original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print(f"Original list: {original_list}")
print(f"Manually reversed list: {reversed_list}")

