import tkinter as tk
from tkinter import messagebox
import json
import os

FILENAME = "todo_list_gui.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_tasks():
    with open(FILENAME, "w") as f:
        json.dump(tasks, f)

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔️ " if task["done"] else "❌ "
        listbox.insert(tk.END, status + task["task"])

def add_task():
    task_text = entry.get().strip()
    if task_text:
        tasks.append({"task": task_text, "done": False})
        entry.delete(0, tk.END)
        update_listbox()
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty.")

def mark_done():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["done"] = True
        update_listbox()
        save_tasks()
    else:
        messagebox.showinfo("Info", "Please select a task to mark as done.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        update_listbox()
        save_tasks()
    else:
        messagebox.showinfo("Info", "Please select a task to delete.")

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10, padx=10, fill=tk.X)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

tk.Button(button_frame, text="Add Task", width=12, command=add_task).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Mark Done", width=12, command=mark_done).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete Task", width=12, command=delete_task).grid(row=0, column=2, padx=5)

listbox = tk.Listbox(root, font=("Arial", 12))
listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

tasks = load_tasks()
update_listbox()

root.mainloop()
