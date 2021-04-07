#----Age Year----#

def ageyear(age):
    if(age==100):
        print("this year 2021 u got 100")
    elif(age<100):
        print("At"+str(100-age+2021)+"years you will get 100")
    else:
        print("At"+str(age-100+2021)+"years you crossed")
ageyear(25)