def persistence(n):
    count = 0
    while n > 9:
        n = eval('*'.join(str(n)))
        count += 1
    return count