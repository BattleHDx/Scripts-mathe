from sympy import gcd # == ggt from sympy
 
def kleinsterTerm(frac): # [a, b] = a/b
    zaehler = frac[0]
    nenner = frac[1]
    g = gcd(zaehler, nenner)
    g=g*-1
    return [zaehler // g, nenner // g ]
print(kleinsterTerm([-10, -20]))
print(kleinsterTerm([10, -20]))

def multiFraction (zaehler,nenner,zaehler1,nenner1):
    new_zaehler = zaehler*zaehler1
    new_nenner = nenner*nenner1
    total=new_zaehler/new_nenner
    return total 
print(multiFraction(3,10,5,10))

def add(frac1, frac2):
    z1 = frac1[0]
    n1 = frac1[1]
    z2 = frac2[0]
    n2 = frac2[1]
    return kleinsterTerm([z1*n2 + z2*n1, n1 * n2])
 
print(add([3,5], [4,6]))


def diviFraction (zaehler,nenner,zaehler1,nenner1):
    new_zaehler = zaehler*nenner1
    new_nenner = nenner*zaehler1
    total=new_zaehler/new_nenner
    return total 
print(diviFraction(3,10,5,10))


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