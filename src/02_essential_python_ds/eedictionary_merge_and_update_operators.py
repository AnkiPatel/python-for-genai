# merge (|) and update (|=) operators

# merge () allow to combine two dictionary into one

dict1 = {'a':1,
         'b':2}
dict2 = {'b':3,
         'c':4}
uniounDict = dict1 | dict2; # here key 'b' is common. dict2's value for 'b' will override dict1's value
print(f'{uniounDict=}') #op:uniounDict={'a': 1, 'b': 3, 'c': 4}


dict3 = {'a':1,
         'b':2}
dict4 = {'c':3,
         'd':4}
# update () allow to update one dictionary with another
print(f'{dict3=}') #dict3={'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict3 |= dict4;  #here dict3 is getting updated with value of dict4
print(f'{dict3=}')