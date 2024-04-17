def sum_str(a, b):
    return str(sum(int(x) for x in [a, b] if x.isnumeric()))
