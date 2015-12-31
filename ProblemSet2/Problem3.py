"""
Uses Newton's method to find and return a root of a polynomial function.

Returns a tuple containing the root and the number of iterations required to

get to the root.

Example:

>>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0) #x4 + 3.0x3 + 17.5x2 - 13.39 

>>> x_0 = 0.1 

>>> epsilon = .0001

>>> print compute_root(poly, x_0, epsilon)

(0.80679075379635201, 8)

poly: tuple of numbers, length > 1.

Represents a polynomial function containing at least one real root.

The derivative of this polynomial function at x_0 is not 0.

x_0: float 

epsilon: float > 0

returns: tuple (float, int)

"""
deep = 0
def wrapper(poly, x_0, epsilon):
    global deep
    return (compute_root(poly,x_0,epsilon),deep)

def compute_root(poly, x_0, epsilon):
    global deep
    deep += 1
    result = evaluate_poly(poly, x_0)
    if( abs(result) < epsilon ):
        return x_0
    else:
        deriv = compute_deriv(poly)
        new_x = x_0 - result / evaluate_poly(deriv, x_0)
        return  compute_root(poly,new_x,epsilon)



def evaluate_poly(poly, x):
    sum = 0
    for i in range(len(poly)):
        sum += poly[i]*(x**i)
    return sum
       

def compute_deriv(poly):
    result = []
    for i in range(1,len(poly)):
        result.append(poly[i]*i)
    return tuple(result)


poly = (-13.39, 0.0, 17.5, 3.0, 1.0) #x4 + 3.0x3 + 17.5x2 - 13.39 
x_0 = 0.1
epsilon = .0001
#print compute_root(poly, x_0, epsilon) #(0.80679075379635201, 8)
print wrapper(poly,x_0,epsilon)
