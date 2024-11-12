def naiv (a,b):
    if a<b:
        k=a
    else:
        k=b

    while k>0:
        if a%k==0 and b%k==0:  #Der Divident(k) wird immmer um eins reduziert. bis Modulo = 0 heruaskommt beispiel 7 wird bis 4 reduziert bei a=16
           return k
        else:
            k = k-1
        
print(naiv(42,66))

#def naivggT(a,b):
 #   if a>b:
  #      a,b=b,a
   # if a == 0:
    #    return b
    #value = a
    #while value > 0:
     #   if b%value == 0:
      #      if a%value==0:
       #     	return value
#value = value -1