"""
=========================================
Day 7 : Terminal-Based Task List Manager
=========================================

Manage your daily tasks directly from the terminal.
Tasks are automatically saved in a text file,
so they remain available even after closing the program.

Concepts Covered:
✔ File Handling
✔ Lists & Dictionaries
✔ Functions
✔ Loops
✔ Match-Case
✔ Exception Handling
"""

import os

TASK_FILE = "tasks.txt"


# Step 1 : Load Saved Tasks

def load_tasks():
    """Loads all saved tasks from the text file."""

    tasks = []

    if os.path.exists(TASK_FILE):

        with open(TASK_FILE, "r", encoding="utf-8") as file:

            for line in file:
                task_text, status = line.strip().rsplit("||", 1)

                tasks.append({
                    "text": task_text,
                    "done": status == "done"
                })

    return tasks


# Step 2 : Save Tasks

def save_tasks(tasks):
    """Saves all tasks back to the text file."""

    with open(TASK_FILE, "w", encoding="utf-8") as file:

        for task in tasks:

            status = "done" if task["done"] else "not_done"

            file.write(f"{task['text']}||{status}\n")


# Step 3 : Display Tasks

def display_tasks(tasks):
    """Displays all tasks with their completion status."""

    if not tasks:
        print("\n📭 No tasks found.\n")
        return

    print("\n========== YOUR TASKS ==========\n")

    for index, task in enumerate(tasks, start=1):

        checkbox = "✔" if task["done"] else " "

        print(f"{index}. [{checkbox}] {task['text']}")

    print()


# Step 4 : Main Task Manager

def task_manager():

    tasks = load_tasks()

    while True:

        print("=" * 40)
        print("      TERMINAL TASK MANAGER")
        print("=" * 40)

        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ").strip()

        match choice:

            # ---------------- Add Task ----------------

            case "1":

                task_text = input("Enter your task: ").strip()

                if not task_text:
                    print("❌ Task cannot be empty.\n")
                    continue

                tasks.append({
                    "text": task_text,
                    "done": False
                })

                save_tasks(tasks)

                print("✅ Task added successfully!")

            # ---------------- View Tasks ----------------

            case "2":

                display_tasks(tasks)

            # ------------ Mark as Completed ------------

            case "3":

                display_tasks(tasks)

                try:

                    task_number = int(input("Enter task number: "))

                    if 1 <= task_number <= len(tasks):

                        tasks[task_number - 1]["done"] = True

                        save_tasks(tasks)

                        print("✅ Task marked as completed!")

                    else:

                        print("❌ Invalid task number.")

                except ValueError:

                    print("❌ Please enter a valid number.")

            # ---------------- Delete Task ----------------

            case "4":

                display_tasks(tasks)

                try:

                    task_number = int(input("Enter task number to delete: "))

                    if 1 <= task_number <= len(tasks):

                        removed_task = tasks.pop(task_number - 1)

                        save_tasks(tasks)

                        print(f"🗑️ '{removed_task['text']}' deleted successfully!")

                    else:

                        print("❌ Invalid task number.")

                except ValueError:

                    print("❌ Please enter a valid number.")

            # ---------------- Exit ----------------

            case "5":

                print("\n👋 Thank you for using Task Manager!")
                break

            # ---------------- Invalid Option ----------------

            case _:

                print("❌ Please choose a valid option (1-5).")


# Program Entry Point

task_manager()