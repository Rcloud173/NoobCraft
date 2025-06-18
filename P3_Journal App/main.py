import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import datetime

class JournalApp:
    def __init__(self, root):

        self.current_user = None

        self.root = root
        self.root.title("Simple Journal App")

        self.root.config(bg='#92DCE5')
        self.root.geometry('600x600')

        self.login_gui()


        # Create UI components
        

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def login_gui(self):
        self.clear()

        head = Label(self.root, text='Simple Journal App',bg="#9DEA4A",fg="#E30D6D",font=("Arial", 24,'italic'))
        head.pack(pady=30)

        label1 = Label(self.root, text="Enter your email: ", bg="#9DEA4A", font=(15))
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(10,10), ipady=4)

        label2 = Label(self.root, text='Enter Password: ', bg="#9DEA4A", font=(15))
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50,show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_btn = Button(self.root, text='Login', font=('verdana',15), width=10,bg='#EB2B81', command=self.main_page)
        login_btn.pack(pady=(10,10))


        label3 = Label(self.root, text='Not a member?', bg="#9DEA4A", font=(15))
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Register Now!', font=('verdana',15), width=15,bg='#EB2B81', command=self.register_gui)
        redirect_btn.pack(pady=(10,10))

    def login_logic(self):
        pass

    def register_gui(self):
         self.clear()

         head = Label(self.root, text='ToDoAPP',bg='#9DEA4A',fg="#E30D6D",font=("Arial", 24,'italic'))
         head.pack(pady=30)


         label0 = Label(self.root, text="Enter your Name: ", bg="#9DEA4A", font=(15))
         label0.pack(pady=(10,10))

         self.name_input = Entry(self.root, width=50)
         self.name_input.pack(pady=(10,10), ipady=4)

         label1 = Label(self.root, text="Enter your email: ", bg="#9DEA4A", font=(15))
         label1.pack(pady=(10,10))

         self.email_input = Entry(self.root, width=50)
         self.email_input.pack(pady=(10,10), ipady=4)

         label2 = Label(self.root, text='Enter Password: ', bg="#9DEA4A", font=(15))
         label2.pack(pady=(10, 10))

         self.password_input = Entry(self.root, width=50,show='*')
         self.password_input.pack(pady=(5, 10), ipady=4)

         register_btn = Button(self.root, text='Register', font=('verdana',15), width=10,bg='#EB2B81', command=self.register_logic)
         register_btn.pack(pady=(10,10))


         label3 = Label(self.root, text='Already a member? Login', bg="#9DEA4A", font=(15))
         label3.pack(pady=(20, 10))

         redirect_btn = Button(self.root, text='Login Now!', font=('verdana',15), width=10,bg='#EB2B81', command=self.login_gui)
         redirect_btn.pack(pady=(10,10))

    def register_logic(self):
        pass

    def main_page(self):

        self.clear()
        
        self.label = tk.Label(root, text="Write your journal entry below:", bg="#9DEA4A", font=(15))
        self.label.pack(pady=10)

        self.text_area = tk.Text(root, height=15, width=60)
        self.text_area.pack(padx=10, pady=10)

        self.save_button = tk.Button(root, text="Save Entry", bg="#9DEA4A")
        self.save_button.pack(pady=(10,10))

        self.clear_button = tk.Button(root, text="Clear", bg="#9DEA4A")
        self.clear_button.pack(pady=(10,10))

        
if __name__ == "__main__":
    root = tk.Tk()
    app = JournalApp(root)
    root.mainloop()