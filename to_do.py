# import needed modules
import firebase_admin
from firebase_admin import db, credentials
import datetime
import threading

# initialize firebase admin using private key
key = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(key, {"databaseURL": 
    "https://to-do-1c749-default-rtdb.firebaseio.com/"})


# function to add a task to the database
def add_task(tasks):
    
    # create task prompt
    print("\nEnter the task to be added to your to-do list:")
    task = input()

    # verify task details with user
    print("\n\033[1;32mYou are about to create this task:\033[00m")
    print(f"\033[1;33m{task}\033[00m")
    user_choice = input("Is this correct (y/n)? ")

    # if choice is y, add task to database
    if user_choice.lower() == "y":
        
        # get unused task number for key
        # if tasks dictionary is empty, task number is 0
        if tasks == None:
            task_number = 0

        # otherwise, get the next empty integer key in the database
        else:
            task_number = 0
            for task_number in range(len(tasks) + 1):
                if f"Task {task_number + 1}" not in tasks:
                    break
            task_number += 1
        
        # get current date and time to insert into database
        date = get_date()
        time = get_time()
        
        # add to database 
        db.reference("/").update(
            {f"Task {task_number}": [f"{task}", f"{date}", f"{time}"]})

        # show user what was added
        print(f"\nOn \033[1;33m{date}\033[00m at ", end="")
        print(f"\033[1;33m{time}\033[00m you added the task:")
        print(f"\033[1;33m{task}\033[00m\n")
        
    # otherwise, return to menu without adding a task to the database
    else:
        print("\nQuitting add task and returning to menu...\n")


# function to delete a task from the database
def delete_task(task_number, tasks):
    
    # find key in tasks dictionary by calling find key function
    key_name = find_key(task_number, tasks)
        
    # remember old task name
    old_task = tasks[key_name][0]

    # verify deletion by user
    print("\n\033[1;31mYou are about to delete this task:\033[00m")
    print(f"\033[1;33m{old_task}\033[00m")
    user_choice = input(f"Is this correct y/n? ")
    
    # if choice is anything other than y, return to menu
    if user_choice.lower() != "y":
        print("\nExiting delete task and returning to menu.\n")
        return
    
    # delete the task
    print("\nPlease wait. Deleting selected task...")
    db.reference(f"/{key_name}").delete()
    print(f"\nTask\n\033[1;33m'{old_task}'\033[00m")
    print(f"was deleted on \033[1;33m{get_date()}\033[00m", end=" ")
    print(f"at \033[1;33m{get_time()}\033[00m.\n")


# function to update an existing task in the database
def update_task(task_number, tasks):
    
    # find key in tasks dictionary by calling find key function
    key_name = find_key(task_number, tasks)
    
    # remember old task
    old_task = tasks[key_name][0]

    # verify deletion by user
    print("\n\033[1;31mYou are about to update this task:\033[00m")
    print(f"\033[1;33m{old_task}\033[00m")
    user_choice = input(f"Is this correct y/n? ")

    # if user didn't choose y, return to menu
    if user_choice.lower() != "y":
        print("Exiting update task and returning to menu...")
        return

    # create prompt
    print("\nEnter new task information:")
    task = input()

    # verify the update with the user
    print(f"\033[1;31mYou are about to update this task:\033[00m")
    print(f"\033[1;33m{old_task}\033[00m")
    print("with")
    print(f"\033[1;33m{task}\033[00m")
    user_choice = input(f"Is this correct y/n? ")

    # if user didn't choose y, return to menu
    if user_choice.lower() != "y":
        print("\nExiting update task and returning to menu...\n")
        return

    # get current time and date to insert into the database
    date = get_date()
    time = get_time()

    # update the task in the database
    db.reference("/").update(
            {f"{key_name}": [f"{task}", f"{date}", f"{time}"]})

    # inform user of the changes
    print(f"\nOn {date} at {time} task")
    print(f"\033[1;33m{old_task}\033[00m")
    print("was updated to")
    print(f"\033[1;33m{task}\033[00m.\n")


