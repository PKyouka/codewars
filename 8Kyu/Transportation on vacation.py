def rental_car_cost(d):
    total_harga = d * 40
    if d >= 7:
        total_harga -= 50
    elif d >= 3:
        total_harga -= 20
    return total_harga

print(rental_car_cost(1))