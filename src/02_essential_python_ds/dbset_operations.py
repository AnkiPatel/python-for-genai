# Set operations and methods

# Create a set (duplicates are automatically removed)
unique_ids = {1, 2, 3, 1}
print(unique_ids)  # Output: {1, 2, 3} (order may vary)

# Add an element to the set
unique_ids.add('a')
print(unique_ids)  # Output: {1, 2, 3, 'a'} (order may vary)

# Remove an element from the set
unique_ids.remove('a')
print(unique_ids)  #OP:{1, 2, 3} (order may vary)

# Add an immutable element (like a tuple) to the set
# NOTE: You cannot add list as set element becuase list is mutable
mutable_elements = ['a','b']
#unique_ids.add(mutable_elements) # this gives error 'unhashable type: 'list''

immutable_element = tuple([1, 2])
unique_ids.add(immutable_element) #op:{1, 2, (1, 2), 3}

# Iterate through the set (order is not guaranteed)
for uid in unique_ids:
    print(uid)

# Check for membership in the set
if 'token2' in unique_ids:
    print('Token found!')
else:
    print('Token not found!')  # Output: Token not found!