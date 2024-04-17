def invert(lst):
    for i in range(len(lst)):
        lst[i] = -lst[i]
    return lst

print(invert([1,2,3,4,5]))