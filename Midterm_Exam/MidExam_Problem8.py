def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def polynomial(x):
        k = len(L) - 1
        value = 0
        for number in L:
            value = value + (x**k) * number
            k -= 1
        return value
    return polynomial

print(general_poly([1, 2, 3, 4])(10))
print(general_poly([2,3,5])(4))

def general_poly2(L):
    """
    L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0
    another version
    """
    def polynomial(x):
        k = 0
        for i in L:
            k = x*k + i
        return k
    return polynomial
