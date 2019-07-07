# python raise and assert statements

# raise allows custom Exception messaging 

# eg. raise Exception('This is an error message') 
#raise Exception('Custom Error')    # this line literally causes an error in this case
# exceptions are best raised asap to avoid running through buggy code

import traceback


def printBox(symbol,width,height):
    '''Prints a box of specific dimesions
       using the user provided symbol
       symbol must be a single character
       width and height must be greater than 2
       '''
    
    print(symbol*width)  #print top of the box
    for i in range(height-2):
        print(symbol+' '*(width-2)+symbol)  #print the middle of the box 
    print(symbol*width)  #bottom
try:
    sym = input('Please enter a symbol >> ')
    if len(sym) > 1:
            raise Exception('Please enter a sybmol which only 1 character')  # input check for symbol length 
    width = int(input('Enter the width of the box >> '))
    height = int(input('Enter the height of the box >> '))
    if width <= 2 or height <= 2:  #checking for width/height validity
            raise Exception('Please enter a valid width/height. Must be greater than 2')
except:
    with open('error_log.txt','a') as error_log:
        error_log.write(traceback.format_exc())
        print('Error!!! \nCheck "error_log.txt" for more details'+'\n\n')
    
printBox(sym,width,height)   

