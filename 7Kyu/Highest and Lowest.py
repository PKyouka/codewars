def high_and_low(numbers):
    numbers = list(map(int, numbers.split()))
    return f"{max(numbers)} {min(numbers)}"