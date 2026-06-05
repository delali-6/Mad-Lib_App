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

# Create a button to generate the story
def generate_story():
    name = name_entry.get()
    place = place_entry.get()
    adjective = adjective_entry.get()
    noun = noun_entry.get()

    story = f"""One day, a {adjective} explorer named {name} set out to find the legendary {noun} of Doom.
Armed with a {adjective} backpack and a {noun}, they traveled through the {adjective} forest where giant (plural noun) __________ roamed freely.
Suddenly, a {adjective} {animal} jumped out and shouted, "{silly_phrase}!"
Without hesitation, the explorer {verb_past_tense} over a fallen {noun} and raced toward a mysterious {place}.
Inside, they discovered a glowing {noun} that could {verb} anything it touched. Curious, they used it on a {food}, which instantly transformed into {plural_noun}.
The explorer laughed so hard they {verb_past_tense} __________, then carefully packed the treasure and returned home to {verb} __________ with their friends.
And from that day on, everyone called them "{ridiculous_title}."
The End.
"""
    story_label.config(text=story)

    generate_button = tk.Button(root, text="Generate Story", command=generate_story, font=("Helvetica", 14, "bold"))
generate_button.pack(pady=20)
# Start the main event loop
root.mainloop()                           
