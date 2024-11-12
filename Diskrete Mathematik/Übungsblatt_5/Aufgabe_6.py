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
print(getrational(2,3,4))