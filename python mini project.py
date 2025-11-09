import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_all():
    confirm = messagebox.askyesno("Clear All", "Are you sure you want to clear all tasks?")
    if confirm:
        listbox_tasks.delete(0, tk.END)

def mark_completed():
    try:
        selected = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected)

        # Check if already marked
        if task.startswith("✔ "):
            messagebox.showinfo("Info", "Task already marked as completed!")
        else:
            listbox_tasks.delete(selected)
            listbox_tasks.insert(selected, "✔ " + task)
            listbox_tasks.itemconfig(selected, fg="#00FF00")  # green text
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed!")

# --------------------------- UI DESIGN ---------------------------

root = tk.Tk()
root.title("To-Do List")
root.geometry("420x500")
root.resizable(False, False)
root.config(bg="#121212")

title = tk.Label(
    root,
    text="📝 To-Do List",
    font=("Helvetica", 22, "bold"),
    bg="#121212",
    fg="#00FFAA"
)
title.pack(pady=15)

frame_task = tk.Frame(root, bg="#121212")
frame_task.pack(pady=10)

entry_task = tk.Entry(
    frame_task,
    width=26,
    font=("Helvetica", 14),
    bg="#1E1E1E",
    fg="#FFFFFF",
    insertbackground="#00FFAA",
    borderwidth=2,
    relief="solid"
)
entry_task.grid(row=0, column=0, padx=10)

add_button = tk.Button(
    frame_task,
    text="Add Task",
    font=("Helvetica", 12, "bold"),
    bg="#00BFA5",
    fg="white",
    width=10,
    activebackground="#00FFAA",
    command=add_task
)
add_button.grid(row=0, column=1)

listbox_tasks = tk.Listbox(
    root,
    width=40,
    height=15,
    font=("Helvetica", 13),
    selectbackground="#00FFAA",
    selectforeground="#000000",
    bg="#1E1E1E",
    fg="#FFFFFF",
    borderwidth=0,
    highlightthickness=0
)
listbox_tasks.pack(pady=15)

frame_buttons = tk.Frame(root, bg="#121212")
frame_buttons.pack(pady=10)

delete_button = tk.Button(
    frame_buttons,
    text="Delete Task",
    font=("Helvetica", 12, "bold"),
    bg="#E53935",
    fg="white",
    width=12,
    activebackground="#EF5350",
    command=delete_task
)
delete_button.grid(row=0, column=0, padx=5)

complete_button = tk.Button(
    frame_buttons,
    text="Mark Completed",
    font=("Helvetica", 12, "bold"),
    bg="#43A047",
    fg="white",
    width=14,
    activebackground="#66BB6A",
    command=mark_completed
)
complete_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(
    frame_buttons,
    text="Clear All",
    font=("Helvetica", 12, "bold"),
    bg="#757575",
    fg="white",
    width=12,
    activebackground="#BDBDBD",
    command=clear_all
)
clear_button.grid(row=0, column=2, padx=5)

footer = tk.Label(
    root,
    text="Dark Mode • Tkinter To-Do App",
    font=("Helvetica", 10),
    bg="#121212",
    fg="#777"
)
footer.pack(pady=10)

root.mainloop()
