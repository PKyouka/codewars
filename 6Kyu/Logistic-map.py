def logistic_map(width, height, x_supplies, y_supplies):
    if not x_supplies or not y_supplies:
        return [[None] * width for _ in range(height)]

    distance_map = [[None] * width for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            min_distance = float('inf')
            
            
        for supply_x, supply_y in zip(x_supplies, y_supplies):
            distance = abs(x - supply_x) + abs(y - supply_y)
            min_distance = min(min_distance, distance)  


    distance_map[y][x] = min_distance
    return distance_map