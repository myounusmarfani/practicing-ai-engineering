## Loops in Python
# In Python, loops are used to execute a block of code repeatedly as long as a certain condition is met. The most common types of loops are `for` loops and `while` loops.
# ## For Loop
# The `for` loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects.
# Example:

for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

## Note: range(5) generates a sequence of numbers from 0 to 4.
## Identation is important in Python, as it defines the block of code that belongs to the loop.

## Use of `for` loop with a list:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Output: apple, banana, cherry

### While Loop

i = 0
while i < 5:
    print(i)  # Output: 0, 1, 2, 3, 4
    i += 1  # Increment i by 1

## Note: The `while` loop continues to execute as long as the condition `i < 5` is true. Once `i` reaches 5, the loop stops.

while True:
    user_input = input("Enter 'exit' to stop the loop: ")
    if user_input.lower() == 'exit':
        break  # Exit the loop
    else:
        print(f"You entered: {user_input}")