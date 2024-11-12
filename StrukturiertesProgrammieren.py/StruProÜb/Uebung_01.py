def BmG(x):
    a=x/3.14159*180
    return a
print(BmG(5))


def is_palindrom(digits):
    i = 0
    j = len(digits) -1

    while i != j:
        if digits[1] != digits [j]:
            return False
        
        i = i + 1
        j = j - 1
    
    return True