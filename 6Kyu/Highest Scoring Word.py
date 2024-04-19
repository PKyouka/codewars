def high(x):
    words = x.split()
    max_word = ""
    max_score = -1
    for word in words:
        score = sum(ord(c) - 96 for c in word)
        if score > max_score:
            max_score = score
            max_word = word
    return max_word


print(high('never gonna let you down'))  # never