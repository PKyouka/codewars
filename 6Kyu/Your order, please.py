def order(sentence):
    return ' '.join(sorted(sentence.split(), key=lambda x: int(''.join(filter(str.isdigit, x)))))


print(order("is2 Thi1s T4est 3a"))