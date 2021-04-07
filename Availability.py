
#----Availability Check---#

def Available(emailId): 
    emails=['naga@gmail.com','reddy@gmail.com','babu@gmail.com','ganesh@gmail.com']
    flag=0
    for i in emails:
        if i==emailId:
            flag=1
            break
        else:
            continue
    if(flag==0):
        print("Email id is available")
    else:
        print("Email Id is already Exist")
           
            

		
Available('babu@gmail.com')



