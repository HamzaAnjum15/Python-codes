def has_duplicates(arr):
    seen = []
    for item in arr:
        if item in seen:
            return True
        seen.append(item)
    return False

# Example usage:
my_array = [1, 2, 3, 4,4, 5]
if has_duplicates(my_array):
    print("The array contains duplicates.")
else:
    print("The array does not contain duplicates.")
