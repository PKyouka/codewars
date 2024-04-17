import re
from collections import Counter

def top_3_words(text):
    words = re.findall(r"[a-z']+", text.lower())
    return [word for word, _ in Counter(words).most_common(3) if word != "'" and word != "''" and word != "'''"]


print(top_3_words(" ' ' ' '")) # []