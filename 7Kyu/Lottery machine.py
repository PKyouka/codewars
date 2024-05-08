def lottery(s):
    s = ''.join(filter(str.isdigit, s))
    s = ''.join(sorted(set(s), key=lambda x: s.index(x)))
    return s if s else 'One more run!'

