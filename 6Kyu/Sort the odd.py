def sort_array(source_array):
    odd = sorted((x for x in source_array if x % 2 != 0), reverse=True)
    return [x if x % 2 == 0 else odd.pop() for x in source_array]