import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class JournalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Journal App")

        self.root.config(bg='#92DCE5')
        self.root.geometry('600x600')

        self.login_gui()


        # Create UI components
        # self.label = tk.Label(root, text="Write your journal entry below:")
        # self.label.pack(pady=10)

        # self.text_area = tk.Text(root, height=15, width=60)
        # self.text_area.pack(padx=10, pady=10)

        # self.save_button = tk.Button(root, text="Save Entry")
        # self.save_button.pack(pady=5)

        # self.clear_button = tk.Button(root, text="Clear")
        # self.clear_button.pack(pady=5)

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def login_gui(self):
        pass

    def login_logic(self):
        pass

    def register_gui(self):
        pass

    def register_logic(self):
        pass

        
if __name__ == "__main__":
    root = tk.Tk()
    app = JournalApp(root)
    root.mainloop()