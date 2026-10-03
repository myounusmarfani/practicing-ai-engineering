## Input and Output
# In Python, you can take input from the user using the input() function. The input() function reads a line from the input (usually from the user), converts it into a string, and returns it. You can also use the print() function to display output to the console.
# For example, you can ask the user for their name and then greet them:

name = input("Enter your name: ")
print("Hello, " + name + "!") 


## Expected Output
"""

Enter your name: Younus
Hello, Younus!

"""


## Different Types of Input

number = int(input("Enter a number: "))  # Convert input to an integer
print("The number you entered is:", number)

word = input("Enter a word: ")  # Input as a string
print("The word you entered is:", word)

decimal = float(input("Enter a decimal number: "))  # Convert input to a float
print("The decimal number you entered is:", decimal)

boolean_input = input("Enter True or False: ")  # Input as a string
if boolean_input.lower() == "true":
    boolean_value = True
elif boolean_input.lower() == "false":
    boolean_value = False
else:
    boolean_value = None  # Invalid input

print("The boolean value you entered is:", boolean_value)


# Some terminologies:
# .lower() - This method converts all characters in a string to lowercase.
# if/elif/else - These are conditional statements used to execute different blocks of code based on certain conditions.
