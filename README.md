# Todo List Manager

A simple command-line todo list manager that allows you to manage your tasks with basic operations.

## Features

- Add new tasks with automatic date stamps
- View all tasks
- Delete tasks by their number
- Tasks are stored persistently in a text file

## How to Use

1. Make sure you have Python installed on your system
2. Run the program by executing:
   ```
   python todo.py
   ```
3. Choose from the following options:
   - 1: Add a new task
   - 2: View all tasks
   - 3: Delete a task
   - 4: Exit the program

## File Structure

- `todo.py`: The main program file
- `tasks.txt`: Storage file for tasks (created automatically)

## Notes

- Tasks are automatically saved with the current date
- Tasks are numbered for easy reference when deleting
- The program will create tasks.txt if it doesn't exist