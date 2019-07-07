# open() << opens a specific file on read-mode by default 

import os, shelve

fileID = open('test.txt')
print(fileID.read())
fileID.close()

fileID = open('test2.txt','w')
st = 'This string has been written by python'
fileID.write(st)
fileID.close()

# to open a file in append mode use 'a' modifier in the open() function 
# always close a file after its been used otherwise memory will be in use.

# to store python variables in a bin file use the shelve module
# it stores data which is similar to a dict file using key:value pairing

myCats = ['Dogoo','Leo','Gutoolz','ToonToon']
shelfFile = shelve.open('catStorage')  # >>> creating a storage file 
shelfFile['cats'] = myCats  # >>> storing the list using the 'cats' key
shelfFile.close()  # >>> closing it to free up memory 

shelfFile = shelve.open('catStorage')
print(shelfFile['cats'])
shelfFile.close()

# can use keys(), values() method on the shelve container

