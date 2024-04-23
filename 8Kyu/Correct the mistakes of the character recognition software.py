def correct(s):
    for _ in s:
        s = s.replace('5', 'S')
        s = s.replace('0', 'O')
        s = s.replace('1', 'I')
    return s


print(correct("k3n5y"))