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

        try:
            with open(FILE_NAME, "r", encoding="utf-8") as student_file:
                lines = student_file.readlines()

            # the first line is the record count, so student data starts on the second line.
            for line in lines[1:]:
                line = line.strip()
                if line:
                    student.append(line)

        except FileNotFoundError:
            messagebox.showerror("Error", f"Could not find {FILE_NAME}")
        except (OSError, UnicodeDecodeError) as error:
            messagebox.showerror("Error", f"Could not read {FILE_NAME}: {error}")

        return student

    def save_student(self):
        """Write all student lines back to the file with an updated record count.""" 
        try:
            with open(FILE_NAME, "w", encoding="utf-8") as student_file:
                student_file.write(f:"{len(self.students)}\n")

        except OSError as error:
            messagebox.showerror(
                "Save error",
                f"Could not save {FILE_NAME}:\n{error}",
            )
    def parse_student(self, student_line):
        """Split a saved student line into its separate field."""
        parts = student_line.split(",")

        if len(parts) !=6:
            return None

        try:
            return {
                "code": parts[0].strip(),
                "name": parts[1].strip(),
                "coursework": [
                    int(parts[2]),
                    int(parts[3]),
                    int(parts[4]),
                ]
            }
        except ValueError:
            return None
    
                
