def get_count(sentence):
    a = 0
    for i in sentence:
        if i in 'aeiou':
            a += 1
    return a