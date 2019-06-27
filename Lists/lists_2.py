# method is like a function which is called on a certain value 

spam = ['hello','hi','heya','howdy']

print(spam.index('hi'))   # << finds the index of the element in the given list. if it doesnt exist raises value error. if multiple occurences exits it returns the index of the first instance

# list.append(value)  <<< adds to the end of the list

# list.insert(index, value)  <<< inserts a value to a specific index

# both of the above values are modified in place

# list.remove(value)  <<<  removes the value from the list. errors and multiples handled the same way as index() methods
# list.sort()  << sort in ascending order (ASCII values usede for strings)<<< add reverse = True to do descending. needs to be a list containing same type of data
# can use key = key_function <<< to have a specific type of sort 



