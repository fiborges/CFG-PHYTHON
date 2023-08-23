# Reading and Writing Files
## What is File I/O?
File I/O stands for Input/Output operations on files. It's a way for our programs to interact with files stored on our computer. We can read data from files, write data to files, and modify existing data within them.

## Writing to a File
Imagine you want to create a text file and put some text in it. Python makes this easy! We use the open() function to open or create a file and specify whether we want to read ('r'), write ('w'), or append ('a') to it.

```python

with open('example.txt', 'w') as file:
    file.write("Hello, this is a test!")
```

## Reading from a File
Now let's say you want to read the contents of a file. Python's got you covered there too!

```python

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

### Exercise 5.1: Creating a To-Do List Program
Think about a to-do list. We can create a program that lets you add tasks to a list and saves them to a file. Here's how it could work:

Ask the user to input a new task.
Read the existing tasks from the file.
Add the new task to the existing ones.
Save the updated tasks back to the file.

```python

new_task = input("Enter a new task: ")
with open('todo.txt', 'r') as file:
    tasks = file.read()
    tasks += new_task + '\n'
with open('todo.txt', 'w') as file:
    file.write(tasks)
```

## Working with CSV Files
### What is a CSV?
CSV stands for Comma-Separated Values. It's a file format used to store tabular data, like a spreadsheet. Each line in the file represents a row, and each value within a line is separated by a comma.

### Writing a CSV File
You can use Python's built-in csv module to create and write data to a CSV file. This is super handy for creating reports, logs, or structured data.

```python

import csv

field_names = ['name', 'age']
data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 32},
]

with open('people.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)

```

### Reading a CSV File
To read from a CSV file, you can use the csv.DictReader class provided by the csv module. It allows you to treat each row as a dictionary, making it easy to access data by column name.

```python

import csv

with open('people.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['name'], row['age'])
```

### Exercise 5.2: Finding the Shortest Tree
Let's say we have a CSV file with data about different trees, including their heights. We want to find the shortest tree.

```python

import csv

with open('trees.csv', 'r') as file:
    reader = csv.DictReader(file)
    heights = [int(row['height']) for row in reader]
    shortest_height = min(heights)
    print(f"The shortest tree is {shortest_height} meters tall.")
```
### Real-Life Context
Imagine you are part of a sports team, and you need to keep track of the players' information such as their names and ages. Using a CSV file makes it easy to manage this data and generate reports.
Suppose you have a CSV file with data about different players, including their ages. Let's find the youngest player using Python:

Open the CSV file.
Read the ages of all players.
Find the youngest age.
Display the youngest player's information.

```python
import csv

with open('players.csv', 'r') as file:
    reader = csv.DictReader(file)
    ages = [int(row['age']) for row in reader]
    youngest_age = min(ages)

    with open('players.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row['age']) == youngest_age:
                print(f"Youngest player: {row['name']} (Age: {row['age']})")

```
## Python Pip
### What is Pip?
pip is a package manager for Python. Think of it as a way to install, manage, and share Python libraries – sets of code created by other developers that you can use in your own projects.

### Why Use Pip?
Imagine you need to connect to the internet in your program, but you're not sure how to do it. Instead of building it from scratch, you can use a library like requests that simplifies the process. You can install it using pip:
### Real-Life Context
Imagine you are working on a project that requires sending HTTP requests to fetch data from the internet. Instead of writing the networking code from scratch, you can use the popular requests library to simplify the process.
```
pip install requests

```
## Conclusion
In this class, we've covered the basics of reading and writing files in Python, explored working with CSV files, and learned about pip, the Python package manager. These skills will come in handy as you continue your Python journey and build more complex programs!
