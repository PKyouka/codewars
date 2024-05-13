def diamond(n):
    if n < 0 or n % 2 == 0:
        return None
    diamond = ""
    for i in range(1, n+1, 2):
        diamond += " " * ((n - i) // 2) + "*" * i + "\n"
    for i in range(n-2, 0, -2):
        diamond += " " * ((n - i) // 2) + "*" * i + "\n"
    return diamond
    
    
print(diamond(3)) #  "*\n***\n*\n"