# Creating a basic tkinter window
import tkinter as tk
# Create the main window
root = tk.Tk()
root.title("Mad Libs Game")
root.geometry("500x500")

title_label = tk.Label(root, text="Welcome to the Mad Libs Game!", font=("Helvetica", 16, "bold"))
title_label.pack(pady=20)

# Create a label and entry for a name in the story
name_label = tk.Label(root, text="Enter a name:")
name_label.pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack()

# Create a label and entry for a place in the story
place_label = tk.Label(root, text="Enter a place:")
place_label.pack()
place_entry = tk.Entry(root, width=30)
place_entry.pack()

# Create a label and entry for an adjective in the story
adjective_label = tk.Label(root, text="Enter an adjective:")
adjective_label.pack()
adjective_entry = tk.Entry(root, width=30)
adjective_entry.pack()

# Create a label and entry for a noun in the story
noun_label = tk.Label(root, text="Enter a noun:")
noun_label.pack()
noun_entry = tk.Entry(root, width=30)
noun_entry.pack()
# Start the main event loop
root.mainloop()                           
