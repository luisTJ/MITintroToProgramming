"""
Computes and returns the derivative of a polynomial function. If the

derivative is 0, returns (0.0,).

Example:

>>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0) # x4 + 3.0x3 + 17.5x2 - 13.39 

>>> print compute_deriv(poly) # 4.0x3 + 9.0x2 + 35.0x 

(0.0, 35.0, 9.0, 4.0)

poly: tuple of numbers, length > 0

returns: tuple of numbers

"""
def compute_deriv(poly):
    result = []
    for i in range(1,len(poly)):
        result.append(poly[i]*i)
    return tuple(result)


poly = (-13.39, 0.0, 17.5, 3.0, 1.0) # x4 + 3.0x3 + 17.5x2 - 13.39 
print compute_deriv(poly) # 4.0x3 + 9.0x2 + 35.0x 