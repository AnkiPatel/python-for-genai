# List Operations: Concatenation, Slicing, and Iteration

# -----------------------------
# 1. List Concatenation
# -----------------------------

print(' List Concatenation\n------------------------')
l1 = [3, 4]
print(l1, id(l1))   # Prints list and its memory address #OP:[3, 4] 1704387388352

l1 = l1 + [5, 6]    # Creates a new list (concatenation) #OP:[3, 4, 5, 6] 1704387195136
print(l1, id(l1))   # Memory address changes

l1 += [7, 8]        # Modifies the existing list in place
print(l1, id(l1))   # Memory address remains the same #OP:[3, 4, 5, 6, 7, 8] 1704387195136

# extend() adds elements individually
l1.extend([11, 12])
print(l1)  # Output: [3, 4, 5, 6, 7, 8, 11, 12]
print(id(l1)) #OP:1704387195136

# append() vs extend()
l1.append(['a', 'b'])   # Appends the list as a single element
l1.extend(['x', 'y'])   # Extends the list with individual elements
print(l1)               #OP:[3, 4, 5, 6, 7, 8, 11, 12, ['a', 'b'], 'x', 'y']

# -----------------------------
# 2. List Slicing (works as the same way as the string slicing)
# -----------------------------
print(' List Slicing\n------------------------')
numbers = [1, 2, 3, 4, 5]

# Slicing [start:end] (end is exclusive)
nums = numbers[1:4]
print(f'nums: {nums}')          # Output: [2, 3, 4]
print(f'numbers: {numbers}')    # Original list remains unchanged #OP:numbers: [1, 2, 3, 4, 5]

# Various slicing examples
print(numbers[:3])    #OP:[1, 2, 3] #(first three elements)
print(numbers[2:])    #OP:[3, 4, 5] #(from index 2 onward)
print(numbers[1:5:2]) #OP:[2, 4] #(step of 2)
print(numbers[::-1])  #OP:[5, 4, 3, 2, 1] #(reversed list)

# -----------------------------
# 3. Iteration and Membership Testing
# -----------------------------
print(' Iteration and Membership Testing\n------------------------')
ip_list = ['192.168.0.1', '192.168.0.2', '10.0.0.1']

# Iterating over the list
for ip in ip_list:
    print(f'Connecting to {ip}')

# Checking for membership in a list
target_id = '10.0.0.1'
if target_id in ip_list:
    print(f'{target_id} is in the list')

some_ip = '192.134.8.0'
if some_ip not in ip_list:
    print(f'No addresses with the {some_ip=} found in the list')

# -----------------------------
# LIST GOTCHAS (Common Pitfalls)
# -----------------------------
print('  LIST GOTCHAS\n------------------------')
# 1. Modifying one list affects another if they share the same reference
l1 = [1, 2, 3]
l2 = l1  # l2 references the same object as l1
l2[0] = 'xx'
l2.append(10)
print(l2, l1)  #OP:['xx', 2, 3, 10] ['xx', 2, 3, 10]
# Both lists are modified because they reference the same object


# To avoid this, use list.copy() for a shallow copy
l3 = l1.copy()
l3.append('abc')
print(l3, l1) #OP:['xx', 2, 3, 10, 'abc'] ['xx', 2, 3, 10]
# l3 is modified independently

# 2. Removing items from a list while iterating can cause unexpected behavior
nums = [1, 2, 3, 4, 5, 6, 7]
for n in nums:
    if n < 5:
        nums.remove(n)  # This skips elements because the list shrinks while iterating
print(nums)             # Output may be unexpected: [2, 4, 5, 6, 7]

# Correct approach: Create a new list instead of modifying the original one during iteration
nums = [1, 2, 3, 4, 5, 6, 7]
new_list = []
for n in nums:
    if n < 5:
        new_list.append(n)
print(new_list)

# shorter way for such operation
new2_list = [n for n in nums if n >= 5]
print(new2_list)  # Output: [5, 6, 7]
