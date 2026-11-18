"""A 10 question arithmethic quiz with three difficulty levels"""

import random
import tkinter as tk
from tkinter import ttk


QUESTION_COUNT = 10
POINTS_FIRST_ATTEMPT = 10
POINTS_SECOND_ATTEMPT = 5

#Each difficulty maps to the inlcusive minimum and maximum used when generating number.
DIFFICULTY_RANGES = {
    "Easy": (0, 9),
    "Medium": (10, 99),
    "Hard": (1000, 999),
}

def randomInt(difficulty):
    """Return a randomly generated number from the selected difficulty level"""
    minimum, maximum = DIFFICULTY_RANGES[difficulty]
    return random.randint(minimum, maximum)

def decideOperation():
    """Randomly choose and return either the addition or subtraction symbol."""
    return random.choice(["+", "-"])

def displayMenu(parent,choose_difficulty_):
    """Build the difficulty menu and connect each button to its selection callback."""
    ttk.Label(
        parent,
        text="Choose your difficulty",
        style="Header.TLabel",
    ).pack(pady=(0, 16))

    descriptions = {
        "Easy": "Single-digit numbers",
        "Medium": "Two-digit numbers",
        "Hard": "Four-digit numbers",
    }

    for difficulty, description in descriptions.items():
        ttk.Button(
            parent
            text=f"{difficulty} ({description})",
            command=lambda d=difficulty: choose_difficulty_(d)  
        ).pack(fill="x", pady=5)

def displayQuestion(parent, question_text, answer_callback):
    """Shows the current arithmetic question and prepare the entry box for an answer."""
    question_label.config(text=f"{first_number} {operation} {second_number} = ?")
    answer_entry.delete(0, tk.END)
    answer_entry.focus_set ()


Def is correctAnswer(user_answer, correct_answer):
    """Shows the final score and selects a grade and message that matches the results."""



