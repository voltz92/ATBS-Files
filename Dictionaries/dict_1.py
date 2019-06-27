# dictionaries are like list = they can store many types of data in them 
# their indices are called 'keys'. each key can store a 'value'. so dicts store key:value pairs
cats = {'name':'leo','color':'black and white','age':5}

print(cats)
# dicts indexing
print(cats['color'])

# dicts can use numbers for keys as well and they dont have to start at 0 
# dicts are unordered.   <<< this shit is kinda like structures in matlab 

# to check for keys presence in a dict we can use 'in' statements
# dicts are mutable

# dict.keys() << returns a iterable of keys in a dict
# dict.values() << returns an iterable of values in a dict
# dict.items() << returns an iterable of tuples conatining the key:value pairs in the dict
# e.g

for i, j in cats.items():
    print(i,j)
# dicts.get('key','do what if key not present in dict') << this allows us to run a code using a key before checking whether the target dict has the key or not
# dicts.setdefault('key','value if the key is not present') << used to assign values to a key without checking for presence first


