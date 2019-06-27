# modules are python programs that contain a related group of functions that can be called when imported into current script
# import module1, module2.....
# module1.function1()   <<< to use the function1() from module1
# to use the function names directly we can use 
# from module_name import function (or * to import all functions)
# the example below uses the module pyperclip

import pyperclip

#pyperclip.copy('Hello World')  --- copies the arguments into clipboard

print(pyperclip.paste())    # --- prints out the clipboard contents. only plain-text

# function(param1, param2,....paramN) contain block of codes that is run everytime the funciton is called. declared with the 'def' statement


def hello(name):
    print('Hello '+ name + '!')

hello('Zafar')
hello('Zamil')

# the return statement returns a value evaluated by the function. can be of many types. eg 'None' 
# every function returns a value but it can be a None type value as well. if a function does not include a return statement it just returns None. 

print('Hello','World')  #print retunrs a None type characters

