def ungeradewerte(x):
    value = 0
    i=0
    while i < len(x):
        if x[i]%2 != 0:
            value +=1
            i+=1
        else:
            i+=1
    return value
print(ungeradewerte([2,3,4,5,6,7,8]))