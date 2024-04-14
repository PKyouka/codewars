def solution(s):
    return ''.join(' '+ a if a.isupper() else a for a in s)