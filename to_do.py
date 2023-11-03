# import firebase module with credentials
import firebase_admin
from firebase_admin import db, credentials
import datetime

# initialize firebase admin using private key
key = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(key, {"databaseURL": "https://to-do-1c749-default-rtdb.firebaseio.com/"})

# set database reference pointer
root = db.reference("/")

# get the current date and time
datetime_object = datetime.datetime.now()
time = datetime_object.strftime("%I:%M %p")
date = datetime_object.strftime("%B %d, %Y")

# db.reference("/").update({f"Task 5": ["Yet more new task details", f"{date}", f"{time}"]})
task_number = 1
# db.reference("/").update({f"Task {task_number}": ["New task details", f"{date}", f"{time}"]})
print(f"Database contents: {root.get()}\n")

# delete task 1 in the database
# db.reference(f"/Task {task_number}").delete()
# print(f"Database contents: {root.get()}")

task_number = 2
# db.reference("/").update({f"Task {task_number}": ["More new task details", f"{date}", f"{time}"]})
# print(f"Database contents: {root.get()}\n")

# delete task 2 in the database
# db.reference(f"/Task {task_number}").delete()
# print(f"Database contents: {root.get()}")


def add_task(tasks):
    if "Task 1" in tasks:
        print("\nIt's here!")


def delete_task(task_number, tasks):
    
    # set key name default value
    key_name = ""
    
    # find key in tasks dictionary
    for number, task in enumerate(tasks):
        if task_number == number:
            key_name = task

    # if key name is not in database, tell user and return
    if key_name == "":
        print("Invalid task! Exiting delete task.")
        return

    # verify deletion by user
    print("\nVerify you want to delete this task:")
    print(tasks[key_name][0])
    user_choice = input(f"y/n? ")
    if user_choice.lower() != "y":
        print("\nExiting delete task.\n")
        return
    
    # delete the task
    print("\nPlease wait. Deleting selected task...")
    db.reference(f"/{key_name}").delete()
    print(f"\nTask\n{tasks[key_name][0]}\nwas deleted.\n")


def update_task(task_number, task):
    pass


# print out all tasks in the database
def view_tasks(tasks):
    
    # print the number of tasks in database in double underlined white font
    print(f"\n\033[1;37m\033[1;21mYou have {len(tasks)} tasks:\033[00m")
    
    # display list of tasks
    for number, task in enumerate(tasks):
        print(f"\n\033[1;31mTask {number + 1}\033[00m")
        print(f"\033[1;33m{tasks[task][0]}\033[00m")
        print("set up on")
        print(f"\033[1;33m{tasks[task][1]}\033[00m", end=" ")
        print(f"at \033[1;33m{tasks[task][2]}\033[00m")
    
    # print clean line
    print()


# main function
def main():

    # set defaults for variable scope
    task = ""
    user_choice = ""
    task_number = 0

    # welcome message
    print("\nWelcome to Firebase To-Do Task Manager.\n")
    
    # to do task options loop - loop until user selects quit
    while True:
    
        # print menu and loop until a valid user choice is made
        while True:
            
            # print menu
            print("Menu:")
            print("1. Add a task")
            print("2. Delete a task")
            print("3. View tasks")
            print("4. Update a task")
            print("5. Quit Firebase To-Do Task Manager")
            
            # get user choice
            user_choice = input("\nSelect 1, 2, 3, 4, or 5: ")
            
            # if choice is valid, break out of loop
            if(user_choice == "1" or 
            user_choice == "2" or 
            user_choice == "3" or
            user_choice == "4" or
            user_choice == "5"):
                break
            
            # if user_choice is not good, print message and loop again
            else:
                print("\nInvalid input. Please select 1, 2, 3, 4, or 5.\n")

        #get database json information and store in a dictionary
        tasks = root.get()

        # act on user choice
        # TODO add a task to the to do list
        if (user_choice == "1"):
            print("\nAdding task")

        # delete a task from the to do list
        elif (user_choice == "2"):
            view_tasks(tasks)
            while True:
                user_choice = input("Which task do you want to delete? ")
                if user_choice.isdigit():
                    task_number = int(user_choice) - 1
                    if task_number >= 0 and task_number < len(tasks):
                        delete_task(task_number, tasks)
                        break            
                print("Invalid selection, input a valid task number.")

        # view all tasks
        elif (user_choice == "3"):
            if tasks != None:
                view_tasks(tasks)
            else:
                print("You have no tasks to view.")

        # TODO update a task
        elif (user_choice == "4"):
            print("Updating task")

        # quit Firebase to do task manager
        elif (user_choice == "5"):
            print("\nGoodbye. Thanks for using Firebase To-Do Task Manager!\n")
            return 0


# if run directly, call main function, otherwise do nothing
if(__name__ == "__main__"):
    main()