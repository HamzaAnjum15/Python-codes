def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Example usage:
my_array = [1, 2, 3,4,5]
reverse_array(my_array)
print(my_array)
