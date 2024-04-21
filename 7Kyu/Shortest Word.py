def find_short(s):
    for _ in s.split():
        return len(min(s.split(), key=len))