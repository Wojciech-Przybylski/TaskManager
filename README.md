# Task Manager App
This project is a task manager program written in Python. The program allows users to log in to their account, add tasks, view tasks assigned to them, and view tasks assigned to all users. The program also provides an option for administrators to register new users and view program statistics.

The program reads user data from a text file named "user.txt" and task data from a text file named "tasks.txt". The program uses the datetime and time libraries in Python to handle dates and times.

The program starts with a login section, where users enter their username and password. The program then presents a menu of options based on the user's role - regular user or administrator. Regular users can add tasks, view their tasks, view all tasks, or exit the program. Administrators have additional options, including registering new users and viewing program statistics.

If the user selects the "add task" option, the program prompts them to enter information about the new task, including the user to whom the task should be assigned, the task title, description, and due date. The program then writes this information to the "tasks.txt" file.

If the user selects the "view all tasks" option, the program reads all the task information from the "tasks.txt" file and displays it in a clear format. If the user selects the "view my tasks" option, the program reads the task information from the "tasks.txt" file and displays only the tasks assigned to the current user.

If the user selects the "statistics" option, the program reads the data from both the "user.txt" and "tasks.txt" files and displays the number of registered users and the number of tasks assigned in the program.

The program allows the user to perform multiple tasks before logging out or exiting the program.
