def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase to make the comparison case-insensitive
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted strings are equal
    return sorted(str1) == sorted(str2)

# Example usage:
string1 = "listen"
string2 = "silent"
result = are_anagrams(string1, string2)

if result:
    print(f"'{string1}' and '{string2}' are anagrams.")
else:
    print(f"'{string1}' and '{string2}' are not anagrams.")
