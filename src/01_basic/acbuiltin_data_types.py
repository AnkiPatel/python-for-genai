
# PYTHON'S BUILT-IN DATA TYPES

# 1. Numbers: int and float
age = 40
temperature = 20.1

# 2. Booleans: Logical values => True or False
check = (age == 40)
print(check)
check = (age < 30)
print(check)

# you can directly print the boolean value
print(age == 40)
print(age < 30)

# 3. None  => absence of a value

# 4. Strings: Ordered sequences of characters, stored in UTF-8 encoding.
model_name = 'Gemini'

# 5. Lists: Ordered, mutable sequences of objects.
person = ['Dan', 40, 82.5, True]    # list type

# 6.Tuples: Ordered, immutable sequences of objects.
# It is like constant list whose size and elements value cannot change
coordinates = (40.7128, -74.0060)   # tuple type (NYC latitude and longitude)

"""
When Do I Use Tuples vs. Lists?
When to use tuples or lists depends on your needs.

There may be some occasions when you don’t want your data to be changed. 
If you have data that’s not meant to be changed in the first place — such as critical 
information or records — you should choose tuple data type over lists.

But if you know that the data will grow and shrink during the runtime of the application, 
you need to go with the list data type.
Reference: https://builtin.com/software-engineering-perspectives/python-tuples-vs-lists#:~:text=Tuples%20are%20immutable%20objects%20and,list%20syntax%20uses%20square%20brackets.
"""

# 7. Sets: Mutable collections of unordered, unique objects.
ip_addresses = {'100.0.0.1', '80.1.1.2', '5.6.1.4'}     # set type

# 8. FrozenSets: Immutable collections of unordered unique objects.
frozen_user_ids = frozenset([1001, 1002, 2003, 543])    # frozenset type

# 9. Dictionaries: Collections of unordered key-value pairs
friend = {'name': 'Alice', 'age': 30, 'is_employed': True}  # dict type