"""A 10-question arithmetic quiz with three difficulty levels."""

import random
import tkinter as tk
from tkinter import ttk


QUESTION_COUNT = 10
POINTS_FIRST_ATTEMPT = 10
POINTS_SECOND_ATTEMPT = 5

# Inclusive minimum and maximum values for each difficulty level.
DIFFICULTY_RANGES = {
    "Easy": (0, 9),
    "Medium": (10, 99),
    "Moderate": (10, 99),
    "Hard": (1000, 9999),
    "Advanced": (1000, 9999),
}


def randomInt(difficulty):
    """Return a random integer for the selected difficulty level."""
    minimum, maximum = DIFFICULTY_RANGES[difficulty]
    return random.randint(minimum, maximum)


def decideOperation():
    """Randomly return '+' or '-' for an arithmetic problem."""
    return random.choice(["+", "-"])


def displayMenu(parent, choose_difficulty):
    """Display the difficulty menu and connect a callback to each button."""
    for child in parent.winfo_children():
        child.destroy()

    ttk.Label(parent, text="Difficulty Level", style="Header.TLabel").pack(pady=(0, 16))

    descriptions = {
        "Easy": "Single-digit numbers",
        "Medium": "Double-digit numbers",
        "Hard": "Four-digit numbers",
    }

    for difficulty, description in descriptions.items():
        ttk.Button(
            parent,
            text=f"{difficulty} ({description})",
            command=lambda d=difficulty: choose_difficulty(d),
        ).pack(fill="x", pady=5)


def isCorrect(user_answer, correct_answer):
    """Check whether an answer is correct."""
    try:
        return int(user_answer) == int(correct_answer)
    except (TypeError, ValueError):
        return False


# Keep the names used by the original draft available to callers.
def is_correctAnswer(user_answer, correct_answer):
    return isCorrect(user_answer, correct_answer)


def displayResults(parent, score):
    """Display the final score and grade, with options to replay or quit."""
    for child in parent.winfo_children():
        child.destroy()

    if score > 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"

    ttk.Label(parent, text="Quiz Complete", style="Header.TLabel").pack(pady=(0, 12))
    ttk.Label(parent, text=f"Score: {score}/100", style="Score.TLabel").pack(pady=5)
    ttk.Label(parent, text=f"Grade: {grade}", style="Score.TLabel").pack(pady=5)


class ArithmeticQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Arithmetic Quiz")
        self.root.geometry("520x420")
        self.root.resizable(False, False)

        self.style = ttk.Style(root)
        if "clam" in self.style.theme_names():
            self.style.theme_use("clam")
        self.style.configure("Header.TLabel", font=("Segoe UI", 20, "bold"))
        self.style.configure("Score.TLabel", font=("Segoe UI", 16))
        self.style.configure("Question.TLabel", font=("Segoe UI", 24, "bold"))

        self.main = ttk.Frame(root, padding=30)
        self.main.pack(fill="both", expand=True)

        self.difficulty = None
        self.question_number = 0
        self.attempt = 1
        self.score = 0
        self.first_number = 0
        self.second_number = 0
        self.operation = "+"
        self.answer_entry = None

        displayMenu(self.main, self.start_quiz)

    def clear_main(self):
        for child in self.main.winfo_children():
            child.destroy()

    def start_quiz(self, difficulty):
        self.difficulty = difficulty
        self.question_number = 0
        self.score = 0
        self.clear_main()
        self.next_question()

    def next_question(self):
        if self.question_number >= QUESTION_COUNT:
            self.show_results()
            return

        self.question_number += 1
        self.attempt = 1
        self.first_number = randomInt(self.difficulty)
        self.second_number = randomInt(self.difficulty)
        self.operation = decideOperation()
        self.clear_main()

        ttk.Label(
            self.main,
            text=f"Question {self.question_number} of {QUESTION_COUNT}",
        ).pack(pady=(0, 16))
        ttk.Label(
            self.main,
            text=f"{self.first_number} {self.operation} {self.second_number} = ?",
            style="Question.TLabel",
        ).pack(pady=(0, 16))

        self.answer_entry = ttk.Entry(self.main, width=12, justify="center", font=("Segoe UI", 16))
        self.answer_entry.pack(pady=5)
        self.answer_entry.bind("<Return>", lambda event: self.submit_answer())

        self.feedback = ttk.Label(self.main, text="", foreground="#555555")
        self.feedback.pack(pady=12)

        ttk.Button(self.main, text="Submit Answer", command=self.submit_answer).pack(pady=5)
        self.answer_entry.focus_set()

    def submit_answer(self):
        if self.answer_entry is None:
            return

        answer_text = self.answer_entry.get().strip()
        if not answer_text:
            self.feedback.configure(text="Please enter an answer.", foreground="#b00020")
            return

        correct_answer = (
            self.first_number + self.second_number
            if self.operation == "+"
            else self.first_number - self.second_number
        )

        if isCorrect(answer_text, correct_answer):
            if self.attempt == 1:
                self.score += POINTS_FIRST_ATTEMPT
            else:
                self.score += POINTS_SECOND_ATTEMPT
            self.root.after(350, self.next_question)
        else:
            if self.attempt == 1:
                self.attempt = 2
                self.feedback.configure(
                    text="Incorrect. You have one more attempt.",
                    foreground="#b00020",
                )
                self.answer_entry.delete(0, tk.END)
                self.answer_entry.focus_set()
            else:
                self.feedback.configure(
                    text=f"Incorrect. The correct answer was {correct_answer}.",
                    foreground="#b00020",
                )
                self.answer_entry.state(["disabled"])
                self.root.after(900, self.next_question)

    def show_results(self):
        displayResults(self.main, self.score)
        ttk.Button(self.main, text="Play Again", command=lambda: displayMenu(self.main, self.start_quiz)).pack(pady=12)
        ttk.Button(self.main, text="Quit", command=self.root.destroy).pack(pady=5)


def displayProblem(parent, question_text, answer_callback):
    """Compatibility helper that displays a question and submit button."""
    ttk.Label(parent, text=question_text).pack(pady=8)


def displayQuestion(parent, question_text, answer_callback):
    """Compatibility alias for displayProblem."""
    return displayProblem(parent, question_text, answer_callback)


if __name__ == "__main__":
    root = tk.Tk()
    app = ArithmeticQuiz(root)
    root.mainloop()



