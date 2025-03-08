import json
import os

# File to store tasks
TASKS_FILE = 'tasks.json'


# Load tasks from the file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Warning: tasks.json is corrupted or empty. Starting with an empty task list.")
                return []
    return []


# Save tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)


# Add a new task
def add_task(tasks, task_description):
    tasks.append({"description": task_description, "completed": False})
    save_tasks(tasks)
    print(f'Task added: "{task_description}"')


# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for index, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        print(f"{index + 1}. [{status}] {task['description']}")


# Mark a task as complete
def complete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        print(f'Task "{tasks[task_index]["description"]}" marked as complete.')
    else:
        print("Invalid task number.")


# Main function to run the application
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            task_description = input("Enter the task description: ")
            add_task(tasks, task_description)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
            task_number = int(input("Enter the task number to complete: ")) - 1
            complete_task(tasks, task_number)
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
