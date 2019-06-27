# python strings can considered as a list of characters
# indexing/slicing/'in' statements can be performed on them as well 

# list values is mutable  <<< can be changed
# strings are immutable  <<< cannot be changed later

# to modify a string it needs to be created again or saved in a new var with modifications

#  variables store the references to a mutable value but not the value itself. so if two vars have the same references, changing the mutable value
#  using one variable will cause it to change for the other as well. this allows them to modified in place
#  immutable values are stored by assigning  the value to the variable. they cannot be changed in place

# when mutable objects are passed into a function << the function can modify the list even if its not declared as a global var. 

# using the 'copy' module and copy.deepcopy() function we can copy the list itself not the reference.

# string.upper()/lower()  << you guessed it.

