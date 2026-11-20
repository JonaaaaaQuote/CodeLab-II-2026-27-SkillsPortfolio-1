"""A tkinter joke assistant that reads jokes from the supplied text file."""

import random
import tkinter as tk
from pathlib import Path
from tkinter import messagebox


def load_jokes(filepath):
    """Read valid joke setup and punchline pairs from a text file."""
    jokes = []

    try:
        with filepath.open("r", encoding="utf-8") as joke_file:
            for line in joke_file:
                line = line.strip()

                if "?" in line:
                    setup, punchline = line.split("?", 1)
                    setup = setup.strip() + "?"
                    punchline = punchline.strip()

                    if setup != "?" and punchline:
                        jokes.append((setup, punchline))

    except OSError:
        messagebox.showerror(
            "File error",
            f"Could not find or open the jokes\n{filepath}",
        )

    return jokes

def tell_joke():
    """Chooses a random joke and displays its setup."""
    global current_joke

    if jokes:
        current_joke = random.choice(jokes)
        setup_label.config(text=current_joke[0])
        punchline_label.config(text="")
        punchline_button.config(state="normal")


def show_punchline():
    """Display the punchline for the joke that is currently on screen."""
    if current_joke:
        punchline_label.config(text=current_joke[1])


# Load the jokes and keep track of the joke currently being shown.
jokes_file = (
    Path(__file__).resolve().parent
    / "Assessment 1 - Skills Portfolio"
    / "A1 - Resources"
    / "randomJokes.txt"
)
jokes = load_jokes(jokes_file)
current_joke = None

# Create the main application window.
window = tk.Tk()
window.title("Alexa, Tell Me a Joke")
window.geometry("500x350")
window.minsize(400, 300)

# Add a frame to keep the labels and buttons neatly arranged.
main_frame = tk.Frame(window, padx=20, pady=20)
main_frame.pack(fill="both", expand=True)

title_label = tk.Label(
    main_frame,
    text="Alexa, tell me a joke!",
    font=("Arial", 18, "bold"),
)
title_label.pack(pady=10)

setup_label = tk.Label(
    main_frame,
    text="Click the button to get a joke.",
    font=("Arial", 14),
    wraplength=440,
    justify="center",
)
setup_label.pack(pady=15)

punchline_label = tk.Label(
    main_frame,
    text="",
    font=("Arial", 13, "italic"),
    wraplength=440,
    justify="center",
)
punchline_label.pack(pady=10)   

# Connect each button to the function that handles its action.
tell_button = tk.Button(
    main_frame,
    text="Alexa tell me a Joke",
    command=tell_joke,
)
tell_button.pack(pady=5)

punchline_button = tk.Button(
    main_frame,
    text="Show Punchline",
    command=show_punchline,
    state="disabled",
)
punchline_button.pack(pady=5)

next_button = tk.Button(
    main_frame,
    text="Next Joke",
    command=tell_joke,
)
next_button.pack(pady=5)

quit_button = tk.Button(
    main_frame,
    text="Quit",
    command=window.destroy,
)
quit_button.pack(pady=5)

# Disable joke buttons if the file was empty or could not be loaded.
if not jokes:
    tell_button.config(state="disabled")
    next_button.config(state="disabled")
    setup_label.config(text="No jokes are available. Check the jokes file.")

# Keep the window open and respond to button clicks.
window.mainloop()