def spinning_rings(inner_max, outer_max):
    inner = outer = moves = 0
    while True:
        inner = (inner - 1 + inner_max + 1) % (inner_max + 1)
        outer = (outer + 1) % (outer_max + 1)
        moves += 1
        if inner == outer:
            return moves


print(spinning_rings(2, 3)) # 5
print(spinning_rings(3, 2)) # 2
print(spinning_rings(1, 1)) # 1
print(spinning_rings(2, 2)) # 3
print(spinning_rings(3, 3)) # 2