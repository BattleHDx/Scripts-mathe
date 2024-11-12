def babylon(x):
    a = x
    i = 0
    while (a*a - x) > 0.0001:
        a = (a + x / a) /2
        i += 1
    return (a,i)

babylon(10)