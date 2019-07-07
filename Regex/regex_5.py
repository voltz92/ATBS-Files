# replacing with regex 

# using the .sub('What to replace with','target string')
import re 

text = 'Agent Alice gave Agent Bob the secret documents'
agentReg = re.compile(r'Agent \w+')
print(agentReg.findall(text))
print(agentReg.sub('REDACTED',text))   # this code replaces the Agent Alice and Agent Bob pattern with the word REDACTED

# to use a certain portion of the matching pattern use groups 

nameReg = re.compile(r'Agent (\w)\w+')
print(nameReg.findall(text))  # this returns the first letters of the names Alice and Bob 
print(nameReg.sub(r'Agent \1****',text))  # this replaces the names with the just their first letters and 4 '*'s. Using the \1 we are declaring that we use the \1 element from the findall list

# re.VERBOSE mode allows for seperating complicated patterns into seperate lines and adding comments using '#' 

# re.compile(r'''\d\d\d  #this is a pattern
# \d\d\d\d #we are moving to second line''', re.VERBOSE)

# we can add multiple 2nd arguments to the re.compile() function using the '|' operator

