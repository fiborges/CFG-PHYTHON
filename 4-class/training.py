#Exercise: Task Manager

#Create a list of tasks with their names and due dates.
from datetime import datetime

tasks = [
    {"name": "Finish project proposal", "due_date": "2023-08-10"},
    {"name": "Buy groceries", "due_date": "2023-07-30"},
    {"name": "Exercise", "due_date": "2023-07-28"},
    {"name": "Read a chapter of a book", "due_date": "2023-07-29"}
]

current_date = datetime.strptime("2023-07-27", "%Y-%m-%d")  # Convert current_date to a datetime objectp~
#Sort the tasks by their due dates in ascending order.

sorted_tasks = sorted(tasks, key=lambda task: task["due_date"])
print("Tasks sorted by due date (ascending):")
for index, task in enumerate(sorted_tasks, start=1):
    print(f"Task {index}: {task['name']}  Due: {task['due_date']}")

#Find the task that has the closest due date.

closest_due_task = min(tasks, key=lambda task: abs((datetime.strptime(task["due_date"], "%Y-%m-%d") - current_date).days))
print("Task with closest due date:", closest_due_task["name"], "Due:", closest_due_task["due_date"])

#Calculate the number of tasks that are overdue.

overdue_tasks = [task for task in tasks if datetime.strptime(task["due_date"], "%Y-%m-%d") < current_date]
num_overdue = len(overdue_tasks)
print("Number of overdue tasks:", num_overdue)

#Calculate the average number of days remaining for all tasks.

from datetime import datetime

avg_days_remaining = sum((datetime.strptime(task["due_date"], "%Y-%m-%d") - current_date).days for task in tasks) / len(tasks)
print("Average days remaining:", avg_days_remaining)

'''
In this exercise, we're using lists, dictionaries, and datetime functions to manage tasks and deadlines. 
This scenario relates to task management, which is something most people encounter in their daily lives. 
It showcases how Python can help you organize, sort, and analyze data in a practical context.

'''