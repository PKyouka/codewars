def to_camel_case(text):
    for i in text:
        if i == '-' or i == '_':
            text = text.replace(i, ' ')
    text = text.split()
    for i in range(1, len(text)):
        text[i] = text[i].capitalize()
    return ''.join(text)

print(to_camel_case("the-stealth-warrior"))