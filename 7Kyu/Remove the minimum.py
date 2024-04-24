def remove_smallest(numbers):
    if numbers == []:
        return []
    else:
        numbers_copy = numbers.copy()
        min_number = min(numbers_copy)
        numbers_copy.remove(min_number)
        return numbers_copy