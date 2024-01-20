"""
Problem statement:
1. to store participants name as Input
2. store all inputs inside a list
3. assign a unique roll code to each participant on first come, first serve basis
4. display participants information
5. assign role codes only to valid participant name
"""

import re
import datetime

listOfNames = []
rollCode = []
phoneNo = []










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
