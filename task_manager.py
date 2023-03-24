# =====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import datetime
import time

# ====Login Section====
login_file = open("user.txt", "r+")

login_dictionary = {}

for line in login_file.readlines():
    login_dictionary[line.split(",")[0].strip()] = line.split(",")[1].strip()

while True:
    username_input = input("Enter username:").lower()
    password = login_dictionary.get(username_input)
    if login_dictionary.get(username_input) is None:
        print("Error! Wrong username!")
    else:
        break

while True:
    password_input = input("Enter password(remember about case-sensitivity):")
    if password == password_input:
        print("Logged In! Welcome!")
        login_file.close()
        break
    else:
        print("Error! Wrong password!")

while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.

    if username_input == "admin":
        menu = input('''You're logged in as an Admin
Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
s - display statistics
e - Exit
: ''').lower()
    elif username_input != "admin":
        menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r':  # registering a new user, only allowed to be used by the admin user
        pass
        login_file = open("user.txt", "a")
        new_username = input("Enter a new username you would like to register:")
        login_file.write("\n" + new_username + ", ")
        while True:
            new_password = input("Enter the password you would like to use for this user:")
            password_confirmation = input("Please re-enter the password:")
            if new_password == password_confirmation:
                login_file.write(new_password)
                print("Thank you for registering a new user!")
                login_file.close()
                break
            else:
                print("The passwords don't match, try again!")

    elif menu == 'a':  # adding new task
        pass
        today = str(datetime.today().strftime("%d %b %Y"))
        task_file = open("tasks.txt", "a")
        user_choice = input("Which user would you like to assign the task to?")
        task_file.write("\n" + user_choice + ", ")
        task_title = input("Enter the title of the task:")
        task_file.write(task_title + ", ")
        task_description = input("Describe the task:")
        task_file.write(task_description + ", ")
        task_due_date = input("Enter the due date for the task:")
        task_file.write(today + ", " + task_due_date + ", " + "No")
        print("Thank you for adding a new task to the task board!")
        task_file.close()

    elif menu == 'va':  # displaying all tasks
        pass
        task_file = open("tasks.txt", "r+")
        lines = task_file.readlines()

        for line in lines:  # splitting all the data in the txt document to later display it clearly in the terminal
            user = line.split(",")[0]
            task_name = line.split(",")[1]
            task_disc = line.split(",")[2]
            date_today = line.split(",")[3]
            date_due = line.split(",")[4]
            finished_status = line.split(",")[5]
            print(f'''
Task name: {task_name}
Assigned to: {user}
Date assigned: {date_today}
Due date: {date_due}
Task complete?: {finished_status}
Task description: {task_disc}
            ''')

    elif menu == 'vm':  # displaying tasks only for the user that is logged in
        pass
        task_file = open("tasks.txt", "r+")
        lines = task_file.readlines()

        for line in lines:  # splitting all the data in the txt document to later display it clearly in the terminal
            user = line.split(",")[0]
            if user == username_input:
                for line2 in lines:
                    user = line.split(",")[0]
                    task_name = line.split(",")[1]
                    task_disc = line.split(",")[2]
                    date_today = line.split(",")[3]
                    date_due = line.split(",")[4]
                    finished_status = line.split(",")[5]
                    print(f'''
Task name: {task_name}
Assigned to: {user}
Date assigned: {date_today}
Due date: {date_due}
Task complete?: {finished_status}
Task description: {task_disc}
                                ''')
                    break
            else:
                continue
        task_file.close()

    elif menu == 's':  # new menu option that allows the admin to check the statistics such as the number of user and
        # tasks, only allowed to be used by the admin user
        pass
        total_tasks = 0
        total_users = 0
        task_file = open("tasks.txt", "r")
        login_file = open("user.txt", "r")
        for line in task_file.readlines():
            total_tasks += 1
        for line in login_file.readlines():
            total_users += 1
        print(f'''
Total users registered:{total_users}
Total tasks assigned:{total_tasks}
''')
        task_file.close()
        login_file.close()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
