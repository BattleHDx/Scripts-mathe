#def ggTT(a, b):
 #   while a != b:
  #      if a < b:
   #         b = b-a
    #    else:
     #       a = a- b
    #print(a)
#ggTT(400,225)

def ggT(a,b):
    while a != b:
        if a < b:
            c = b//a
            b = b-a*c
            if b==0:
                return a
        else:
            c = a//b
            a = a-b*c
            if a==0:
                return b
print(ggT(1460,435))
