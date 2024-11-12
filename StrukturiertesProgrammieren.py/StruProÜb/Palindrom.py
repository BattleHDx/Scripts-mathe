def is_palindrom(digits):
    i = 0
    j = len(digits) -1

    while i < j:
        if digits[i] != digits [j]:
            return False
        
        i = i + 1
        j = j - 1
    
    return True

digits = [1,2,1]
print(is_palindrom(digits))

digits = [1,2,2]
print(is_palindrom(digits))

digits = [1,2,2,1]
print(is_palindrom(digits))

digits = [1,2,3,1]
print(is_palindrom(digits))