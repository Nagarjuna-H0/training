#----Larger Number in 3 numbers---#


i=int(input("enter i val"))
j=int(input("enter j val"))
k=int(input("enter k val"))
if(i>j):
    if(i>k):
        print("i is bigger num")
    else:
        print("k is bigger num")
else:
    if(j>k):
        print("j is bigger num")
    else:
        print("k is bigger num")