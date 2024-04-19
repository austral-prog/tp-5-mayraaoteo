def max_of_two(x, y):
    if x > y : 
        return x
    else:
        return y
print(max_of_two)

def max_of_three(x, y, z):
    if x > y and x > z :
        return x
    elif y > x and y > z :
        return y
    else:
        return z
print(max_of_three)
