# To-Do List Program in Python
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_todo_list(todo_list):
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

def add_task(todo_list):
    task = input("\nEnter the task you want to add: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

def remove_task(todo_list):
    if not todo_list:
        print("\nYour to-do list is empty, no task to remove.")
        return
    view_todo_list(todo_list)
    try:
        task_num = int(input("\nEnter the number of the task you want to remove: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task}' removed from the to-do list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input, please enter a number.")

def main():
    todo_list = []
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                view_todo_list(todo_list)
            elif choice == 2:
                add_task(todo_list)
            elif choice == 3:
                remove_task(todo_list)
            elif choice == 4:
                print("Exiting the To-Do List program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input, please enter a number.")
            
if __name__ == "__main__":
    main()
