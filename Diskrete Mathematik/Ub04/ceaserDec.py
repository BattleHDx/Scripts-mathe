def ceaserDec (msg,key):

    result=""
    for c in msg:
        encChar = chr((ord(c) - ord('A') - key) % 26 + ord('A'))
        result +=encChar
    return result
print(ceaserDec('LEPPS',4))