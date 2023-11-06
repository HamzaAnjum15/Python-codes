# Write a function to check if a string is a palindrome.
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward. 
#For example, "racecar" and "level" are palindromes.
def is_palindrome(s):
    # Remove spaces and convert the string to lowercase for a case-insensitive comparison
    s = s.replace(" ", "").lower()
    
    # Compare the original string with its reverse
    if s == s[::-1]:
        return True
    else:
        return False

# Test cases
input_string = "racecar"
if is_palindrome(input_string):
    print(input_string, "is a palindrome.")
else:
    print(input_string, "is not a palindrome.")

input_string = "hello"
if is_palindrome(input_string):
    print(input_string, "is a palindrome.")
else:
    print(input_string, "is not a palindrome.")
