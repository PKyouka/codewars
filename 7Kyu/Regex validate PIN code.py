def validate_pin(pin):
    for i in pin:
        if i not in '0123456789':
            return False
    return len(pin) in [4, 6]

print(validate_pin("1234"))