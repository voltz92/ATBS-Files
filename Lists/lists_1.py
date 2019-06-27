myList = [1,2,5,6,8]
print(myList)
print(myList[0])  #indexing a list
print(myList[0:3]) #slicing a list. 2nd value isnt included.
myList[2] = 99
print(myList[2]) # assigning a new value to a index
print(myList[1:]) # prints from the 2nd element to the end
myNewList = [myList,['cat','bat','rat']]  # list within a list
print(myNewList)
print(myNewList[1][1])  #multidimensional list
print(myNewList[1][-1])  #using negative indices to address the last value in a list
#use 'del' statement to delete specific values from a list
# use len() to get the number of elements in a list
# use '+' to concatenate lists like strings
# []*n << creates a newlist with the same elements repeated n times
# list() >> converts the arg to a list format

# can use the 'in' operator to check whether an element is present in a list or not 

print(99 in myList)

# similarly 'not in' << inverse of 'in'
spam = ['meat', 'tomato','potato','aloo']

for word in spam:
    print(word)    # << accessing the list values using a for loop 

# to access indices we can use 

for i in range(len(spam)):
    print(i) 

# multiple assignment using lists 

# we can assign n- vars to n - values using a list. list must have n-elements in it
# n1, n2, n3 = myList   << < myList = [v1,v2,v3]  << results in n1=v1, n2=v2 and so on 

# increment by 1 >> 

a = 10
a += 1
