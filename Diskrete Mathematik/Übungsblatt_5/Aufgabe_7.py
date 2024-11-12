def getrational (a,b,n):
    r= []
    if a != b:
        while n > 0:
            x = ((b-a)/(n+1))
            x+=a
            n-=1
            r.append(x)
        return r
    else:
        return False
print(getrational(7.9,8,100000))

#Weil wir keine genaue annährung haben, da der computer lange rechnet, bis er rundet.