# Creating a basic tkinter window
import tkinter as tk


def create_labeled_entry(parent, label_text, width=30):
    label = tk.Label(parent, text=label_text)
    label.pack(anchor="w")
    entry = tk.Entry(parent, width=width)
    entry.pack(fill="x", pady=(0, 10))
    return entry


# Create the main window
root = tk.Tk()
root.title("Mad Libs Game")
root.geometry("550x600")

# Scrollable form container so all fields stay accessible.
container = tk.Frame(root)
container.pack(fill="both", expand=True)

canvas = tk.Canvas(container)
scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
form_frame = tk.Frame(canvas)

form_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all")),
)

canvas.create_window((0, 0), window=form_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

title_label = tk.Label(form_frame, text="Welcome to the Mad Libs Game!", font=("Helvetica", 16, "bold"))
title_label.pack(pady=(20, 15))

name_entry = create_labeled_entry(form_frame, "Enter a name:")
place_entry = create_labeled_entry(form_frame, "Enter a place:")
adjective_entry = create_labeled_entry(form_frame, "Enter an adjective:")
noun_entry = create_labeled_entry(form_frame, "Enter a noun:")
animal_entry = create_labeled_entry(form_frame, "Enter any animal:")
silly_phrase_entry = create_labeled_entry(form_frame, "Enter a silly phrase:", width=60)
verb_past_tense_entry = create_labeled_entry(form_frame, "Enter a past tense verb:")
verb_entry = create_labeled_entry(form_frame, "Enter a verb:")
plural_noun_entry = create_labeled_entry(form_frame, "Enter a plural noun:")
ridiculous_title_entry = create_labeled_entry(form_frame, "Enter a ridiculous title:")
food_entry = create_labeled_entry(form_frame, "Enter a food:")


def generate_story():
    fields = {
        "name": name_entry.get() or "____",
        "place": place_entry.get() or "____",
        "adjective": adjective_entry.get() or "____",
        "noun": noun_entry.get() or "____",
        "plural_noun": plural_noun_entry.get() or "____",
        "animal": animal_entry.get() or "____",
        "silly_phrase": silly_phrase_entry.get() or "____",
        "verb_past_tense": verb_past_tense_entry.get() or "____",
        "verb": verb_entry.get() or "____",
        "food": food_entry.get() or "____",
        "ridiculous_title": ridiculous_title_entry.get() or "____",
    }

    story_template = """One day, a {adjective} explorer named {name} set out to find the legendary {noun} of Doom.
Armed with a {adjective} backpack and a {noun}, they traveled through the {adjective} forest where giant {plural_noun} roamed freely.
Suddenly, a {adjective} {animal} jumped out and shouted, "{silly_phrase}!"
Without hesitation, the explorer {verb_past_tense} over a fallen {noun} and raced toward a mysterious {place}.
Inside, they discovered a glowing {noun} that could {verb} anything it touched. Curious, they used it on a {food}, which instantly transformed into {plural_noun}.
The explorer laughed so hard they {verb_past_tense}, then carefully packed the treasure and returned home to {verb} with their friends.
And from that day on, everyone called them "{ridiculous_title}."
The End.
"""
    story_label.config(text=story_template.format_map(fields))


generate_button = tk.Button(form_frame, text="Generate Story", command=generate_story)
generate_button.pack(pady=10)

story_label = tk.Label(form_frame, text="", wraplength=500, justify="left", font=("Helvetica", 12))
story_label.pack(padx=15, pady=(10, 20), fill="x")

# Start the main event loop
root.mainloop()
