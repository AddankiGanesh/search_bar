import mysql.connector
import tkinter as tk
from tkinter import ttk

class RollNumberSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Roll Number Search")

        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.update_suggestions)

        self.create_widgets()

    def create_widgets(self):
        search_label = tk.Label(self.root, text="Search Roll Number:")
        search_label.pack(pady=10)

        self.search_entry = ttk.Entry(self.root, textvariable=self.search_var)
        self.search_entry.pack(pady=5)

        self.suggestion_listbox = tk.Listbox(self.root)
        self.suggestion_listbox.pack(pady=5)

    def update_suggestions(self, *args):
        search_text = self.search_var.get()

        # Fetch suggestions from the database
        suggestions = self.fetch_suggestions(search_text)

        # Clear the current suggestions in the listbox
        self.suggestion_listbox.delete(0, tk.END)

        # Insert new suggestions
        for suggestion in suggestions:
            self.suggestion_listbox.insert(tk.END, suggestion)

    def fetch_suggestions(self, query):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ganesh@123",
            database="college"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT roll_number FROM students WHERE roll_number LIKE %s", ('%' + query + '%',))
        suggestions = [row[0] for row in cursor.fetchall()]
        conn.close()
        return suggestions

if __name__ == "__main__":
    root = tk.Tk()
    app = RollNumberSearchApp(root)
    root.mainloop()
