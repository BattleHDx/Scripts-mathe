def create_word(n):
    letter = "a"

    word =""
    while len(word) < n:
        if len(word) % 2 == 1:
            word = word + "b"
        else:
            word  = word + letter
    return word

def replace_letter(word):
    i=0
    new_word =""
    while i < len(word):
        if word[i] == "a":
            new_word += "#"
        else:
            new_word += word[i]
        
        i += 1
    return new_word

def replace_letter_at(word,pos):
    i=0
    new_word =""
    while i < len(word):
        if i ==pos:
            new_word = new_word + "#"
        else:
            new_word = new_word + word[i]
        i+= 1
    return new_word
def main():
    x = create_word(32)
    print(x)
    x = replace_letter(x)
    print(x)
    x = replace_letter_at(x,3)
    print(x)
main()