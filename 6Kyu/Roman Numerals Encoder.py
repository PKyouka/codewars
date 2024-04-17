def solution(n):
    roman = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
        10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
        100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
        1000: 'M'
    }
    
    for i in sorted(roman.keys(), reverse=True):
        if n >= i:
            return roman[i] + solution(n - i)
    return ''

print(solution(1))
print(solution(4))
print(solution(6))
print(solution(14))
print(solution(21))