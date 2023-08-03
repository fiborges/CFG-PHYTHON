#The input() function allows you to input data after the program has started running

age = input("what is your age?")
print("hello. I am {}". format(age))

fruit = input('What fruit do you like? ')
veg = input('What veg do you like? ')
print('You like {} and you like {}'.format(fruit, veg))

#The int() function converts string value into integer values

apples_string = '12'
total_apples = int(apples_string) + 5
print(total_apples)

#input() always returns a string value. You can convert this string value to an integer with int()

purchased_apples = input('How many apples did you buy? ')
print(type(purchased_apples))
total_apples = int(purchased_apples) + 5
print(total_apples)
#type()

#exercise
friends = input('How many friends? ')
pizzas = int(friends) * 0.5
print('You need {} pizzas for {} friends'.format(pizzas, friends))

#or

friends = int(input('How many friends are at your house? '))
pizzas = friends * 0.5
print('You need {} pizzas for {} friends'.format(pizzas, friends))

'''
In Python, a module is a file containing Python definitions and statements. 
It allows you to organize related code together, making it easier to reuse and maintain in
your programs. Modules can include functions, classes, and variables that you can import into your 
Python scripts to use their functionality.

ex: import math

Once the module is imported, you can access its functions and variables using dot notation. 
For example, to use the sqrt function from the math module to calculate the square root of a number, 
you would write

'''

import math

result = math.sqrt(16)
print(result)  # Output: 4.0

'''
You can also import specific functions or variables from a module using the from import statement.
For example, if you only want to use the sqrt function from the math module, you can write:

from math import sqrt

result = sqrt(16)
print(result)  # Output: 4.0

In [ ]: import datetime
x = datetime.datetime.now()
print(x)

Can you think of any examples where this function would be useful?
Have you ever heard about a timestamp ?

Logging Timestamps - logging events or activities in your application

Date and Time Calculations - reference point for performing various date and time calculations.
For example, you can calculate the time elapsed between two events or schedule tasks

File Naming and Versioning - generating files dynamically, appending the current timestamp from datetime.now() to the 
file name can ensure uniqueness and help in versioning

Data Recording- timestamp data entries or records. It allows you to track when data was collected, logged, or modified.

Scheduling - scheduling tasks or jobs in your application

Testing - In unit testing, you may need to simulate specific timestamps for certain scenarios.

timestamp ?

is a way to represent a point in time, usually as a numerical value, typically the number of seconds or milliseconds that 
have elapsed since a specific reference point, such as the Unix epoch (January 1, 1970, 00:00:00 UTC). Timestamps are commonly
used for tracking and comparing time-related events, especially in databases, log files, and distributed systems.


In Python, datetime.now() can also provide a timestamp by converting the resulting datetime object to a Unix timestamp 
(number of seconds since the epoch) using the .timestamp() method, like this:

Now, about timestamps! It's like a secret code for time. Instead of saying the time in words like "3:30 PM," a timestamp
uses numbers to tell the time. It's like saying "I'm going to tell you the exact time, but I'll use a special code that 
only computers can understand."

So, a timestamp might look like a big number, such as 1678432929. It represents the number of seconds that have passed 
since a specific day in the past, like January 1, 1970. It's used in computer programs to make it easier to work with 
time and do calculations.

In Python, you can also get a timestamp using the datetime.now() function, which is like getting the current time in 
both regular words and the secret timestamp code at the same time!

unix - Unix is an operating system that was developed in the late 1960s and early 1970s.
represent time in a consistent and efficient manner.
decided to use a simple and convenient method of measuring time as the number of seconds that have elapsed since January 
1, 1970, at 00:00:00 Coordinated Universal Time (UTC).

Simplicity: straightforward and easy to understand.
Backward Compatibility: using the same starting point ensured compatibility with existing systems
Consistency: different computer systems can easily agree on the current time by just counting the number of 
seconds that have passed 
Efficiency: Storing time as a single integer (the number of seconds) is efficient in terms of memory and computation.


import datetime
x = datetime.datetime.now()
timestamp = x.timestamp()
print(timestamp)

'''
