import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class TodoList:
    def __init__(self):
        self.head = None
        self.task_count = 0

    def add_task(self, task):
        self.task_count += 1
        new_node = Node(f"{self.task_count}. {task}")
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_task(self, task_number):
        current = self.head
        prev = None
        while current:
            if current.data.startswith(f"{task_number}."):
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def get_tasks(self):
        tasks = []
        current = self.head
        while current:
            tasks.append(current.data)
            current = current.next
        return tasks

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.todo_list = TodoList()

        self.task_entry = tk.Entry(master, width=40, font=("Helvetica", 12))
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        self.task_entry.bind("<Return>", self.add_task_enter)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.listbox = tk.Listbox(master, width=60, height=15, font=("Helvetica", 12))
        self.listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=2, column=0, padx=10, pady=10)

        self.refresh_button = tk.Button(master, text="Refresh", command=self.refresh_tasks)
        self.refresh_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.add_task(task)
            self.refresh_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def add_task_enter(self, event):
        self.add_task()

    def remove_task(self):
        selected_task = self.listbox.curselection()
        if selected_task:
            task_number = int(selected_task[0]) + 1
            if self.todo_list.remove_task(task_number):
                self.refresh_tasks()
            else:
                messagebox.showwarning("Warning", "Task not found.")
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def refresh_tasks(self):
        self.listbox.delete(0, tk.END)
        tasks = self.todo_list.get_tasks()
        for task in tasks:
            self.listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    root.geometry("500x400")  # Set window size
    todo_app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
