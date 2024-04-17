def rot13(message):
        result = ""
        for char in message:
            if char.isalpha():
                if char.islower():
                    if ord(char) + 13 > 122:
                        result += chr(96 + (ord(char) + 13 - 122))
                    else:
                        result += chr(ord(char) + 13)
                else:
                    if ord(char) + 13 > 90:
                        result += chr(64 + (ord(char) + 13 - 90))
                    else:
                        result += chr(ord(char) + 13)
            else:
                result += char
        return result

print(rot13("test"))