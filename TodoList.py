tasks = []

while True:
    print("\nTO-DO LIST")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Delete Task")
    print("4.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter Task: ")
        tasks.append(task)
        print("Task Added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No Tasks")
        else:
            for i, task in enumerate(tasks, 1):
                print(i, task)

    elif choice == "3":
        num = int(input("Enter task number: "))
        if 0 < num <= len(tasks):
            tasks.pop(num-1)
            print("Deleted")

    elif choice == "4":
        break