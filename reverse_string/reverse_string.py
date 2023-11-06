# def reverse_string(input_string):
input_string = str(input("Enter a string: "))
reversed_str = ""
for i in input_string:
        reversed_str = i + reversed_str
print(reversed_str)

# # Example usage:
# original_string = "Hello, World!"
# reversed_string = reverse_string(original_string)
# print(f"Original string: {original_string}")
# print(f"Reversed string: {reversed_string}")
