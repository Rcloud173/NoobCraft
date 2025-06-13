class ToDoListApp:

    def __init__(self):
        self.database = {}  # {email: [name, password]}
        self.tasks = []     # list of task dicts
        self.current_user = None
        self.main_menu()

    def main_menu(self):
        while True:
            choice = input("""
Hello, how can I help you? Press:
    1. Login
    2. Register  
    3. Exit
> """)
            if choice == '1':
                self.login()
            elif choice == '2':
                self.register()
            elif choice == '3':
                print("Exiting application. Goodbye!")
                break
            else:
                print("Invalid input. Please try again.")

    def user_menu(self):
        while True:
            choice = input(f"""
Welcome, {self.database[self.current_user][0]}! Press:
    1. Create a new task
    2. Edit a task
    3. Delete a task
    4. View all tasks
    5. Mark task as done
    6. Logout
> """)
            if choice == '1':
                self.create_new_task()
            elif choice == '2':
                self.edit_task()
            elif choice == '3':
                self.delete_task()
            elif choice == '4':
                self.view_tasks()
            elif choice == '5':
                self.mark_task_done()
            elif choice == '6':
                print("Logging out.")
                self.current_user = None
                break
            else:
                print("Invalid option, please try again.")

    def register(self):
        email = input("Enter your email: ")
        if email in self.database:
            print("Email already registered.")
            return
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        self.database[email] = [name, password]
        print("Registration successful!")

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if email in self.database and self.database[email][1] == password:
            print("Login successful.")
            self.current_user = email
            self.user_menu()
        else:
            print("Invalid email or password.")

    def create_new_task(self):
        print("\n--- Create New Task ---")
        title = input("Enter task title (required): ").strip()
        while not title:
            title = input("Task title cannot be empty. Enter task title: ").strip()

        priority = input("Enter priority (low/medium/high): ").strip().lower()
        description = input("Enter task description (optional): ").strip()

        for task in self.tasks:
            if task["title"].lower() == title.lower() and task["user"] == self.current_user:
                print("Task with this title already exists!")
                return

        task = {
            "title": title,
            "priority": priority,
            "description": description,
            "done": False,
            "user": self.current_user
        }
        self.tasks.append(task)
        print("Task created successfully!")

    def edit_task(self):
        user_tasks = [task for task in self.tasks if task['user'] == self.current_user]

        if not user_tasks:
            print("You have no tasks to edit")
            return
        
        print("Your tasks: ")
        for idx, task in enumerate(user_tasks,1):
            status = "✔" if task["done"] else  "✘"
            print(f"{idx}. {task['title']} ({task['priority']}) - {task['description']} [{status}]")

            try:
                choice = int (input("enter task number to edit: "))
                if choice < 1 or choice > len(user_tasks):
                    print("Invaild choice.")
                    return
                task = user_tasks[choice - 1]
                print("Leave field empty to keep the current value. ")
                new_title = input(f"New title ({task['title']}): ").strip().lower()
                new_priority = input(f"New priority ({task['priority']}): ").strip().lower()
                new_description = input(f"New description ({task['description']}): ").strip().lower()

                if new_title:
                    task["title"] = new_title
                if new_priority:
                    task["priority"] = new_priority
                if new_description:
                    task["description"] = new_description

                print("Task updated.")
            except ValueError:
                print("Invalild input. Please enter a number.")
 

    def delete_task(self):
        user_tasks = [task for task in self.tasks if task['user'] == self.current_user]

        if not user_tasks:
            print("You have no tasks to delete.")
            return
        
        for idx, task in enumerate(user_tasks, 1):
            print(f"{idx}. {task['title']}")

        try:
            choice = int(input("Enter task number to delete: "))
            if 1 < choice <= len(user_tasks):
                task_to_delete = user_tasks[choice - 1]
                self.tasks.remove(task_to_delete)
                print("Task deleted")
            else:
                print("Invalid number")
        except ValueError:
            print("Please enter a valid number. ")

    def view_tasks(self):
        user_tasks = [task for task in self.tasks if task['user'] == self.current_user]

        if not user_tasks:
            print("No task to display.")
            return
        
        print("\n--- Your Tasks ---")
        for idx, task in enumerate(user_tasks,1):
            status = "✔ Done" if task["done"] else "✘ Not Done"
            print(f"{idx}. {task['title']} | Priority: {task['priority']} | Description: {task['description']} | Status: {status} ")
        

    def mark_task_done(self):
        user_tasks = [task for task in self.tasks if task['user'] == self.current_user]

        if not user_tasks:
            print("No pending tasks to mark as done.")
            return
        
        for idx, task in enumerate(user_tasks,1):
            print(f"{idx}. {task['title']} - {task['description']} ")

        try:
            choice = int(input("Enter the task nubmer to mark as done: "))
            if 1 <= choice <= len(user_tasks):
                user_tasks[choice - 1]["done"] = True
                print("Task marked as done.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. please enter a nubmer.")


tdl = ToDoListApp()
