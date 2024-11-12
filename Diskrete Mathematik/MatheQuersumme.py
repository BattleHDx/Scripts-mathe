def crossSum(number):  #definieren eine funktion
    summe=0  #0 ist dafür da das man mit ganzzahlen rechnen.
    while number>0:
        digit=number % 10
        summe= summe + digit
        number= number // 10
    return summe 
result=crossSum (3128)
print(result)

def iterativCrosssum(othernumber):
    while othernumber>9:
        othernumber=crossSum (othernumber)  #Geht von 13 nach 12 bis othernumber>9 ist. Dann verlässt sie erst die Schleife
    return othernumber  # Dannn geben wir das ergebnis in zeile 15 zurück.

otherresult=iterativCrosssum(result)   #Jetzt haben wir es in einer Variable gespeichert Auto beispiel einkaufen
print(otherresult)


