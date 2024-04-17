def count(s):
    return {i: s.count(i) for i in s}
    
    
    
print(count('aba') == {'a': 2, 'b': 1})
print(count('') == {})
print(count('ab') == {'a': 1, 'b': 1})
