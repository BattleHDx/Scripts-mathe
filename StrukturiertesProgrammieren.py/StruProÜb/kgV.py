def is_Prime(number):
    list = []
    primenumber = 2
    while number > 1:
        while number % primenumber == 0:
            list.append (primenumber)
            number = number // primenumber
        primenumber += 1
    return list


def kgV (x,y):
    firstlist=[]        
    secondlist=[]
    firstlist = is_Prime (x)
    secondlist = is_Prime(y)
    results = 1
    for i in firstlist:
        if i in secondlist:
            secondlist.remove(i)
        results *= i
    for i in secondlist:
        results *= i
    return results

print(kgV(20,25))

        