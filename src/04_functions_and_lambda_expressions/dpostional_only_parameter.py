
# positional parameter are mentioned with /

# In this example, a and b are positional only parameters, while c and d can be passed either positionally
# or by keyword.

"""
Why use positional only parameters?
Ans: We use them for clarity, error prevention and performance.
    Explicitly stating which arguments must be positional improves code readability and maintainability.
-> This is useful especially for different APIs, where using positional only parameters improves the clarity of the API.
-> They prevent accidental keyword arguments for parameters intended to be positional,
reducing the likelihood of unexpected behavior.
-> They also help in maintaining backward compatibility by preventing the reliance on parameter names,
-> which might change over time, and in some cases, positional only arguments can lead to slight performance improvements.
"""

def my_function(a, b, /, c, d):
    pass

def divide(numerator, denominator, /):
    """ Divies two numbers """
    if denominator == 0:
        raise ValueError('Division by Zero')
    return numerator / denominator

result = divide(10,2)
print(result)

# incorrect usage
#res = divide(numerator=8, denominator=2)
# above statment gives error: TypeError: divide() got some positional-only arguments passed as keyword arguments: 'numerator, denominator'
#print(res)

"""
In this example, numerator and denominator must be passed positionally.
This ensures that the order of the arguments is always clear and prevents potential errors.
"""

# ====================================


"""
In the below function definition.
The asterisk indicates the start of keyword only arguments.

Keyword only arguments are function parameters that must be passed by keyword when calling the The function,
they cannot be passed positionally.

A and B are positional only because a forward slash follows.
C can be positional or keyword.
D is keyword only and e is keyword only with a default value.
"""
def my_func(a, b, /, c, *, d, e=10):
    print(f"a: {a}, b: {b}, c: {c}, d: {d}, e: {e}")

my_func(5, 3, c=4, d=8, e=3)