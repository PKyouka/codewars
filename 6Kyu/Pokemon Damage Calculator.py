def calculate_damage(your_type, opponent_type, attack_power, opponent_defense):
    
    type_effectiveness = {
      ("fire", "grass"): 2,
      ("water", "fire"): 2,
      ("grass", "water"): 2,
      ("electric", "water"): 2,
      }
    
    neutral_effectiveness = {
        ("fire", "electric"): 1,
        ("grass", "electric"): 1,
        ("electric", "fire"): 1,
        ("electric", "grass"): 1,
    }

    if (your_type, opponent_type) in neutral_effectiveness:
        effectiveness = neutral_effectiveness[(your_type, opponent_type)]
    elif (your_type, opponent_type) in type_effectiveness:
        effectiveness = type_effectiveness[(your_type, opponent_type)]
    else:
        effectiveness = 0.5

    damage = 50 * (attack_power / opponent_defense) * effectiveness

    return int(max(damage, 0))

print(calculate_damage("fire", "electric", 10, 2))