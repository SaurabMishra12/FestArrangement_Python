import pandas as pd
import  SigninWindow as  participant

#calling of function
name = participant.participants_name()
roll = participant.assignroll()

#print(rollCode)
a = pd.DataFrame({'Name':participant.listOfNames,
                  'phoneNo':participant.phoneNo,
                  'Email':participant.Email})
print('\n', a)
a.to_excel('Participants.xlsx', index=False)




