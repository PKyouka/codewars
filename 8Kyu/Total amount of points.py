def points(games):
    for i in range(len(games)):
        games[i] = games[i].split(":")
    total = 0
    for i in games:
        if i[0] > i[1]:
            total += 3
        elif i[0] == i[1]:
            total += 1
    return total