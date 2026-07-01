# Task Completion Tracker

def mark_completed_tasks(tasks):
    completed_tasks = []

    for task in tasks:
        completed_tasks.append(f"Completed: {task}")

    return completed_tasks

# Example list
tasks = ["Study Python", "Complete Assignment", "Exercise"]

result = mark_completed_tasks(tasks)

for task in result:
    print(task)