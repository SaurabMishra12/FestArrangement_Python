import pandas as pd
import SigninWindow as participant



#calling of function
name = participant.participants_name()
roll = participant.assignroll()

key = [['Details of Participants']]
#god = [(participant.listOfNames,participant.phoneNo)]
#print(rollCode)
a = pd.DataFrame(participant.listOfNames,participant.phoneNo,columns=key)
print('\n',a )



