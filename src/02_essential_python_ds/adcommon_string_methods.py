# COMMON STRING METHODS

# Demonstrating type checking for an integer and a string
x = 10
s = 'abc'
print(type(x), type(s))  # Output: <class 'int'> <class 'str'>

# STRING CASE CONVERSIONS

print('STRING CASE CONVERSIONS\n--------------------------')
model_output = 'ai IS the future of everything!'

# Convert the string to uppercase
print(model_output.upper())  # 'AI IS THE FUTURE OF EVERYTHING!'

# Convert the string to lowercase
print(model_output.lower())  # 'ai is the future of everything!'

# The original string remains unchanged (strings are immutable)
print(model_output)  # 'ai IS the future of everything!'

# STRING STRIPPING
print('STRING STRIPPING\n--------------------------')
response = ' 🤖 Hello, human! 🤖 '

# Remove leading and trailing whitespace characters
print(response.strip())  #Output:🤖 Hello, human! 🤖
print(response) # Again,original string will be unchanged. To preserve the result you have to assign to new variable

# Remove specific leading and trailing characters (' 🤖')
print(response.strip(' 🤖'))  #Output:Hello, human!

# WORD OCCURRENCE COUNTING
print('STRING COUNTING\n--------------------------')
text = 'AI is the FUture. Embrace the future of AI!'

#Count occurrences of 'future' (case-insensitive)
print(text.count('AI')) # Output:2

# Count occurrences of 'future' (case-insensitive)
print(text.lower().count('future')) # Output:2

# STRING SPLITTING
print('STRING SPLITTING\n--------------------------')
statement = 'AI breakthrough at every step'
#Split the string into a list of words
words = statement.split()
print(words) #output:['AI', 'breakthrough', 'at', 'every', 'step']

statement = 'Split-the-string-into-a-list-of-words'
words = statement.split('-')
print(words) #output:['Split', 'the', 'string', 'into', 'a', 'list', 'of', 'words']
# STRING JOINING

terms = ['']

# STRING JOINING
print('STRING JOINING\n--------------------------')
#She's a fun person to be with.
terms = ['She', 'is', 'a', 'fun', 'person', 'to', 'be', 'with']

# Join the list elements into a single string, separated by ', '
print(', '.join(terms)) #Output:She, is, a, fun, person, to, be, with
# Join the list elements into a single string, separated by ' '
print(' '.join(terms))  #Output:She is a fun person to be with

# STRING PREFIX AND SUFFIX REMOVAL (Python 3.9+)
print('STRING PREFIX AND SUFFIX REMOVAL\n--------------------------')
url = 'https://exmpale.com'
print('Original url' + url)

# Remove 'https://' from the beginning of the url
cleaned_url = url.removeprefix('https://')
print('Cleaned url: ' + cleaned_url)

testFileName = 'some_data_file.pdf'
cleaned_filename = testFileName.removesuffix('.pdf')
print('Cleaned filename: ' + cleaned_filename)

# USING HELP TO VIEW DOCUMENTATION

# Display available string methods and documentation
# help(str)

# Display help information for the `strip()` method
help(str.strip)