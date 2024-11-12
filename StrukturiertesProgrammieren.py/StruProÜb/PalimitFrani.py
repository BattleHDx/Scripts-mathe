def reverse_number(number):
    reverse = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        reverse *= 10
        reverse += digit
    return reverse

def is_Palindrom(input):
    if input == reverse_number(input):
        return True
    return False
print (is_Palindrom(2332))
