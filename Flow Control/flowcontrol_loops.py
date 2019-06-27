# while loops
i = 1
while i < 5:
    print('This is being repeated')
    i = i+1

# can be used to run something indefinitely until a condition is met
name = ''

while name != 'Zafar':
    print('Please type you name')
    name = input()
print('Thank You')

# ^ an example of input validation << Getting the user to input a valid value

# be careful of infinite loops 

# 'break' = immediately out of loop. no longer executes any other lines after this statement
# 'continue' = jumps back to start of the loop. nothing after this statement is executed.

 # for loops iterate a specific number of times. 

for i in range(5): 
    print('the number is ' + str(i))

print(i)
# the loop above runs 5 times
# the range(start, stop, step) function creates a list of numbers that start at 0 and runs upto the argument passed into function. so range(5) = [0,1,2,3,4]
# the value of i can be accessed outside the loop. its now = 4 
# for loop increments the operator by 1 by default. 



