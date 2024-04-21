import re

def calculate(expression):
    if expression == "" or re.match("[+\-*/\s]$", expression[-1]):
        return False
    elif re.match("^[0-9+\-*/\s]*$", expression):
        return eval(expression)
    else:
        return "Invalid input"

print(calculate("2 + 3")) # 5
print(calculate("2 - 3 - 00004")) # -5
print(calculate("10 * 5 / 2")) # 25
print(calculate("1 + 1")) # 2
print(calculate("18 + 4*6")) # 42
print(calculate("245 - 826")) # -581
print(calculate("09 + 000482")) # 491
print(calculate("8 / 4 + 6")) # 8
print(calculate("5 + 1 / 5")) # 5.2
print(calculate("1+2+3")) # 6
print(calculate("9 /3 + 12/ 6")) # 5

#INI RUSAK CUY, GATAU KENAPA