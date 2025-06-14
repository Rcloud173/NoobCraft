import tkinter as tk
from tkinter import*
from myDB import Database
from tkinter import messagebox

class ToDoApp:
    
    def __init__(self):

        self.dbo = Database()
        self.current_user = None

        self.root = tk.Tk()
        self.root.title('ToDoApp')
        # self.root.iconbitmap('noobcraft/P2_To_Do_List/TODO_GUI/assets/app.ico')
        self.root.config(bg='#92DCE5')
        self.root.geometry('600x600')

        self.login_gui()
        self.root.mainloop()


    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def login_gui(self):

        self.clear()

        head = Label(self.root, text='ToDoAPP',bg='#92DCE5',fg="#E30D6D",font=("Arial", 24,'italic'))
        head.pack(pady=30)

        label1 = Label(self.root, text="Enter your email: ", bg="#92DCE5", font=(15))
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(10,10), ipady=4)

        label2 = Label(self.root, text='Enter Password: ', bg="#92DCE5", font=(15))
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50,show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_btn = Button(self.root, text='Login', font=('verdana',15), width=10,bg='#EB2B81', command=self.login_logic)
        login_btn.pack(pady=(10,10))


        label3 = Label(self.root, text='Not a member?', bg="#92DCE5", font=(15))
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Register Now!', font=('verdana',15), width=15,bg='#EB2B81', command=self.register_gui)
        redirect_btn.pack(pady=(10,10))


    def register_gui(self):
        
        self.clear()

        head = Label(self.root, text='ToDoAPP',bg='#92DCE5',fg="#E30D6D",font=("Arial", 24,'italic'))
        head.pack(pady=30)


        label0 = Label(self.root, text="Enter your Name: ", bg="#92DCE5", font=(15))
        label0.pack(pady=(10,10))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(10,10), ipady=4)

        label1 = Label(self.root, text="Enter your email: ", bg="#92DCE5", font=(15))
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(10,10), ipady=4)

        label2 = Label(self.root, text='Enter Password: ', bg="#92DCE5", font=(15))
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50,show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text='Register', font=('verdana',15), width=10,bg='#EB2B81', command=self.registraion_logic)
        register_btn.pack(pady=(10,10))


        label3 = Label(self.root, text='Already a member? Login', bg="#92DCE5", font=(15))
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Login Now!', font=('verdana',15), width=10,bg='#EB2B81', command=self.login_gui)
        redirect_btn.pack(pady=(10,10))

    
    def registraion_logic(self):
        
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_user_data(name,email,password)

        if response:
            messagebox.showinfo('Success', 'Registration Successful. You can login now')
        else:
            messagebox.showerror('Error', 'Email already exists')



    def login_logic(self):
        
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.login_search(email,password)

        if response:
            self.current_user = email
            messagebox.showinfo('Success', 'Login Successful.')
            self.task_btn()
        else:
            messagebox.showerror('Error', 'Invaild Email/Password')


    def task_btn(self):

        self.clear()

        head = Label(self.root, text='ToDoAPP - Main Menu',bg='#92DCE5',fg="#E30D6D",font=("Arial", 24,'italic'))
        head.pack(pady=30)

        Create_task_btn = Button(self.root, text='Create task', font=('verdana',15), width=15,bg='#EB2B81', command=self.create_task)
        Create_task_btn.pack(pady=(10,10))

        View_task_btn = Button(self.root, text='View task', font=('verdana',15), width=15,bg='#EB2B81', command=self.view_task)
        View_task_btn.pack(pady=(10,10))

        Logout_btn = Button(self.root, text='Logout', font=('verdana',15), width=15,bg='#EB2B81', command=self.login_gui)
        Logout_btn.pack(pady=(10,10))

    def create_task(self):
         
        self.clear()

        head = Label(self.root, text='ToDoAPP - Create Task',bg='#92DCE5',fg="#E30D6D",font=("Arial", 24,'italic'))
        head.pack(pady=30)

        label1 = Label(self.root, text="Enter your title: ", bg="#92DCE5", font=(15))
        label1.pack(pady=(10,10))

        self.title_input = Entry(self.root, width=50)
        self.title_input.pack(pady=(10,10), ipady=4)

        label2 = Label(self.root, text='Enter Priority (high/medimum/low): ', bg="#92DCE5", font=(15))
        label2.pack(pady=(10, 10))

        self.priority_input = Entry(self.root, width=50)
        self.priority_input.pack(pady=(5, 10), ipady=4)

        label3 = Label(self.root, text='Enter Description: ', bg="#92DCE5", font=(15))
        label3.pack(pady=(10, 10))

        self.description_input = Entry(self.root, width=50)
        self.description_input.pack(pady=(5, 10), ipady=10)

        submit_btn = Button(self.root, text='SUBMIT', font=('verdana',15), width=15,bg='#EB2B81', command=self.submit_task)
        submit_btn.pack(pady=(10,10))


        back_btn = Button(self.root, text='Go Back', font=('verdana',15), width=15,bg='#EB2B81', command=self.task_btn)
        back_btn.pack(pady=(10,10))


    def submit_task(self):
        title = self.title_input.get()
        priority = self.priority_input.get()
        description = self.description_input.get()

        if title and priority and description:
            response = self.dbo.add_task(self.current_user,title,priority,description)
            if response:
                messagebox.showinfo('Success', 'Task Created Successfully!')
                self.clear()
                self.task_btn()
            else:
                messagebox.showerror('Error', 'Please Fill all fields.')
            

    def view_task(self):
        self.clear()

        head = Label(self.root, text='ToDoAPP - Your Tasks',bg='#92DCE5',fg="#E30D6D",font=("Arial", 24,'italic'))
        head.pack(pady=30)

        tasks = self.dbo.get_tasks(self.current_user)
        self.task_list = tasks  # Store for reference in edit

        for index, task in enumerate(tasks):
            task_label = Label(
                self.root,
                text=f"{index+1}. {task['title']} - {task['priority']} - {task['description']}",
                bg='#92DCE5', fg="#000000", font=("Arial", 12))
            task_label.pack(pady=(5,5))

        self.selected_index_input = Entry(self.root, width=10)
        self.selected_index_input.pack(pady=(10,10))
        self.selected_index_input.insert(0, "Task No.")

        edit_btn = Button(self.root, text='Edit task', font=('verdana',15), width=15,bg='#EB2B81', command=self.edit_taks)
        edit_btn.pack(pady=(5,5))

        delete_btn = Button(self.root, text='Delete task', font=('verdana',15), width=15,bg='#EB2B81', command=self.delete_task)
        delete_btn.pack(pady=(5,5))

        mark_done_btn = Button(self.root, text='Mark as Done', font=('verdana',15), width=15,bg='#EB2B81', command=self.mark_task_done)
        mark_done_btn.pack(pady=(5,5))

        back_btn = Button(self.root, text='Go Back', font=('verdana',15), width=15,bg='#EB2B81', command=self.task_btn)
        back_btn.pack(pady=(10,10))



    def edit_taks(self):
        try:
            index = int(self.selected_index_input.get()) - 1
            task = self.task_list[index]
        except (ValueError, IndexError):
            messagebox.showerror('Error', 'Invalid task number')
            return

        self.clear()

        head = Label(self.root, text='ToDoAPP - Edit Task',bg='#92DCE5',fg="#E30D6D",font=("Arial", 24,'italic'))
        head.pack(pady=30)

        Label(self.root, text="New Title:", bg="#92DCE5").pack()
        self.title_input = Entry(self.root, width=50)
        self.title_input.insert(0, task['title'])
        self.title_input.pack()

        Label(self.root, text="New Priority:", bg="#92DCE5").pack()
        self.priority_input = Entry(self.root, width=50)
        self.priority_input.insert(0, task['priority'])
        self.priority_input.pack()

        Label(self.root, text="New Description:", bg="#92DCE5").pack()
        self.description_input = Entry(self.root, width=50)
        self.description_input.insert(0, task['description'])
        self.description_input.pack(ipady=10)

        update_btn = Button(self.root, text='Update', font=('verdana',15), width=15, bg='#EB2B81',
                            command=lambda: self.edit_logic(index))
        update_btn.pack(pady=(10,10))

        back_btn = Button(self.root, text='Go Back', font=('verdana',15), width=15,bg='#EB2B81', command=self.task_btn)
        back_btn.pack(pady=(10,10))

    
    def edit_logic(self, task_index):
        title = self.title_input.get()
        priority = self.priority_input.get()
        description = self.description_input.get()

        if title and priority and description:
            response = self.dbo.update_task(self.current_user, task_index, title, priority, description)
            if response:
                messagebox.showinfo('Success', 'Task updated successfully!')
                self.view_task()
            else:
                messagebox.showerror('Error', 'Failed to update task.')
        else:
            messagebox.showerror('Error', 'Please fill all fields.')

    
    def delete_task(self):
        try:
            index = int(self.selected_index_input.get()) - 1
            confirm = messagebox.askyesno('Confirm Delete', 'Are you sure you want to delete this task?')
            if not confirm:
                return
            response = self.dbo.delete_task(self.current_user, index)
            if response:
                messagebox.showinfo('Success', 'Task deleted.')
                self.view_task()
            else:
                messagebox.showerror('Error', 'Invalid task number.')
        except ValueError:
            messagebox.showerror('Error', 'Please enter a valid task number.')

    def mark_task_done(self):
        try:
            index = int(self.selected_index_input.get()) - 1
            response = self.dbo.mark_task_done(self.current_user, index)
            if response:
                messagebox.showinfo('Success', 'Task marked as done.')
                self.view_task()
            else:
                messagebox.showerror('Error', 'Invalid task number.')
        except ValueError:
            messagebox.showerror('Error', 'Please enter a valid task number.')





tda = ToDoApp()
