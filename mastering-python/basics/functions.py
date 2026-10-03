## Funtions are blocks of code that can be reused multiple times in a program. They help in organizing code, making it more readable, and reducing redundancy. In Python, functions are defined using the `def` keyword followed by the function name and parentheses.

# 1 - Defining a Function

def greet(name):
    """This function greets the person passed in as a parameter."""
    print(f"Hello, {name}!")

# 2 - Calling a Function
greet("Alice")  # Output: Hello, Alice!
greet("Bob")    # Output: Hello, Bob!
greet("Charlie")  # Output: Hello, Charlie!

## Components of a Function:
# - Function Name: The name of the function, which is used to call it.
# - Parameters: The values passed to the function when it is called.
# - Function Body: The block of code that performs the desired task.
# - Return Statement: The value that the function returns to the caller.


## Different Types of Functions in Python:
# 1. Built-in Functions: These are functions that are already defined in Python, such
#    as `print()`, `len()`, and `type()`.

# 2. User-defined Functions: These are functions that are defined by the user to perform specific tasks, like the `greet()` function defined above.
def add(a, b):
    """This function returns the sum of two numbers."""
    return a + b

# 3. Lambda Functions: These are small anonymous functions defined using the `lambda` keyword. They can take any number of arguments but can only have one expression.
square = lambda x: x ** 2
print(square(5))  # Output: 25
