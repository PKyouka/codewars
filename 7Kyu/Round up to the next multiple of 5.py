def round_to_next5(n):
    if n % 5 == 0:
        return n
    elif n % 5 == 1:
        return n + 4
    elif n % 5 == 2:
        return n + 3
    elif n % 5 == 3:
        return n + 2
    elif n % 5 == 4:
        return n + 1