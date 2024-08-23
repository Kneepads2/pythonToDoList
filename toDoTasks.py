import os

#Kneepads2 - Dylan - 5/21/2021

#directly set the base directory and file path
file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'tasks.txt') #os.path.expanduser('~') makes it so that the code can save the file to anyone's desktop without having to get their username

#ensure the directory exists (though it should already exist as per your description)
os.makedirs(os.path.dirname(file_path), exist_ok=True)

if os.path.exists(os.path.dirname(file_path)):
    print("Directory exists.")
else:
    print("Directory does not exist.")

#function to save tasks to the file
def save_tasks(tasks):
    try:
        with open(file_path, "w") as file:
            for task in tasks:
                file.write(task + "\n")
            file.flush()  #ensure all data is flushed to disk
    except Exception as e:
        print(f"An error occurred during saving: {e}")

def load_tasks():
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

#initialize the list of tasks by loading from the file
tasks = load_tasks()

print("\nTo-Do List\n========================\n")

while True:
    action = input("1. Add a task\n2. View tasks\n3. Remove a task\n4. Exit\nSelect an action: ")

    if action == '1' or action.lower() == 'add':
        #add a task
        task = input("Enter the task: ")
        tasks.append(task)
        save_tasks(tasks)  #save the updated tasks list to the file
        print(f"Task '{task}' added!\n")

    elif action == '2' or action.lower() == 'view':
        #view tasks
        if tasks:
            print("\nYour tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
            print("")  #add a newline for better formatting
        else:
            print("\nNo tasks added yet.\n")

    elif action == '3' or action.lower() == 'remove':
        #remove a task
        if tasks:
            print("\nYour tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
            
            try:
                task_number = int(input("Enter the task number to remove: "))
                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    save_tasks(tasks)  #save the updated tasks list to the file
                    print(f"Task '{removed_task}' removed!\n")
                else:
                    print("Invalid task number.\n")
            except ValueError:
                print("Please enter a valid number.\n")
        else:
            print("\nNo tasks to remove.\n")

    elif action == '4' or action.lower() == 'exit':
        print("Exiting..")
        break

    else:
        print("Invalid action. Please select a valid option.\n")
