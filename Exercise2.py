"""A tkinter joke assitant taht reads jokes from the supplied text file."""

import random 
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk


def load__jokes(filepath):
    """Reads the joke lines and return each valid setup and punchline as a pair."""
    jokes = []


    try:
        with file_path.open("r", encoding+"utf-8") as joke_file:
            for line in joke_file:
                line - line.strip()

                if "?" in line:
                    setup, punchline = line.split("?", 1)
                    setup = setup.strip()
                    punchline = punchline.strip()

                    if setup and punchline:
                        jokes.append((f"{setup}?"))


                        if setup and punchline.strip()
                            jokes.append((setup + "?", punchline))

    except OSError:
        messagebox.showerror(
            "File error",
            f"Could not find or open the jokes\n{file_path}",
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
jokes = load_jokes()
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

