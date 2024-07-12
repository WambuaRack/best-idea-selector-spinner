import random
import tkinter as tk
from tkinter import messagebox

ideas = []

def enter_idea():
    idea = idea_entry.get()
    if idea:
        ideas.append(idea)
        idea_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Idea added successfully!")
    else:
        messagebox.showwarning("Warning", "Please enter an idea.")

def spin_for_best():
    if ideas:
        best_idea = random.choice(ideas)
        messagebox.showinfo("Best Idea", f"The best idea is: {best_idea}")
    else:
        messagebox.showwarning("Warning", "No ideas entered yet. Please enter some ideas first.")

# Create the main window
root = tk.Tk()
root.title("Idea Spinner")
root.geometry("400x300")
root.resizable(False, False)

# Create and place the widgets
tk.Label(root, text="Enter your idea:", font=("Helvetica", 14)).pack(pady=10)
idea_entry = tk.Entry(root, width=40, font=("Helvetica", 12))
idea_entry.pack(pady=10)

tk.Button(root, text="Add Idea", command=enter_idea, font=("Helvetica", 12), bg="#4CAF50", fg="white").pack(pady=10)
tk.Button(root, text="Spin for Best Idea", command=spin_for_best, font=("Helvetica", 12), bg="#2196F3", fg="white").pack(pady=10)
tk.Button(root, text="Quit", command=root.quit, font=("Helvetica", 12), bg="#f44336", fg="white").pack(pady=10)

# Run the main event loop
root.mainloop()
