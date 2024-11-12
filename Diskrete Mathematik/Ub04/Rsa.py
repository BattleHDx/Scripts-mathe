from sympy import prime, factorint, mod_inverse

def main():
    p = prime(50) # gibt 50 primzahl
    q = prime(54)
    n = p*q # muss größer als die z.b 8262 sein
    phi = (p - 1) * (q - 1) # wird berechnet um den privaten shclüssel zu berechenen
    print(p, q, n, phi, factorint(phi)) #

    e = 7*11*13 # (e,n)weil primzahlen, die nicht in primfaktorzerlegung in phi(n) vorkommen. e ist teilerfrei . Ist der öffentliche schlüssel.
    d = mod_inverse(e,phi) # (d,n)privater schlüssel
    print(e, d)

    def crypt(M, e, n):
        return M**e % n   #Formel im mathe


    encrypted = crypt(8262, e, n)
    print(f"Verschlüsselt: {encrypted}")
    #print("Verschlüsselt:", encrypted)

    def decrypt(C, d, n):
        return C**d % n

    decrypted = decrypt(encrypted, d, n)
    print(f"Entschlüsselt: {decrypted}")

main()