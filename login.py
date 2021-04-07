#----Login verification---#

def login(username,password): 
    UserId=input("Enter username")
    Password=input("Enter password")
    if UserId==username and Password==password:
        print("Login successful!")
    
    else:
        print("Wrong UserId/Password")

		
login('Naga9948','naga@9999')

