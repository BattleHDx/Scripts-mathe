import random

def hangman():
    # Eine Liste von Wörtern, aus denen das Spiel zufällig eines auswählen wird
    word_list = ["python", "programming", "hangman", "challenge", "openai", "developer", "computer"]
    word = random.choice(word_list)
    
    # Initialisierung von Variablen
    guessed_letters = set()  # Set für bereits geratene Buchstaben, Ein set enthält eine ungeordnete Sammlung von einmaligen und unveränderlichen Elementen
    correct_letters = set(word)  # Set der Buchstaben im Wort
    progress = ["_" for _ in word]  # Fortschritt als Liste von Platzhaltern
    attempts = 10  # Maximale Anzahl von Versuchen

    print("Willkommen zum Hangman-Spiel!")
    print("Das Wort hat", len(word), "Buchstaben.")

    # Spielschleife, die läuft, bis der Spieler gewinnt oder alle Versuche verbraucht sind
    while attempts > 0:
        print("\nAktueller Fortschritt: ", " ".join(progress))
        print("Verbleibende Versuche: ", attempts)
        guess = input("Bitte geben Sie einen Buchstaben ein: ")

        # Überprüfen, ob der Buchstabe bereits geraten wurde
        if guess in guessed_letters:
            print("Sie haben diesen Buchstaben bereits geraten. Versuchen Sie es erneut.")
            continue
        
        # Füge den gerateten Buchstaben zu den geratenen Buchstaben hinzu
        guessed_letters.add(guess)

        # Überprüfen, ob der Buchstabe im Wort enthalten ist
        if guess in correct_letters:
            print("Richtig! Der Buchstabe ist im Wort enthalten.")
            for idx, letter in enumerate(word):
                if letter == guess:
                    progress[idx] = guess
        else:
            print("Falsch! Der Buchstabe ist nicht im Wort enthalten.")
            attempts -= 1

        # Überprüfen, ob das Wort vollständig erraten wurde
        if "_" not in progress:
            print("\nHerzlichen Glückwunsch! Sie haben das Wort erraten: ", word)
            break
    else:
        print("\nSie haben keine Versuche mehr. Das Wort war: ", word)

# Spiel starten
if __name__ == "__main__":
    hangman()
