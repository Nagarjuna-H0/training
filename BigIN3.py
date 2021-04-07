#---created by Nagarjuna----#


def larger_3(i,j,k): #finding largest of 3 numbers
    if(i>j):
        if(i>k):
            print(str(i)+" is bigger num")
        else:
            print(str(k)+" is bigger num")
    else:
        if(j>k):
            print(str(j)+" is bigger num")
        else:
            print(str(k)+"is bigger num")
larger_3(1,2,3)
