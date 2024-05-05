def positive_sum(arr):
    for i in arr:
        if i < 0:
            arr.remove(i)
    return sum(arr)

print(positive_sum([1, -4, 7, 12]))