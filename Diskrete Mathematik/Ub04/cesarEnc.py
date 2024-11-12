#def caesarEnc(msg, key):

 #   result = ""

  #  for c in msg: 

   #     encChar = chr((ord(c) - ord('A') + key) % 26 + ord('A'))

    #    result += encChar

    #return result

#print(caesarEnc('HALLO', 4))
 
def caesarEnc(msg, key):

    result = ""

    for c in msg: 

        encChar = chr((ord(c) - ord('A') + key) % 54 + ord('A'))

        result += encChar

    return result

print(caesarEnc('HaLlO', 4))