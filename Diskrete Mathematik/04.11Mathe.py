#from sympy import gcd #ggt from sympy

#def kleinsterTerm(frac): # [a,b] = a/b
 #   zaehler = frac[0]
  #  nenner = frac[1]
   # g =gcd(zaehler, nenner)
    #return [zaehler // g, nenner // g]
#kleinsterTerm([20,30])

from sympy import gcd # == ggt from sympy
 
def kleinsterTerm(frac): # [a, b] = a/b
    zaehler = frac[0]
    nenner = frac[1]
    g = gcd(zaehler, nenner)
    return [zaehler // g, nenner // g ]
print (kleinsterTerm([-10, -20]))
print (kleinsterTerm([10, -5]))
