def increment_string(strng):
    if strng == '':
        return '1'
    if strng[-1].isnumeric():
        number = ''
        for i in range(len(strng)-1, -1, -1):
            if not strng[i].isnumeric():
                break
            number = strng[i] + number
        return strng[:len(strng)-len(number)] + str(int(number)+1).zfill(len(number))
    return strng + '1'