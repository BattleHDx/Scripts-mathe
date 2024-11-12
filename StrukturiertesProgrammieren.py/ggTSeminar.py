def ggT(a,b):

    # Die kleinere der beiden Zahlen wählen
    ggT = a if a < b else b

    # Rückwärts zählen, um den ggT zu finden
    while ggT > 0:
        if a % ggT == 0 and b % ggT == 0:
            break  # ggT gefunden, Schleife beenden
        ggT -= 1
    return ggT

    # Ergebnis anzeigen
print (ggT(60,70))