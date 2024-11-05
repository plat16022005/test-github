import math
def cos_taylor(x, epsilon=1e-10):
    x = x % (2 * math.pi)
    term = 1
    cos_x = term
    n = 1
    while abs(term) > epsilon:
        term *= -x**2 / (2*n * (2*n - 1))
        cos_x += term
        n += 1
    return cos_x
x = math.pi / 3 
print(f"cos({x}) = {cos_taylor(x)}")
print(f"math.cos({x}) = {math.cos(x)}")
