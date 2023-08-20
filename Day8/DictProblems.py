myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}

sorting_myDict = list(myDict.items())
sorting_myDict.sort()

for key,value in sorting_myDict:
   print(key,value)