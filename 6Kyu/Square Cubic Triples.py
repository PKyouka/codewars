def find_abc_sumsqcube(c_max, num_sol):
    result = []
    for a in range(1, c_max):
        for b in range(a, c_max):
            for c in range(b, c_max):
                if a**2 + b**2 == c**3:
                    result.append(c)
    return sorted(result)[:num_sol]

    
print(find_abc_sumsqcube(5, 1)) #[2]
print(find_abc_sumsqcube(5, 2)) #[5]
print(find_abc_sumsqcube(10, 2)) #[5, 10]
print(find_abc_sumsqcube(20, 8)) #[]


#belum jadi