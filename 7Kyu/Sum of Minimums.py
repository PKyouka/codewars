def sum_of_minimums(numbers):
    for i in range(len(numbers)):
        numbers[i] = min(numbers[i])
    return sum(numbers)