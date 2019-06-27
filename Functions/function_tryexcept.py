# error handling using try... except block

def divideBy(num):
    try:
        return 42/num
    except ZeroDivisionError:
        print('You were trying to divide by zero')  #handles the error and since print() returns None it outputs none. 


print(divideBy(1))
print(divideBy(20))
print(divideBy(0))