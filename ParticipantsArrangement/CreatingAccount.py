
import main
import re



# defining a fncn
def mobileNumber():

 mobileNo = input('enter your mobile nuber: ')

 compReg = re.compile(r'^[1-9]\d{9}')

 if compReg.match(mobileNo):
     print("valid")


 else:
        print("invalid")

def Password():

    #calling the fncn phoneNumber inside password
    mobileNumber()

    # (?=.*[A-Z])       used to set a must condition
    password = input("Enter Your Password")
    passCheck = re.compile(r"(?=.*[A-Z])(?=.*[1-9])[a-zA-Z0-9*]{8}")

    if passCheck.match(password):
     print("Password Entered")
    else:
     print("invalid password")

#calling function(password)
Password()