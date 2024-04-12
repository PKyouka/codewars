def dir_reduc(arr):
    aturan = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}
    stack = []
    for tujuan in arr:
        if stack and stack[-1] == aturan[tujuan]:
            stack.pop()
        else:
            stack.append(tujuan)
    return stack