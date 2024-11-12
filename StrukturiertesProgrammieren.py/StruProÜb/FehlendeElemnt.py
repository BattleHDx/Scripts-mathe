def find_missing_Element (input_list):
    Is_Found = True
    counter = 0
    while Is_Found==True:
        for i in input_list:
            if counter == i:
                Is_Found = True
                counter +=1
            else:
                Is_Found = False
    return counter
print (find_missing_Element([0,2,4,1]))