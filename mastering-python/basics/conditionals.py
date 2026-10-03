## Conditionals in Python
# # In Python, conditionals are used to perform different actions based on different conditions. The most common conditional statements are `if`, `elif`, and `else`.
# # ## If Statement
# The `if` statement is used to test a specific condition. If the condition evaluates to `True`, the block of code within the `if` statement is executed.
# Example:

number = input("Enter a number: ")
if number > 0:
    print("The number is positive.")

# ## Elif Statement
# The `elif` statement stands for "else if" and allows you to check multiple conditions. If the first condition is `False`, the program checks the next condition, and so on.
# Example:

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")

# ## Else Statement
# The `else` statement is used to execute a block of code if none of the previous conditions are `True`.
# Example:

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
    