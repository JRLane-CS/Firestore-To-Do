# import firebase module with credentials
import firebase_admin
from firebase_admin import db, credentials
import datetime

# initialize firebase admin using private key
key = credentials.Certificate("C:/Users/jerry/OneDrive/Documents/BYU-Idaho/BYU-I Fall 2023/CSE 310/Software Assignments/serviceAccountKey.json")
firebase_admin.initialize_app(key, {"databaseURL": "https://to-do-1c749-default-rtdb.firebaseio.com/"})




# database connected
print("\nDatabase is connected.\n")

# set database reference
pointer = db.reference("/")

# add a task to the database
current = datetime.datetime.now()
task_number = 1
db.reference("/").update({f"Task {task_number}": ["New task details", f"{current}"]})
print(f"Database contents: {pointer.get()}")

# delete a task in the database
db.reference(f"/Task {task_number}").delete()
print(f"Database contents: {pointer.get()}")





# main function
def main():

    # set defaults for variable scope
    task = ""
    user_choice = ""
    task_number = 1

    # welcome message
    print("\nWelcome to Firebase To-Do Task Manager.\n")
    
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
            print("\nInvalid input. Please select 1, 2, or 3.\n")

    # echo user choice
    if (user_choice == "1"):
        print("\nAdding task")
    elif (user_choice == "2"):
        print("\nDeleting task")
    elif (user_choice == "3"):
        print("\nTasks left:")
    elif (user_choice == "4"):
        print("Updating task")
    elif (user_choice == "5"):
        return    
    
    print("Done.")
    

if(__name__ == "__main__"):
    main()