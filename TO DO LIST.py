import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []
        self.username = ""
        self.password = ""

        # Create login GUI components
        self.login_label = tk.Label(root, text="Login")
        self.login_label.pack()

        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(root, width=20)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(root, width=20, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(root, text="Login", command=self.check_login)
        self.login_button.pack()

        self.create_account_button = tk.Button(root, text="Create Account", command=self.create_account)
        self.create_account_button.pack()

        self.task_label = tk.Label(root, text="Enter a task:")
        self.task_label.pack_forget()

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack_forget()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack_forget()

        self.task_listbox = tk.Listbox(root, width=40, height=10)
        self.task_listbox.pack_forget()

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack_forget()

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "arnav" and password == "arnav":
            self.login_label.config(text="Logged in as arnav")
            self.username_label.pack_forget()
            self.username_entry.pack_forget()
            self.password_label.pack_forget()
            self.password_entry.pack_forget()
            self.login_button.pack_forget()
            self.create_account_button.pack_forget()
            self.task_label.pack()
            self.task_entry.pack()
            self.add_button.pack()
            self.task_listbox.pack()
            self.delete_button.pack()
        else:
            messagebox.showinfo("Error", "Invalid username or password")

    def create_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username and password:
            self.username = username
            self.password = password
            self.login_label.config(text="Account created successfully")
            self.username_label.pack_forget()
            self.username_entry.pack_forget()
            self.password_label.pack_forget()
            self.password_entry.pack_forget()
            self.login_button.pack_forget()
            self.create_account_button.pack_forget()
            self.task_label.pack()
            self.task_entry.pack()
            self.add_button.pack()
            self.task_listbox.pack()
            self.delete_button.pack()
        else:
            messagebox.showinfo("Error", "Please enter a username and password")

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(task_index)
            self.tasks.pop(task_index)
        except:
            messagebox.showinfo("Error", "Select a task to delete")

root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()
