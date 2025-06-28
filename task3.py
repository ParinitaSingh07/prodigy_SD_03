import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

CONTACTS_FILE = "contacts.json"

# Load and save
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# GUI Functions
def refresh_listbox():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        display = f"{contact['name']} | {contact['phone']} | {contact['email']}"
        contact_listbox.insert(tk.END, display)

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name and phone and email:
        contacts.append({"name": name, "phone": phone, "email": email})
        save_contacts(contacts)
        refresh_listbox()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

def delete_contact():
    selected = contact_listbox.curselection()
    if selected:
        index = selected[0]
        del contacts[index]
        save_contacts(contacts)
        refresh_listbox()
    else:
        messagebox.showinfo("Select Contact", "Please select a contact to delete.")

def edit_contact():
    selected = contact_listbox.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]
        new_name = simpledialog.askstring("Edit Name", "Enter new name:", initialvalue=contact['name'])
        new_phone = simpledialog.askstring("Edit Phone", "Enter new phone:", initialvalue=contact['phone'])
        new_email = simpledialog.askstring("Edit Email", "Enter new email:", initialvalue=contact['email'])

        if new_name and new_phone and new_email:
            contacts[index] = {"name": new_name, "phone": new_phone, "email": new_email}
            save_contacts(contacts)
            refresh_listbox()
    else:
        messagebox.showinfo("Select Contact", "Please select a contact to edit.")

# Main window
root = tk.Tk()
root.title("Contact Manager")
root.geometry("500x400")
root.configure(bg="#E3A1A1")


contacts = load_contacts()

# Labels + Entries
tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Phone:").grid(row=1, column=0, padx=5, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, padx=5, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).grid(row=3, column=0, pady=10)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=3, column=1, pady=10)
tk.Button(root, text="Edit Contact", command=edit_contact).grid(row=3, column=2, pady=10)

# Listbox
contact_listbox = tk.Listbox(root, width=70)
contact_listbox.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

refresh_listbox()
root.mainloop()
