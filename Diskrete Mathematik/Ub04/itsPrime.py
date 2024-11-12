def isPrime(n): # primitive Funktion um festzustellen ob n prim ist
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)):
        if n % i == 0:
            return False
    return True
print(isPrime(10))