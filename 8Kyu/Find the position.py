def position(alphabet):
    for i in range(26):
        if alphabet == chr(97+i):
            return f"Position of alphabet: {i+1}"
    return None
