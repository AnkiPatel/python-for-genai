# Key Python Operators: Assignment, Comparison, and Identity Operators

# Assignment Operator
# ======================
print('Assignment Operator')
a = 5
print(a)

# Augmented Assignment Operators
# ======================
print('Augmented Assignment Operators')
a += 2  # Equivalent to: a = a + 2
print(a)  # Output: 7

a -= 4  # Equivalent to: a = a - 4
print(a)  # Output: 3

# Other augmented assignment operators: *=, /=, **=, %=, //=
# ======================
a *= 10  # Equivalent to: a = a * 10
print(a)  # Output: 30

# Incrementing and decrementing (unlike java and c++, here ++ is NOT supported
# ======================
print('Incrementing and decrementing')
a += 1  # Equivalent to: a = a + 1
a -= 1  # Equivalent to: a = a - 1


# Comparison Operators
# ======================
print('Comparison Operators')
a, b = 10, 5
print(a == b)  # False: Checks if a is equal to b
print(a > b)   # True: Checks if a is greater than b

# Concept of mutable and immutable objects
"""
Mutable objects can be changed after they’re created,
while immutable objects can’t.

-> integer and string are immutable objects
"""
print('Concept of mutable and immutable objects')
a = 2
print(id(a))    # Prints the memory address of a
a += 3          # Modifies the value of a
print(id(a))    # Memory address changes since integers are immutable

# Identity Operators: 'is' and 'is not'
# ======================
# 'is' checks if two variables reference the same object in memory
print('Identity Operators')
m = 10
n = 10
print(id(m))    #140706394830024
print(id(n))    #140706394830024
print(m is not n)   #False
print(m is n)       #True


# Identity check with mutable objects
# list is mutable object
print('Identity check with mutable objects')
numbers = [1, 2, 3]
print(id(numbers))  # Prints the memory address of the list
numbers.append(10)  # Modifies the list (mutable)
print(id(numbers))  # Memory address remains the same