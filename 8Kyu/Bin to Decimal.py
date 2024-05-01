def bin_to_decimal(binary):
    for i in binary:
        if i not in '01':
            return 'Invalid'
    return int(binary, 2)