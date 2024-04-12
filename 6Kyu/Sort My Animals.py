def sort_animals(lst : list) -> list:
    return sorted(lst, key=lambda x: (x.number_of_legs, x.name))