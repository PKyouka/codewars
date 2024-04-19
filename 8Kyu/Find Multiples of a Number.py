def find_multiples(integer, limit):
    return list(range(integer, limit+1, integer))


print(find_multiples(5, 25) == [5, 10, 15, 20, 25])