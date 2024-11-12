def sumMod(a,b,n):
    k =(a+b)%n
    print(k)
sumMod(10,23,5)


# Funktion zur Berechnung der Quersumme
def quersumme(n):
    return sum(int(digit) for digit in str(n))

# Funktion zur Berechnung der iterierten Quersumme
def iterierte_quersumme(n):
    while n >= 10:  # solange die Zahl mehrstellig ist
        n = quersumme(n)
    return n

# Beispiele
zahl = 98765
print(f"Quersumme von {zahl} ist {quersumme(zahl)}")
print(f"Iterierte Quersumme von {zahl} ist {iterierte_quersumme(zahl)}")
