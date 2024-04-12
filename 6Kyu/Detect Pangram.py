import string
def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    if set(s.lower()) >= alphabet:
        return True
    else:
        return False