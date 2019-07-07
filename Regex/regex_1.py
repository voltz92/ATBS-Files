# import re module first

# describe the patter using re.compile(raw_string_of_patterns)  << this creates a regex object

# using .search(target)  on the regex object finds the first instance of the pattern in the target string
# then we can access the found object by using .group() method on the match_object created above
# to find all instances of the pattern in target_string we can also use the .findall() method on the regex object
# this returns a list of the occurences.
#  

import re 

phoneNum = re.compile(r'\d\d-\d\d-\d\d\d-\d\d\d')  # << this creates a regex object for the pattern 11-11-111-111 >> \d implies digits. raw strings are used as a lot of '\' are used in regex
mo = phoneNum.search('This is my nnumber : 04-49-200-435 or 04-49-200-231')
print(mo.group())

# the above code only returns the first instance of a phone number

print(phoneNum.findall('This is my nnumber : 04-49-200-435 or 04-49-200-231'))  # this returns a list of all occurences of the pattern in the target string

# we can greate groups of patterns using '()' then access each group by using indexing the group() method
phoneNum = re.compile(r'(\d\d)-(\d\d-\d\d\d-\d\d\d)')
mo = phoneNum.search('This is my nnumber : 04-49-200-435 or 04-49-200-231')  # returns None if no pattern found.
print(mo.group(0)) #prints the whole pattern 
print(mo.group(1)) #prints the first group, ie the area code
print(mo.group(2)) #prints the rest of the phone number

# if () is to be included in the pattern they must be esacped using the \ character
# to set a pattern containing multiple variations of somethine we can use '|' <<< eg r'Bat(man|mobile|copter)' will search for a combination of Batmobile, Batman, Batcopter

