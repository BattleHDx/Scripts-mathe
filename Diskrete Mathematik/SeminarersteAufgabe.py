werte=list(range(321))
print(werte)

def liste (number):
    digit = 0
    Numberlist=[]
    while number>0:
        digit=number % 10
        Numberlist.append(digit)   #das.append ist eine funktion die die liste bereitstellt. Wurde in die Liste gespeichert
        number=number // 10
    return Numberlist
print(liste(321))


def sum_values(values):
    sum = 0
    i = 0
    while i < len(values):
        sum = sum + values[i]
        i = i + 1
    return sum 



digits = liste(321)
print(sum_values(digits))


def multi(numbers,b):
    a=1
    while a<=numbers:
        c=a*b
        print(a,"*",b,"=",c)
        a=a+1
multi(25,2)


#zahl = 51
zahl = 2
teiler = 2

while zahl != 1:
    rest = zahl % teiler
    if rest > 0 :
        teiler = teiler + 1
    else:
        print (teiler)
        zahl = zahl // teiler

