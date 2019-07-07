# '^' before a pattern means that the pattern must be present at the start of the string 
# '$' after a pattern means that the pattern must be present at the end of the string
# '^pattern$' <<< will look for the exact match of the pattern within a string. so '^ring$' will only return true for 'ring' not in 'string'

# '.' - any character other than the newline character 
# '.at' implies any character combination that ends in 'at' e.g cat, hat, rat, mat
# '.*' --- any character any number of times other than newlines

import re

# getting first name last name using regex 

ringReg = re.compile(r'(^ring$)')
print(ringReg.findall('This string contains the word ring to bring the idea of exclusive matching into the ring'))


# names = 'FName: Zafar LName: Ullah'
# nameReg = re.compile(r'FName: (.*) LName: (.*)')
# print(nameReg.findall(names))

# non greedy version '.*?'

# re.compile(r'.*', re.DOTALL) << now includes the newline char as well 
# re.compile(r'[aeiou]', re.I) <<< now case insensitive

