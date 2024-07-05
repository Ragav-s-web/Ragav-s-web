Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Function to display the to-do list
... def display_todo_list(todo_list):
...     if not todo_list:
...         print("Your to-do list is empty.")
...     else:
...         print("Your to-do list:")
...         for index, task in enumerate(todo_list, start=1):
...             print(f"{index}. {task}")
... 
... # Function to add a task to the to-do list
... def add_task(todo_list, task):
...     todo_list.append(task)
...     print(f"Task '{task}' added to the to-do list.")
... 
# Function to remove a task from the to-do list
def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task index. Please try again.")

# Main program
def main():
    todo_list = []
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Display to-do list")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            task = input("Enter the task to add: ")
            add_task(todo_list, task)
        elif choice == '3':
            task_index = int(input("Enter the index of the task to remo
