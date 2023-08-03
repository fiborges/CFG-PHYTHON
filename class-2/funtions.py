#functions
#is a reusable block of code that contains one or more Python statements and used for performing a specific task.
# Code re-usability, Improves Readability, Avoid redundancy.

#def hello():
#    print('Hello, class!')

#hello()

# Pass single argument to a function
def hello(name):
    print('Hello,', name)

hello('Maria')
hello('Kim')
hello('Olya')

# Pass multiple arguments
def some_function(name, job):
    print(name, 'is a', job)

some_function('developer', 'Fiona')

def some_function(name, job='developer'):
    print(name, 'is a', job)
    
some_function('Fiona')
some_function('Fiona', 'manager')


#Greeting Function:

def greet(name):
    print(f"Hello, {name}! How are you today?")

# Call the function
greet("Alice")
greet("Bob")


#Addition Function

def add_numbers(a, b):
    return a + b

result = add_numbers(5, 10)
print("Result:", result)  # Output: 15


#Factorial Function

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print("Factorial of 5:", result)  # Output: 120


#Temperature Conversion Functions

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temp_celsius = 25
temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
print(f"{temp_celsius} degrees Celsius is {temp_fahrenheit} degrees Fahrenheit.")

temp_fahrenheit = 77
temp_celsius = fahrenheit_to_celsius(temp_fahrenheit)
print(f"{temp_fahrenheit} degrees Fahrenheit is {temp_celsius} degrees Celsius.")


#Check Prime Number Function

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

num = 17
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


#List Sum Function:

def list_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

my_list = [1, 2, 3, 4, 5]
result = list_sum(my_list)
print("Sum of the list:", result)  # Output: 15
