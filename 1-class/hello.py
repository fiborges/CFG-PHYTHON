print("hello, world")
print("filipa borges \n joao")

# This is a single-line comment

"""
This is a multi-line comment.
You can write comments across multiple lines.
"""

# Addition
result = 5 + 3

# Subtraction
result1 = 10 - 4

# Multiplication
result2 = 2 * 6

# Division
result3 = 15 / 3

# Exponentiation
result4 = 2 ** 3  # 2 raised to the power of 3

print(result1)
print(result2)
print(result3)
print(result4)

# dar entrada do nosso nome
name = input("Enter your name: ")
print("Hello, " + name + "!")

age = 18

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just turned 18!")
else:
    print("You are an adult.")

# For loop

for i in range(5):
    print(i)

for i in range(6, 10):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# criar uma funçao que se chama greet!!
def greet(name):
    print("Hello, " + name + "!")

# Call the function
greet("Alice")


fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])  # Output: "apple"

# Modifying elements
fruits[1] = "orange"

# Looping through a list
for fruit in fruits:
    print(fruit)

# Números inteiros
x = 5
y = -99
z = 1048

# Números de ponto flutuante
a = 5.6
b = 9.0
c = -67.1001

# Boolean
is_student = True

# Operações matemáticas com inteiros e floats
soma = x + a
multiplicacao = y * b
divisao = z / c

print(soma)          # Output: 10.6
print(multiplicacao) # Output: -891.0
print(divisao)       # Output: -15.609279172403866

text = "hello, world!"
upper_text = text.upper()
print(upper_text)  # Output: "HELLO, WORLD!"

text = "Hello, World!"
lower_text = text.lower()
print(lower_text)  # Output: "hello, world!"

text = "welcome to python programming"
title_text = text.title()
print(title_text)  # Output: "Welcome To Python Programming"
