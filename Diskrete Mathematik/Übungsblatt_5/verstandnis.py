from sympy import gcd # == ggt from sympy
 
def kleinsterTerm(frac): # [a, b] = a/b
    zaehler = frac[0]
    nenner = frac[1]
    g = gcd(zaehler, nenner)
    g=g*-1
    return [zaehler // g, nenner // g ]

def add(frac1, frac2):
    z1 = frac1[0]
    n1 = frac1[1]
    z2 = frac2[0]
    n2 = frac2[1]
    return kleinsterTerm([z1*n2 - z2*n1, n1 * n2])
 
print(add([3,5], [4,6]))