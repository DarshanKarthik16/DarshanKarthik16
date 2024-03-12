import tkinter as tk
from tkinter import simpledialog, messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        
        self.contacts = []
        
        self.create_widgets()
    
    def create_widgets(self):
        # Contact Listbox
        self.contact_listbox = tk.Listbox(self.root, width=40, height=15)
        self.contact_listbox.grid(row=0, column=0, padx=10, pady=10)
        
        # Add Contact Button
        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        
        # Delete Contact Button
        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        
        # Exit Button
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        self.exit_button.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
        
    def add_contact(self):
        name = tk.simpledialog.askstring("Add Contact", "Enter Name:")
        if name:
            self.contacts.append(name)
            self.update_contact_list()
        else:
            messagebox.showinfo("Add Contact", "Invalid name. Please enter a valid name.")
    
    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            try:
                del self.contacts[index]
                self.update_contact_list()
            except IndexError:
                messagebox.showinfo("Delete Contact", "No contact selected.")
        else:
            messagebox.showinfo("Delete Contact", "Please select a contact to delete.")
    
    def update_contact_list(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, contact)

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
