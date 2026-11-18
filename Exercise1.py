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

def displayProblem(parent, question_text, answer_callback):
    """Shows the current arithmetic question and prepare the entry box for an answer."""
    question_label.config(text=f"{first_number} {operation} {second_number} = ?")
    answer_entry.delete(0, tk.END)
    answer_entry.focus_set ()

def isCorrectAnswer(user_answer, correct_answer):
    """Compares the submitted answer with the solution and return whether they match"""
    return user_answer == correct_answer

def displayFinalScore(parent, score):
    """Shows the final score and selects a grade and message that matches the results."""
    if score >= 90:
        grade = "A" 
        message = "Excellent job!"
    elif score >= 80:
        grade = "B"
        message = "Good work!"
    elif score >= 70:
        grade = "C"
        message = "You passed!"
    elif score >= 60:
        grade = "D"
        message = "You barely passed!"
    else:
        grade = "F"
        message = "Try again and see if you can improve your score!"

ttk.Label(
    parent,
    text="Quiz Complete!",
    style="Header.TLabel",
).pack(pady=(0, 16))

ttk.Label(
    parent, 
    text=f"Your final score is: {score}/ 100",
    style="Score.TLabel",
).pack(pady = 6)

ttk.Label(
    parent,
    text=f"Your grade is: {grade}",
    style="Score.TLabel",
).pack(pady=4)

ttk.Label(parent, text=message).pack(pady=(4, 16))

class MathsQuiz:
    """Manage the quiz interface, question flow, answer checkingm and score."""

    def __init__(self, root):
        self.root = root
        self.root.title("Maths Quiz")
        self.root.geometry("400x300")

        self.style = ttk.Style()
        self.style.configure("Heading.TLabel", font=("Segoe UI", 18, "bold"))
        self.style.configure("Question.TLabel", font=("Segoe UI", 18, "bold"))
        self.style.configure("Score.TLabel", font=("Segoe UI", 16, "bold"))

        self.main_frame = ttk.Frame(self.root, padding=28)
        self.main_frame.pack(fill="both", expand=True)

        self.score = 0
        self.current_question = 0
        self.attempt_number = 1
        self.difficulty = None
        self.first_number = 0
        self.second_number = 0
        self.operation = "+"
        self.correct_answer = 0

        self.show_menu()

    def clear_screen(self):
        """Remove all the current widgets from the main frame to prepare for the next screen."""
        self.clear_screen
        self.score = 0
        self.clear_screen()
        self.score = 0

        displayMenu(self.main_frame, self.choose_difficulty)

def start_quiz(self):
        """Reset the quiz state and displays the available difficulty levels."""
        self.clear_screen()
        self.score = 0
        self.question_number = 0
        self.question_number = 0
        self.difficulty = None

        displayMenu(self.main_frame, self.start_quiz)

def start_quiz(self, difficulty):
        """Resets the quiz state and displays the available difficulty levels."""
        self.difficulty = difficulty
        self.score = 0
        self.current_question = 0
        self.show_question()

def show_question(self):
        """Creates the question and display it on the screen, along with an entry box for the answer."""
        self.clear_screen()

        self.question_label = ttk.Label(
             self.main_frame,
             style="Question.TLabel"
        )
        self.question_label.pack(pady=(24, 20))


        self.question_label = ttk.Label(self.main_frame)
        self.score_label.pack(pady=4)

        self.intrustion_label = ttk.Label(
             self.main_frame,
             text="Enter your answer below and press Enter to submit.",
        )
        self.intruction_label.pack(pady=(16, 8))

        self.answer_entry = ttk.Entry(
             self.main_frame,
             font=("Segoe UI", 14),
             justify="center",
             width=14,
        )
        self.answer_entry.pack(pady=6)
        self.answer_entry.bind("<Return>", self.submit_answer)


        self.submit_button = ttk.Button(
             self.main_frame,
             text="Submit answer"
             comman=self.submit_answer,
        )
        







