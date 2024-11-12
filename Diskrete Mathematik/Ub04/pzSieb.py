def pzSieb(n):
    primes = []
    numbers = list(range(2,n))
    c = 2
    while c*c < n:
        for k in range(c,n,c):
            if k in numbers:
                numbers.remove(k)
        primes.append(c)
        c = numbers[0]
    return primes + numbers
pzSieb(100)

def pzSieb(n):
    primes = []
    numbers = list(range(2,n))
    c = 2
    counter = 0
    while c*c < n:
        if counter>=3:
            return primes + numbers
        for k in range(c,n,c):
            if k in numbers:
                numbers.remove(k)
        primes.append(c)
        c = numbers[0]
        counter+=1
    return primes + numbers
print(pzSieb(97))