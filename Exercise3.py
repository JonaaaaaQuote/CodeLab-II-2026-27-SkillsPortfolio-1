"""A tkinter app for viewing and managing student marks."""

import tkinter as tk
from tkinter import messagebox, simpledialog


# This is the text file for the studentmarks
FILE_NAME = "studentMarks.txt" 
MAXIMUM_MARK = 160


class StudentManager:
    """Display and manage studen records."""

    def __init__(self,window):
        self.window= window
        self.window.title("Student Manager")
        self.window.geometry("850x570")
        self.view_all_students()

    def load_students(self):
        """Read the student file and store its records in a list."""
        student = []

