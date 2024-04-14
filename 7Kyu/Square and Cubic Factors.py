def factors(n):
    square = []
    cube = []
    for i in range(2, n+1):
        if n % i == 0:
            if n % (i**2) == 0:
                square.append(i)
            if n % (i**3) == 0:
                cube.append(i)
    return [square, cube]