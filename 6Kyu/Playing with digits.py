def dig_pow(n, p):
    for i in range(len(str(n))):
        if i == 0:
            sum = int(str(n)[i]) ** (p + i)
        else:
            sum += int(str(n)[i]) ** (p + i)
    if sum % n == 0:
        return sum // n
    else:
        return -1

print(dig_pow(89, 1)) # 1
print(dig_pow(92, 1)) # -1
print(dig_pow(46288, 3)) # 51
print(dig_pow(41, 5)) # 25
print(dig_pow(46288, 6)) # 51
