## Data Structures in Python
# Python provides several built-in data structures that allow you to store and organize data efficiently. The
# most commonly used data structures in Python are lists, tuples, sets, and dictionaries.
# ## Lists
# Lists are ordered collections of items that can be changed (mutable). They are defined using square brackets `[]`. Lists can contain elements of different data types, including other lists.
# Example:

students = ["Alice", "Bob", "Charlie"]
print(students)  # Output: ['Alice', 'Bob', 'Charlie']
print(type(students))  # Output: <class 'list'>

# You can access elements in a list using their index (starting from 0):
print(students[0])  # Output: Alice
print(students[1])  # Output: Bob
print(students[2])  # Output: Charlie

# Methods to manipulate lists include `append()`, `remove()`, `insert()`, and `pop()`:
students.append("David")  # Adds "David" to the end of the list
print(students)  # Output: ['Alice', 'Bob', 'Charlie', 'David']
students.remove("Bob")  # Removes "Bob" from the list
print(students)  # Output: ['Alice', 'Charlie', 'David']
students.insert(1, "Eve")  # Inserts "Eve" at index 1
print(students)  # Output: ['Alice', 'Eve', 'Charlie', 'David']
students.pop()  # Removes the last item from the list
print(students)  # Output: ['Alice', 'Eve', 'Charlie']
students.sort()  # Sorts the list in ascending order
print(students)  # Output: ['Alice', 'Charlie', 'Eve']
students.reverse()  # Reverses the order of the list
print(students)  # Output: ['Eve', 'Charlie', 'Alice']


### Tuples

# Tuples are ordered collections of items that cannot be changed (immutable). They are defined using parentheses `()`. Tuples can also contain elements of different data types, including other tuples.
# Example:

roll_numbers = (101, 102, 103)
print(roll_numbers)  # Output: (101, 102, 103)
print(type(roll_numbers))  # Output: <class 'tuple'>

# You can access elements in a tuple using their index (starting from 0):
print(roll_numbers[0])  # Output: 101

# Tuples do not have methods to modify their contents, but you can perform operations like concatenation and repetition:


### Sets

# Sets are unordered collections of unique items. They are defined using curly braces `{}` or the `set()` function. Sets are useful for storing distinct elements and performing mathematical set operations like union, intersection, and difference.
# Example:

fruits = {"apple", "banana", "cherry"}
print(fruits)  # Output: {'banana', 'cherry', 'apple'}
print(type(fruits))  # Output: <class 'set'>

## You can add and remove elements from a set using the `add()` and `remove()` methods:
fruits.add("orange")  # Adds "orange" to the set
print(fruits)  # Output: {'banana', 'cherry', 'orange', 'apple'}
fruits.remove("banana")  # Removes "banana" from the set
print(fruits)  # Output: {'cherry', 'orange', 'apple'}

### Dictionaries

# Dictionaries are unordered collections of key-value pairs. They are defined using curly braces `{}` with keys and values separated by colons `:`. Dictionaries allow you to store and retrieve data based on unique keys.
# Example:

users = {
    "user1": "Alice",
    "user2": "Bob",
    "user3": "Charlie"
    }

print(users)  # Output: {'user1': 'Alice
print(type(users))  # Output: <class 'dict'>


## Leaen it's methods: your task!


