# to include some special characters in strings we need to use the escape character '\' 

e = 'This is a string that\'s like new \t the best of both \n'
print(e)

# raw strings

spam = r'this is an example of a raw string here \n we dont need to escape "special characters"'
print(spam)

# or we can use """ quotes if theres a lot of special characters to escape.

g = '''This is a multiline string containing a lot of shit 
\\\\\\\\\ alksdjlaksd  a \n \t '''

print(g)

print(g[5])
print(g[5:10])
print('what' in g)
print('this' not in g) 