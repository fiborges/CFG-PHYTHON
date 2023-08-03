# Python Class - Introduction to Basic Concepts

## Input Function
The `input()` function is used to get user input from the keyboard. It allows you to prompt the user for information and store the input in a variable. Here's an example of how to use it:

```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

## Importing Libraries
Python allows you to use external libraries to extend its functionality. 
You can import libraries using the import keyword. Here's an example of importing the math 
library to perform mathematical operations:

```python
import math

# Calculate the square root of a number
num = 16
sqrt = math.sqrt(num)
print("Square root of", num, "is", sqrt)
```

## While Loops
A while loop is used to repeat a block of code as long as a condition is true. It continues executing the code until the condition becomes false. 
Here's an example of a while loop that counts down from 5 to 1:

```python
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1

```
## For Loops
A for loop is used to iterate over a sequence of elements (like a list, tuple, or string) or a range of numbers. It executes a block of code for each element or
number in the sequence.
Here's an example of a for loop that prints the numbers from 1 to 5:

```python
for num in range(1, 6):
    print(num)


```

## Functions
Functions are blocks of code that perform a specific task and can be reused throughout your program. They are defined using the def keyword. Here's an 
example of a function that calculates the sum of two numbers:

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 10)
print("Result:", result)  # Output: 15

```

## Putting It All Together
Here's a comprehensive example that combines the concepts we've learned:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def greet(name):
    print("Hello, " + name + "!")

name = input("Enter your name: ")
greet(name)

for i in range(1, 6):
    print(i)

num = 7
if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")

result = factorial(5)
print("Factorial of 5:", result)


```
