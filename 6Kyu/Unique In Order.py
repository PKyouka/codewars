def unique_in_order(sequence):
    if len(sequence) == 0:
        return []
    else:
        unique = []
        unique.append(sequence[0])
        for i in range(1, len(sequence)):
            if sequence[i] != sequence[i-1]:
                unique.append(sequence[i])
        return unique