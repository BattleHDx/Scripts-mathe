def addInv(a, n):
    """
    Berechnet das additive Inverse von a im Restklassenring Z/nZ.
    
    Parameter:
    a (int): Das Element, dessen additiv Inverse berechnet werden soll.
    n (int): Der Modulwert des Restklassenrings.
    
    Returns:
    int: Das additiv Inverse von a in Z/nZ.
    """
    # Das additive Inverse von a ist (n - a) modulo n
    return (-a) % n

# Beispielaufruf
print(addInv(4, 6))  # Erwartet: 2, da 4 + 2 ≡ 0 (mod 6)