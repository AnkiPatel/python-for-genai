'''
A Python set is an unordered collection of unique, immutable elements.
Scenario to use it: 1) When you want to have a lookup in unique data set. 2) Avoid identity conflicts
'''

unqiue_ids = {1,2,3,'a','b',4} #OP:{1, 2, 3, 4, 'a', 'b'}
print(unqiue_ids)
#print(unqiue_ids[0]) #Sets does not support indexing hence you will get the error ''set' object is not subscriptable' while accessing through index
#Because set is unordered. There is no concept of first element or last element

# Print the set (order is not guaranteed)
print(unqiue_ids)

# Create an empty set ({} creates an empty dictionary, not a set)
empty_set = set()
empty_set.add(1)
print(empty_set) #OP:{1}

empty_set2 = {} # this will be dictionary, not the set. BE CAREFULL
# Check the type of {} (it's a dictionary)
print(type({}))  # Empty dict, not set

# Create a set from a list to get unique sentences
sentences = ['Hello world', 'AI is amazing', 'Hello world', 'Python is great']
unique_sentences = set(sentences)  # Duplicate 'Hello world' is removed
print(unique_sentences)

# Create an immutable set (frozenset)
immutable_tokens = frozenset(unqiue_ids)
print(immutable_tokens)

# immutable_tokens.add('abc') # Error: Cannot add to a frozenset (it's immutable)