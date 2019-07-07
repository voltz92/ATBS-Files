import logging 

logging.basicConfig(filename = 'debug_log.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
# by adding the filename argument, we can output all the debug messages to a file instead of printing to console. 
# this enables storage of debug messages as these are appended and not written over


# format :: 
# asctime << ascii encoded time
# levelname << DEBUG level 
# message << prints out the string we passed into the logging.debug() method

# logging.disable(logging.CRITICAL)  # this will disable all the logging messages from showing up

# this way we dont have to comment out or delete all the print statements if they were used. <<< 

# logging levels: debug > info > warning > error > CRITICAL  (highest) 


logging.debug('Start ----')
def factorial(n):
    logging.debug('Inside the funciton')
    fact = 1
    for i in range(1,n+1):
        fact *= i
        logging.debug('The value of iterator in the loop is %s and the total is %s' % (i,fact))
    logging.debug('Value to be returned : %s' % fact)
    return fact

print(factorial(5))

logging.debug('Execution complete')
