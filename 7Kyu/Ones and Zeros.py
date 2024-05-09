def binary_array_to_number(arr):
    for i in range(len(arr)):
        if arr[i] == 1:
            arr[i] = 2**(len(arr)-1-i)
    return sum(arr)