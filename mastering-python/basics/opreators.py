## Operators in Python
# Operators are used to perform operations on variables and values.
# There are several types of operators in Python, including arithmetic, comparison, logical, and assignment operators.

# 1 - Arithmetic Operators
    
x = 10
y = 5

print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x % y)  # Modulus
print(x ** y) # Exponentiation

# 2 - Comparison Operators

print(x == y)  # Equal to
print(x != y)  # Not equal to
print(x > y)   # Greater than
print(x < y)   # Less than
print(x >= y)  # Greater than or equal to
print(x <= y)  # Less than or equal to

# 3 - Logical Operators

print(x > 5 and y < 10)  # Logical AND
print(x > 5 or y < 10)   # Logical OR
print(not(x > 5))        # Logical NOT

# 4 - Assignment Operators

x += 5  # Add and assign
print(x)  # Output: 15

x -= 3  # Subtract and assign
print(x)  # Output: 12

x *= 2  # Multiply and assign
print(x)  # Output: 24

x /= 4  # Divide and assign
print(x)  # Output: 6.0

x %= 5  # Modulus and assign
print(x)  # Output: 1.0

x **= 3  # Exponentiation and assign
print(x)  # Output: 1.0

x //= 2  # Floor division and assign
print(x)  # Output: 0.0

# 5 - Bitwise Operators

print(x & y)  # Bitwise AND
print(x | y)  # Bitwise OR
print(x ^ y)  # Bitwise XOR

# 6 - Membership Operators

my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # True
print(6 not in my_list)  # True

# 7 - Identity Operators

a = 5
b = 5
print(a is b)  # True
print(a is not b)  # False
