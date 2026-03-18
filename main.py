tasks = []

def add_task():
    task = input("Enter task: ")
    deadline = input("Enter deadline: ")
    tasks.append((task, deadline))
    print("Task added!")

def view_tasks():
    for i, (task, deadline) in enumerate(tasks):
        print(f"{i+1}. {task} - Due: {deadline}")

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        break
    else:
        print("Invalid choice")