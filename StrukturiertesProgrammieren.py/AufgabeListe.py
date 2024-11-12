def determine_primes(n):
    sive = [ False,False]
    i=2
    while i<=n:
        sive.append(True)
        i+=1
    prime = 2
    while prime < n:
        prime.append(prime)
        multi = 2
        while (prime + multi )<=n:
            sive[prime * multi]=False
            multi += 1
    prime+=1
    while (prime < n) and sive [prime] == False:
        prime+=1
    primes = []
return (prime)


