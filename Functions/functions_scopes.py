#scopes

#global = variables usable by everyone is a global variable. destroyed when the program is closed.
#local = variables only usable inside the local scope. << i.e inside a function. destroyed once the function has returned a value
# local vars are also not usable by other functions. ony defined within a specific function

# can use 'global statement to declare a global variable inside a function that would allow it to be accessible everywhere

# if there is a local variable inside the function using the same name it takes precedence over the global var. 


def hello(myVar):
    global var2
    myVar = 200
    print(myVar)
    myVar = myVar + 2
    print(myVar)
    print(var2)
    var2 = var2+10

myVar = 'hi'
var2 = 1000
print('calling function using myVar as arg')

hello(myVar)

print('now we are done running function')
print(myVar)
print(var2)