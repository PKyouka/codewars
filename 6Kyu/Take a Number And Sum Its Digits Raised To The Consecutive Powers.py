def sum_dig_pow(a, b):
    result = []
    for i in range(a, b + 1):
        if i == sum([int(str(i)[j])**(j+1) for j in range(len(str(i)))]):
            result.append(i)
    return result