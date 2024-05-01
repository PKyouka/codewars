def lovefunc( flower1, flower2 ):
    for _ in range(2):
        if flower1 % 2 == 0 and flower2 % 2 != 0:
            return True
        elif flower1 % 2 != 0 and flower2 % 2 == 0:
            return True
        else:
            return False
    return False

print(lovefunc(1,4))