import openpyxl
import pandas as pd
import AssignParticipantsIdentificationNumber              #importing the class

rollCode = []

#assigning roll code to participant names
def assign_role_using_while():
    #calling participantsName function from class AssignParticipantsIdentificationNumber
    AssignParticipantsIdentificationNumber.participants_name()      #returns list of participant names
    x = 0
    while x < 3:
        #variable contains participant name list, roll code
        #concatenated string with int. using f-string
        uniqueCode = f"{AssignParticipantsIdentificationNumber.listOfNames[x]},{x}"
        rollCode.append(uniqueCode)
       # print(uniqueCode)
        x = x + 1




def mobileNumber():
    mobileNo = input('Enter your Mobile nuber: ')
    compReg = re.compile(r'^[1-9]\d{9}')
    for i in listOfNames:
        if compReg.match(mobileNo):
            nameWithMobileNo = f'{i}, {mobileNo}'
            phoneNo.append(nameWithMobileNo)
            print("Your Mobile Number Registered Successfully \n",nameWithMobileNo)
        else:
            print("please enter valid mobile number")