# print out all tasks in the database
def view_tasks(tasks):
    
    # print the number of tasks in database in double underlined white font
    print(f"\n\033[1;37m\033[1;21mYou have {len(tasks)} tasks:\033[00m")
    
    # display list of tasks in color
    for number, task in enumerate(tasks):
        print(f"\n\033[1;31mTask {number + 1}\033[00m")       # red task header
        print(f"\033[1;33m{tasks[task][0]}\033[00m")          # task in yellow
        print("set up on")                                    # text in gray
        print(f"\033[1;33m{tasks[task][1]}\033[00m", end=" ") # date in yellow
        print(f"at \033[1;33m{tasks[task][2]}\033[00m")       # time in yellow
    
    # print clean line
    print()


# function to find the key in the database using the user input (task number)
def find_key(task_number, tasks):
    
    # find key in tasks dictionary
    for number, task in enumerate(tasks):
        if task_number == number:
            return task
        
    print("\nTask not found in database.\n")


# function to return current date and time
def get_date():
    
    # get current date
    datetime_object = datetime.datetime.now()
    date = datetime_object.strftime("%B %d, %Y")

    # return date and time in string format
    return date


#function to return current time
def get_time():
    
    # get current time
    datetime_object = datetime.datetime.now()
    time = datetime_object.strftime("%I:%M %p")

    # return time
    return time


# main function
def main():

    # set defaults for variable scope
    task = ""
    user_choice = ""
    task_number = 0

    # welcome message
    print("\nWelcome to the \033[1;36mFirebase To-Do Task Manager\033[00m.\n")
    
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
            
            # if user choice is valid, break out of loop
            if(user_choice == "1" or 
            user_choice == "2" or 
            user_choice == "3" or
            user_choice == "4" or
            user_choice == "5"):
                break
            
            # if user_choice is not good, inform user and loop again
            else:
                print("\nInvalid input. Please select 1, 2, 3, 4, or 5.\n")

        #set database root and create dictionary with database data
        root = db.reference("/")
        tasks = root.get()

        # act on user choice
        # add a task to the to do list
        if (user_choice == "1"):
            add_task(tasks)

        # delete a task from the to do list
        elif (user_choice == "2"):
            
            # verify there are tasks to be deleted
            if tasks == None:
                print("\n\033[1;31mYou have no tasks to delete.\033[00m\n")
                continue

            # list tasks in database
            view_tasks(tasks)

            # loop until a valid user choice is made selecting a task to delete
            while True:
                user_choice = input(
                    "Which task number do you wish to delete? ")
                
                # make sure the choice can be cast to integer
                if user_choice.isdigit():

                    # cast to integer and subtract one to match actual element
                    task_number = int(user_choice) - 1

                    # verify the input falls within the dictionary length
                    # if so, call the delete task function and break loop
                    if task_number >= 0 and task_number < len(tasks):
                        delete_task(task_number, tasks)
                        break 

                # otherwise, alert user to invalid input and loop again               
                print("Invalid selection, input a valid task number.")

        # view all tasks
        elif (user_choice == "3"):
            
            # if database has data, call view tasks function using the
            # tasks dictionary holding the database data as an argument
            if tasks != None:
                view_tasks(tasks)
            
            # otherwise alert user and loop again
            else:
                print("\n\033[1;31mYou have no tasks to view.\033[00m\n")

        # update a task
        elif (user_choice == "4"):
            
            # verify the database holds a task to update
            if tasks == None:
                print("\n\033[1;31mYou have no tasks to update!\033[00m\n")
                continue

            # loop until user select a valid task to update
            while True:

                # prompt user for which task to update
                view_tasks(tasks)
                user_choice = input(
                    "Which task number do you wish to update? ")
                
                # make sure the choice can be cast to integer
                if user_choice.isdigit():

                    # cast to integer and subtract one to match actual element
                    task_number = int(user_choice) - 1

                    # verify the input falls within the dictionary length
                    # if so, call the update task function and break loop
                    if task_number >= 0 and task_number < len(tasks):
                        update_task(task_number, tasks)
                        break 

                # otherwise, alert user to invalid input and loop again               
                print("\nInvalid selection, input a valid task number.\n")

        # quit Firebase To-Do Task Manager
        elif (user_choice == "5"):
            print("\nGoodbye. Thanks for using ", end="")
            print("\033[1;36mFirebase To-Do Task Manager\033[00m!\n")
            return 0


# if run directly, call main function, otherwise do nothing
if(__name__ == "__main__"):
    main()