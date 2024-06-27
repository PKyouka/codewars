def get_size(w,h,d):
    return [2*(w*h + h*d + w*d), w*h*d]

print(get_size(4, 2, 6) == [88, 48])