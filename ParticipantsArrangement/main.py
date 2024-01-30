import pandas as pd
import  SigninWindow as  participant

#calling of function
name = participant.participants_name()
roll = participant.assignroll()
#print(rollCode)
a = pd.DataFrame(participant.listOfNames,participant.rollCode)
print('\n', a)



