def reverse_words(text):
    for word in text.split():
        text = text.replace(word, word[::-1])
    return text
    
    
print(reverse_words("YAHAHA WAHYU"))