import tkinter as tk
from tkinter import*
from myDB import Database
from tkinter import messagebox

class ToDoApp:
    
    def __init__(self):

        self.dbo = Database()

        self.root = tk.Tk()
        self.root.title('ToDoApp')
        self.root.iconbitmap('noobcraft/P2_To_Do_List/TODO_GUI/assets/app.ico')
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
            messagebox.showinfo('Success', 'Login Successful.')
            self.task_btn()
        else:
            messagebox.showerror('Error', 'Invaild Email/Password')


    def task_btn(self):

        self.clear()

        head = Label(self.root, text='ToDoAPP',bg='#92DCE5',fg="#E30D6D",font=("Arial", 24,'italic'))
        head.pack(pady=30)

        Create_task_btn = Button(self.root, text='Create task', font=('verdana',15), width=15,bg='#EB2B81', command=self.create_task)
        Create_task_btn.pack(pady=(10,10))

        # Edit_task_btn = Button(self.root, text='Edit task', font=('verdana',15), width=15,bg='#EB2B81', command=self.register_gui)
        # Edit_task_btn.pack(pady=(10,10))

        # Delete_task_btn = Button(self.root, text='Delete task', font=('verdana',15), width=15,bg='#EB2B81', command=self.register_gui)
        # Delete_task_btn.pack(pady=(10,10))

        View_task_btn = Button(self.root, text='View task', font=('verdana',15), width=15,bg='#EB2B81', command=self.view_task)
        View_task_btn.pack(pady=(10,10))

        # Marktask_done_btn = Button(self.root, text='Marktask done', font=('verdana',15), width=15,bg='#EB2B81', command=self.register_gui)
        # Marktask_done_btn.pack(pady=(10,10))

        Logout_btn = Button(self.root, text='Logout', font=('verdana',15), width=15,bg='#EB2B81', command=self.login_gui)
        Logout_btn.pack(pady=(10,10))

    def create_task(self):
         
        self.clear()

        head = Label(self.root, text='ToDoAPP',bg='#92DCE5',fg="#E30D6D",font=("Arial", 24,'italic'))
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
            response = self.dbo.add_task(title,priority,description)
            if response:
                messagebox.showinfo('Success', 'Task Created Successfully!')
                self.clear()
                self.task_btn()
            else:
                messagebox.showerror('Error', 'Please Fill all fields.')
            

    def view_task(self):

        self.clear()

        head = Label(self.root, text='ToDoAPP',bg='#92DCE5',fg="#E30D6D",font=("Arial", 24,'italic'))
        head.pack(pady=30)

        tasks = self.dbo.get_tasks()
        for task in tasks:
            task_label = Label(self.root, text=f"{task['title']}: {task['priority']} - {task['description']}", bg='#92DCE5',fg="#E30D6D",font=("Arial", 24,'italic'))
            task_label.pack(pady=(10,10))

        back_btn = Button(self.root, text='Go Back', font=('verdana',15), width=15,bg='#EB2B81', command=self.task_btn)
        back_btn.pack(pady=(10,10))



tda = ToDoApp()
