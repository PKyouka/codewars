import heapq

def hamming(n):
    h = [1]
    s = set(h) 
    for _ in range(n):
        a = heapq.heappop(h)
        for i in [2, 3, 5]:
            m = a * i
            if m not in s:
                s.add(m)
                heapq.heappush(h, m)
    return a