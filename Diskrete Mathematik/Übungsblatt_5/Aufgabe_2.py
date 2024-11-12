def multiFraction (zaehler,nenner,zaehler1,nenner1):
    new_zaehler = zaehler*zaehler1
    new_nenner = nenner*nenner1
    total=new_zaehler/new_nenner
    return total 
print(multiFraction(3,7,5,10))