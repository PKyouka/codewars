def is_uppercase(inp):
    return all(char.isupper() or not char.isalpha() for char in inp)