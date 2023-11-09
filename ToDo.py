import tkinter as tk

root = tk.Tk()
root.title("To-Do List")
task_list = tk.Listbox(root , width = 50 , bg="lightgray")
task_list.pack()

task_entry = tk.Entry(root , width= 50 , bg= "lightgray")
task_entry.pack()
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
def remove_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.delete(selected_task_index)
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
add_button.pack()
remove_button.pack()
root.geometry("400x400")
root.configure(bg= "black")
root.mainloop()
