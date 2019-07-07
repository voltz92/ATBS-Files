import re 

# '?' operator in the regex pattern >> results in a match if the group preceding the symbol appears once or never. 
# eg.

qmReg = re.compile(r'Bat(wo)?man')
mo = qmReg.search('The adventures of Batwoman')   
print(mo.group())
# will not work if 'wo' appears more than once before 'man' 
# this can be used to create optional patterns. eg Area codes in phone numbers

# to check if the pattern occurs more than once >>> use the '*' after the target group 
# eg. r'Bat(wo)*man   <<< 0 or more occurences of wo such as Batwowowoman

# to check if at least once or more times <<< '+' character
# r'Bat(wo)+man'  <<< checks if (wo) group is present at least once or more times


# to check a specific number of occurences << use the format r'(ha){3}' <<< this checks if the (ha) group is present at least 3 times or not 

haReg = re.compile(r'(ha){3}')
mo = haReg.search('hahahahahaha')
print(mo.group())

# to check the occurence between a certain range {x,y}  >> 
# eg. consecutive occurence of 3 to 5 digits in a text >>> r'(\d){3,5}'  << checks for a minimum of 3 occurences and upto 5 occurences. this is 
# greedy version by default >> as in this will return 123456789 >>> 12345 not 123 even though that satisfies the conditions as well 
# for non greedy version >> use a '?' >>> r'(\d){3,5}?'  >> this will return 123 for the above search. matches shortest string possible
