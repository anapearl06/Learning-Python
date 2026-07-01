# Numbered Task List

def generate_numbered_tasks(tasks):
    numbered_tasks = []

    for index, task in enumerate(tasks, start=1):
        numbered_tasks.append(f"{index}. {task}")

    return numbered_tasks

# Example list
tasks = ["Study Python", "Complete Assignment", "Exercise"]

result = generate_numbered_tasks(tasks)

for task in result:
    print(task)
    