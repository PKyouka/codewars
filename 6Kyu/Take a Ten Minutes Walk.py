def is_valid_walk(walk):
    east = walk.count('e')
    west = walk.count('w')
    north = walk.count('n')
    south = walk.count('s')
    
    return len(walk) == 10 and east == west and north == south