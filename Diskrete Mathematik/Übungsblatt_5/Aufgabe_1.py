from sympy import gcd # == ggt from sympy
 
def kleinsterTerm(frac): # [a, b] = a/b
    zaehler = frac[0]
    nenner = frac[1]
    g = gcd(zaehler, nenner)
    g=g*-1
    return [zaehler // g, nenner // g ]
print(kleinsterTerm([-10, -20]))
print(kleinsterTerm([10, -20]))