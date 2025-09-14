
# COMMENTS IN PYTHON
# =================================

# use '#' for single line comment

# Example of commented-out code (useful for debugging or reference)
# total = sum([1, 2, 3])
# print(total)
# print(max([5, 6, 1, -2]))

# """ your text in multiline """  for multiline comment

"""
line   1
line   2
"""

"""
Example of a multi-line comment (docstring style),
typically used for docstrings.

temp = preprocess_data(raw_input)
model.train(temp)
"""

# Best practices for comments
#--------------------------------
# 1: Be clear and Concise

counter = 0

# Bad comment: Too vague, doesn't add value
# increment
counter += 1

# Good comment: Clearly explains the purpose
# Increment the counter to track the number of iterations
counter += 1

# 2: Explain the "Why", Not Just the "What"

# Bad comment: States the obvious
# Set is_active to True
is_active = True

# Good comment: Provides context on why the value is set
# Activate the user account after email verification
is_active = True

# 3: Keep Comments Up-to-Date
# (Reminder: Ensure comments reflect the latest code logic)

# 4: Avoid Obvious Comments

# Bad comment: The code itself is self-explanatory
# Assign 5 to x
x = 5


# NAMING CONVENTION FOR VARIABLE NAME
# ============================================================

# 1: Allowed characters ( ato z, Ato Z, 0 to 9 and _)
total_count = 100 #valid
_hidden_value = 42 # valid, but not recommended
# 1st_place = 'Gold' #invalid, Start with a digit

# 2: Avaoid leading underscores
# in python variable starting with 1 or 2 underscores has special meaning so avoid using it

# 3: No special character or spaces
# $abc = 10  #  not valid
# user-name = 'Alice' # not valid
# user name = 'tanvi'

# 4: Do not use reserved keyword
'''
if, else, for -- this are the reserved keyword
'''

# 5: Case sensitivity
'''
python is case-sensitive 
Avar = 18 and avar - 18 are two different variables.
'''

# 6: Recommendation is, Use Descriptive Names and snake_case, Avoid camel case

max_value = 99
total_items = 23
avoidThisStyle = 'Good for java only' # camel case is not recommended in python

# 7: Don't shadow built-in names
list = [1,2,3] #not recommended, list is built in type in python

# 8: Define constant , Use all upper case letter
DAYS_IN_YEARS = 365
MAX_CONNECTIONS = 10


