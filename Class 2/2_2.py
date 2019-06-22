# the seterotypical hello world program


print ('Hello World')  # function print() << runs a specific block of code when called. The values inside the '()' are called the arguments of the function.

print ('what is your name? ')
myName = input()   # takes user input. data type is string
print('Nice to meets you '+myName) #concatenating the user input to this message using addition operation on a string
print('Your name consists of '+str(len(myName))+' characters') # len() = determines the length of the string. Output is an integer. the str() function converts other data types to string, as only strings can be concatenated to other strings.
print ('What is your age? ') 
myAge = input()  # once again in string format, even though the user is typing in a number
print ('You will be '+ str(int(myAge)+1)+ ' years old next year')
