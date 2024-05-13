def take(arr,n):
    if n == 0:
        return []
    elif n < 0:
        return []
    else:
        for i in range(n):
            if i < len(arr):
                return arr[:n]
            else:
                break