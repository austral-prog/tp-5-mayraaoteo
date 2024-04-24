import math

def roots(a, b, c):
    my_var_disc = b ** 2 - 4 * a * c
    if my_var_disc == 0:
        x1 = float(-b / 2 * a)
        return f"({x1})"
    elif my_var_disc > 0:
        x1 = ((-b + math.sqrt(my_var_disc)) / (2 * a))
        x2 = ((-b - math.sqrt(my_var_disc)) / (2 * a))
        return f"({x1}, {x2})"
    else:
        return "( )"
print(roots)

def value_y(a, b, c, x):
    y = a * x ** 2 + b * x + c
    return y
print(value_y)

def to_string(a, b, c):
    if a == 0 and b == 0:
        return f"f(x) = {c}"
    elif b == 0:
        return f"f(x) = {a} * X^2 + {c}"
    elif a == 0:
        return f"f(x) = {b} * X + {c}"
    else:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
print(to_string)

def derivation(a, b, c):
    if a == 0 and b != 0:
        no_a = f"f\'(x) = {b}"
        return no_a
    elif b == 0 and a != 0:
        no_b = f"f\'(x) = {a * 2} * X"
        return no_b
    elif a == 0 and b == 0:
        nulo = f"f\'(x) = 0"
        return nulo
    else:
        deriv = f"f\'(x) = {a * 2} * X + {b}"
        return deriv
print(derivation)
