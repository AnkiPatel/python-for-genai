# PYTHON FUNCTIONS

# use snack-case for the function naming. Python conventionally use it for function name.
def my_function():
    print('Hello Python World!')
    x = 10
    print(x ** x)

# DocSrings = A docstring is a string literal that occurs as the first statement in a function.
# module, class, or method definition.

def say_hello(name):
    """Prints a greeting message with the provided name.
        name : string"""
    print(f'Hello {name}!')

my_function()
# see the funciton "say_hello". first comment is DocString.
# Refere PEP 257 for Docstring Conventions


# 1. Using the help() function to display the docstring of say_hello
help(say_hello)

# 2. Accessing the __doc__ attribute directly
print(say_hello.__doc__)

