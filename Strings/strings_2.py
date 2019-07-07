# string methods 

# string.upper()/lower()  > to convert to upper or lower case
# string.isupper()/islower() > returns a boolean after checking whether the string is upper case or lower case. if blank > both False
# string.title() >> convert to title case

# the .upper() and .lower() return a new string so we can call more methods on them as well 

# string.startswith()/endswith() >> pretty clear 

print(' -- '.join(['a','b','v']))   # join a string using a special delimiter

# string.split()  << split a string on whitespace chars. 
# split('character') << split on a specific character.

# string.rjust(total_length) <<< right justify by adding whitespace padding.  .ljust() and .center() behave the same way 

# string.strip() << remove whitespaces. a string can be passed into this method remove the occurences of that string
# string.rstrip()/lstrip() < remove whitespace on right or left
# string.replace('a','b') << replace the occurences of the character 'a' to 'b' in that string


# string formatting

a = 'asbad a'
b = 'askdlasd'

print('Hi this is %s how to format strings and enter a large %s number of variables in a given string' % (a,b))