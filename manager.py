# Task Manager Software - By Aiswarya Maddali
# CSE Student | Aspiring Software Developer

print("=== AISWARYA'S TASK MANAGER SOFTWARE ===")

tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print(f"Added: {task}")

    elif choice == "2":
        print("\n--- Your Tasks ---")
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete!")
        else:
            num = int(input("Enter task number to delete: "))
            if num > 0 and num <= len(tasks):
                tasks.pop(num-1)
                print("Deleted!")
            else:
                print("Wrong number!")

    elif choice == "4":
        print("Thank you for using my software! Bye!")
        break

    else:
        print("Please enter 1 to 4 only!")