def min_value(digits):
    for i in digits:
        if digits.count(i) > 1:
            digits.remove(i)
    return int(''.join(map(str, sorted(digits))))