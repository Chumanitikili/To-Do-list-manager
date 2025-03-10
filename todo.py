import os
from datetime import datetime

def load_tasks():
    """Load tasks from the file."""
    if not os.path.exists('tasks.txt'):
        return []
    
    with open('tasks.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    """Save tasks to the file."""
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(task):
    """Add a new task to the list."""
    tasks = load_tasks()
    date = datetime.now().strftime("%Y-%m-%d")
    task_with_date = f"[{date}] {task}"
    tasks.append(task_with_date)
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks():
    """Display all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
        return
    
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task(task_number):
    """Delete a task by its number."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks to delete!")
        return
    
    try:
        task_idx = int(task_number) - 1
        if 0 <= task_idx < len(tasks):
            removed_task = tasks.pop(task_idx)
            save_tasks(tasks)
            print(f"Deleted task: {removed_task}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    while True:
        print("\n=== Todo List Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        
        elif choice == '2':
            view_tasks()
        
        elif choice == '3':
            view_tasks()
            task_num = input("Enter the task number to delete: ")
            delete_task(task_num)
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main() 
    