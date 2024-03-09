# Take Name , PhoneNo , Password as an input
# store them in an empty list


import re
import datetime
from validate_email import validate_email



listOfNames = []
rollCode = []
phoneNo = []
passWord = []
Email = []

# defining a fncn
def mobileNumber():
    mobileNo = input('Enter your Mobile nuber: ')
    compReg = re.compile(r'^[1-9]\d{9}')                     #setting up the must conditins
    if compReg.match(mobileNo):
            phoneNo.append(mobileNo)
            print("  Your Mobile Number Registered Successfully \n")
           # phoneNo.append(mobileNo)                      # store mobileNo in phoneNo list
            #phoneNo.append(mobileNo)                      # store mobileNo in phoneNo list
    else:
            print("please enter valid mobile number")
            mobileNumber()

# defining a fncn
def Password():
    # (?=.*[A-Z])       used to set a must condition
    print("Note: password must consist 8 alphanumeric character ")
    password = input("Enter Your Password: ")
    passCheck = re.compile(r"(?=.*[A-Z])(?=.*[1-9])[a-zA-Z0-9]{8}")
    isPassTrue = passCheck.match(password)
    if isPassTrue:
        print("Thank You for Registering \n ---------------------------------------")
        passWord.append(password)           #storing password in passWord List

    else:
        print("please enter valid Password")
        Password()


# to store participants name as Input
def participants_name():
    p = datetime.datetime.today()  # datetime function
    print("\n\tWelcome To Participant Portal\t\t\t\t[", p, "]", "\n")
    for i in range(10):                    #Setting the Range
        name = input("\tEnter Your Name:  ")
        listOfNames.append(name)  # store all inputs inside a list
        print("\n_______________________________________\n")
        def emailid():

            mail = input("Please Enter a valid email Address:   ")

            is_valid = validate_email(mail)

            if is_valid:
                print("Your Email Address Registered Successfully")
                Email.append(mail)
            else:
                print("It seems you have Entered Incorrect Email Address")
                return emailid()

        print("Hi! ", name, " \n In order to proceed please register with valid Details")
        takemail= emailid()
        mobile = mobileNumber()
        password = Password()
        print("-----------------------------------------\n")


# assign unique roll code
def assignroll():
    y = 0
    emptyString = re.compile(r'^\s*$')
    for i in phoneNo:
        if emptyString.match(str(i)):
            continue
        uniqueCode = f"{i},{y}"
        rollCode.append(uniqueCode)
        # phoneNo.append(rollCode)
        #print("list : ", uniqueCode)
        y = y + 1

    return rollCode
