from typing import TypedDict

#It is like structure in c++ and c
#It provides static type checking. you need "mypy" to detect it

class Movie(TypedDict):
    title: str
    year: int
    rating: float

# Creating an instance of the TypedDict
myliked_movie_one: Movie = {
    "title":"Inception",
    "year":2009,
    "rating":8.7
}

# Accessing Values
print(myliked_movie_one["title"])
print(myliked_movie_one["year"])

# Modifying values
myliked_movie_one["rating"] = 8.9

myliked_movie_one["year"] = "after 2012"
"""
with mypy, above line gives error as below 
etype_dict.py:25: error: Value of "year" has incompatible type "str"; expected "int"  [typeddict-item]
Found 1 error in 1 file (checked 1 source file)
"""

# Passing typeDict as function parameter
# -> None : this shows that function is returning nothing
def process_movie(mov: Movie) -> None:
    """Prints movie details."""
    print(f'Title: {mov["title"]}')
    print(f'Year: {mov["year"]}')
    print(f"Rating: {mov['rating']}")

# Correct usage
amovie = {'title': 'Alice', 'year': 1990, 'rating': 8.5}
process_movie(amovie)

# Incorrect usage (missing required keys)
m = {'title': 'Alice'}
# process_movie(m) # This will throw type error

# Defining a TypedDict with optional keys
class Employee(TypedDict, total=False):
    name: str
    age: int
    department: str

# Creating an instance with optional keys
employee: Employee = {
    "name": "Alice"
}

# Accessing values
print(employee.get("name"))  # Output: Alice
#print(employee["age"]) # this will throw error ad "age" attribute has not been initiated
#To avoid such issue, use the get method
print(employee.get("age", "N/A"))  # Output: N/A (since age is not defined)

# Nested TypedDict
class Address(TypedDict):
    street: str
    city: str
    zip: str

class User(TypedDict):
    username: str
    email: str
    address: Address

# Creating an instance with nested Address
user: User = {
    "username": "johndoe",
    "email": "johndoe@example.com",
    "address": {
        "street": "123 Main St",
        "city": "NYC",
        "zip": "12345"
    }
}

# Accessing nested values
print(user["address"]["city"])  # Output: NYC