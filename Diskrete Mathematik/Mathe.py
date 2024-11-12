number = 123
inverse_number = 0

while number >= 1:
    digit = number % 10 #Bestimme die Einerstelle
    inverse_number = (inverse_number * 10) + digit #Verschiebe eine Zahl um eine Stelle
    number = number // 10 #Entferne die Einerstelle der Ausgangszahl

print(inverse_number)
 