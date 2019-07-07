# findall()  >>> allows search of every occurence of a given pattern. 
# if no groups present >> then it will present a list of strings not a match object
# if groups are present >> then it returns a list of tuples of strings containing each group 
import re 

phoneNum = re.compile(r'((\d\d)-(\d\d)-(\d\d\d\d\d\d))')
print(phoneNum.findall('I can be reached at 04-49-200435, 04-57-399421'))

# the code above returns this list [('04-49-200435', '04', '49', '200435'), ('04-57-399421', '04', '57', '399421')] <<< each tuple contains a individual groups



# character classes  

# \d  - any 0-9 numbers
# \D  - not numbers
# \w  - any word characters i.e letter,number or underscore
# \W  - capital means not \w
# \s  - blankspace
# \S  - not a space tab or newline

# creating custom character classes .... 

# r'[aeiou]'  <<< essentially creates a class of vowel characters << 
# r'[a-z]'  <<< range of letters can be created using '-' so this creates a range of all lowercase letters
# r'[a-zA-Z] <<< range of all upper and lowercase letters. cases must be explicitly described.

letters = re.compile(r'[a-zA-Z]')
print(letters.findall('I can be reached at 04-49-200435, 04-57-399421'))

# results in ['I', 'c', 'a', 'n', 'b', 'e', 'r', 'e', 'a', 'c', 'h', 'e', 'd', 'a', 't']  << list of all letters in the string excluding all the whitespaces and numebrs

# r'[aeiouAEIOU]{2}' <<< finds the occurences where 2 upper/lowercase vowels appear consecutively 
# r'[^aeiouAEIOU]'  <<< '^' finds the inverse of the character class << i.e this is the 'not' operator
