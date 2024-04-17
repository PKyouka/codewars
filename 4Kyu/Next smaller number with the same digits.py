def next_smaller(n):
    n = str(n)
    for i in range(len(n)-1, 0, -1):
        if n[i] < n[i-1]:
            break
    else:
        return -1
    for j in range(len(n)-1, i-1, -1):
        if n[j] < n[i-1]:
            break
    n = n[:i-1] + n[j] + ''.join(sorted(n[i-1:j] + n[j+1:], reverse=True))
    return int(n) if n[0] != '0' else -1

print(next_smaller(100)) # -1
print(next_smaller(907)) # 790