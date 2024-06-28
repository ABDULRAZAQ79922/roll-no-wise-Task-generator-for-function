import tkinter as tk
from tkinter import messagebox

class TaskGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Roll Number-wise Task Generator")
        self.root.geometry("400x300")
        
        self.tasks = {}
        
        self.lbl_title = tk.Label(root, text="Task Generator", font=("Helvetica", 16))
        self.lbl_title.pack(pady=10)
        
        self.lbl_roll_number = tk.Label(root, text="Enter Roll Number:")
        self.lbl_roll_number.pack()
        
        self.entry_roll_number = tk.Entry(root)
        self.entry_roll_number.pack()
        
        self.lbl_task = tk.Label(root, text="Enter Task:")
        self.lbl_task.pack()
        
        self.entry_task = tk.Entry(root)
        self.entry_task.pack()
        
        self.btn_add_task = tk.Button(root, text="Add Task", command=self.add_task)
        self.btn_add_task.pack(pady=5)
        
        self.btn_show_tasks = tk.Button(root, text="Show All Tasks", command=self.show_tasks)
        self.btn_show_tasks.pack(pady=5)
        
    def add_task(self):
        roll_number = self.entry_roll_number.get()
        task = self.entry_task.get()
        
        if roll_number and task:
            if roll_number not in self.tasks:
                self.tasks[roll_number] = []
            self.tasks[roll_number].append(task)
            messagebox.showinfo("Success", f"Task added for Roll Number {roll_number}")
            self.entry_roll_number.delete(0, tk.END)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "enter both Roll Number and Task.")
        
    def show_tasks(self):
        all_tasks = ""
        for roll_number, tasks in self.tasks.items():
            all_tasks += f"Roll Number {roll_number}:\n"
            for task in tasks:
                all_tasks += f"  - {task}\n"
        if all_tasks:
            messagebox.showinfo("All Tasks", all_tasks)
        else:
            messagebox.showinfo("No Tasks", "No tasks have been added yet.")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskGeneratorApp(root)
    root.mainloop()
