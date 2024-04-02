class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.todo_list = TodoList()

        self.task_entry = tk.Entry(master, width=40, font=("Helvetica", 12))
        self.task_entry.grid(row=0, column=0, padx=10, pady=(10, 5), columnspan=2)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="ew")

        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=1, column=1, padx=(5, 10), pady=5, sticky="ew")

        self.listbox = tk.Listbox(master, width=60, height=15, font=("Helvetica", 12))
        self.listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

        self.refresh_button = tk.Button(master, text="Refresh", command=self.refresh_tasks)
        self.refresh_button.grid(row=3, column=0, columnspan=2, padx=10, pady=(5, 10), sticky="ew")

        # Configure grid resizing behavior
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)
        master.rowconfigure(2, weight=1)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.add_task(task)
            self.refresh_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_task = self.listbox.curselection()
        if selected_task:
            task_number = int(selected_task[0]) + 1
            if self.todo_list.remove_task(task_number):
                self.refresh_tasks()
            else:
                messagebox.showwarning("Warning", "Task not found.")
        else:
            messagebox.showwarning("Warning", "Please select
