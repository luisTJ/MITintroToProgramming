"""Computes the polynomial function for a given value x. Returns that value.
poly: tuple of numbers, length > 0
x: number
returns: float
"""
def evaluate_poly(poly, x):
    sum = 0
    for i in range(len(poly)):
        sum += poly[i]*(x**i)
    return sum
       
poly = (0.0, 0.0, 5.0, 9.3, 7.0)
x = -13
print evaluate_poly(poly, x)
