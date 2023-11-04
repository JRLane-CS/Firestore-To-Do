# Firestore To-Do Task Manager
## Overview
This is a cloud-based to-do task manager developed using Firebase and Python. It allows for full creation, deletion, updating, and viewing of tasks the user wishes to work on. It permits monitoring of the online database for unexpected changes.

## Description
The Firestore To-Do Task Manager is a program which tracks tasks input by the user. The tasks are stored in a Firebase realtime database and can be accessed from anywhere so long as the user can connect to the internet. Options which are supported include CRUD actions where the tasks can be created, viewed, updated, or deleted as the user desires. Additionally, it will contact the Firebase database every ten seconds and alert the user if the database contents change outside the program. This simulates multiple users accessing and making alterations to the database in realtime. The tasks themselves are stored in the database along with the date and time they were created or updated.

### Startup
The program begins by displaying a welcome message and a menu in the console window. The menu options include add a task, delete a task, view tasks, update a task, and quit the application. The user is prompted to select one of the options. Error handling is applied, preventing the user from selecting anything other than the displayed options and an error message is shown should the user attempt to do otherwise.

### Add a Task
When add a task is selected, the program then prompts the user for the task to be completed. Once input, the application displays the new task and asks the user to verify it. If he or she inputs 'y' the task is saved in the database. If not, a message is displayed telling the user the add a task function is exiting and they are being returned to the menu.

### Delete a Task
When delete a task is chosen, the program lists the tasks stored and prompts the user to select which task number is to be deleted. Error handling is applied, preventing the user from attempting to delete a non-existent task. If the database holds no tasks, an error message alerts the user that there are no tasks to delete.

### View Tasks
When view tasks is selected as an option, all tasks in the database are printed in the console window. Each task has a red header with an associated number. The task is shown in yellow with the creation/updated date and time also in yellow.
Should a user attempt to view tasks when the database is empty, an error message is shown telling the user there are no tasks to view.

### Update a Task
When update a task is chosen, the program lists all the tasks in the database and prompts the user to select the one to update. Once the selection has been made, the program asks the user to verify it is the correct task. Inputting a 'y' will begin the update process and anything else will cause a message letting the user know they are going back to the menu screen. The update process continues by asking the user to input the updated task. Once this is done, the user is again asked to verify that the old task is being updated with the new, with both being displayed onscreen. Once more, anything other than a 'y' input will exit back to the menu. I the user affirms the update, the old task will be replaced with the new in the database, along with the updated date and time. Should the user attempt to select this option when the database is empty, an error message alerts him or her that there is nothing in the database to update.

### Quit Firebase To-Do Task Manager
Selecting this option will cause a goodbye and thank you message to be displayed and the application will exit.

## Purpose
The reason I developed this application was to familiarize myself with the operation of the Cloud-based Firebase realtime database. In particular, I wanted to learn how to access it using the Python programming language. Learning how to work with Firebase was enlightening. 

A side benefit of this project was the opportunity to learn more about how to use pseudo-threading in Python. It was fun experiementing with this capability so that I could have two parts of the program running simultaneously. This permits the application to monitor the online database in realtime for unexpected changes.

## Video Demo
Here's a walkthrough of the application's code and demonstration of the application as it runs:

[Firebase To-Do Task Manager Demo Video](https://youtu.be/kVBbEdTDXJg)

# Cloud Database
For this application, I used the Firebase realtime database. It is a NoSQL type of database which stores its data in a json-like format using nodes, rather than tables like one would see in a typical relational database.

The structure of the database is quite simple. Each task is stored in the database at the root level. When viewing the json-like structure of the database, the raw data looks something like this:

{'Task 1': ['Take out the trash.', 'November 04, 2023', '02:39 AM'], 'Task 2': ['Mow the lawn.', 'November 04, 2023', '02:39 AM'], 'Task 3': ['Pay the bills.', 'November 04, 2023', '02:39 AM']}

To break this down, first in the structure is the key of each task; in this case, Task 1, Task 2, and Task 3. Following this is the task description, the date it was created or updated, and the time of day the creation or update was done as the values of each key.

# Development Environment
My development environment was Microsoft's Visual Studio Code. The programming language is Python with the firebase_admin module installed to allow for the program to interface with the Firebase realtime database.

# Useful Websites
During my research and early coding on this project, I found the following materials helpful:

- [How to Connect Your Python Application to Firebase Realtime Database](https://www.youtube.com/watch?v=BnrkTpgH5Vc&t=5s)
- [Firebase Cloud Firestore + Python FULL COURSE [NoSQL, Admin SDK, CRUD with Python]](https://www.youtube.com/watch?v=N0j6Fe2vAK4)
- [Python Threading Explained in 8 Minutes](https://www.youtube.com/watch?v=A_Z1lgZLSNc)
- [Thread Pools in Python - Asynchronous Programming](https://www.youtube.com/watch?v=2Koubj0fF9U)
- [NoSQL Tutorial](https://www.guru99.com/nosql-tutorial.html)

# Future Work
While the Firebase To-Do Task Manager is functional, I have plans at some point to make it better. For instance, I would like to: 

- Make the menu look a little more appealing by adding some color and formatting
- Do something with the placement of the monitor's alert so it doesn't mess up the menu selection
- Ultimately, to create a GUI so that the database monitor thread doesn't affect the menu selection as it does in the console
