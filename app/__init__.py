"""
Create the main app frame and the app.
"""

import tkinter as tk
from tkinter import ttk


# Create the root window.
root = tk.Tk()

root.title("Least Squares")
root.minsize(720, 540)

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Create styles for different elements.
style = ttk.Style(root)

style.configure("TLabel", font=("Helvetica", 18))
style.configure("Heading.TLabel", font=("Helvetica", 36, "bold"))

style.configure("TCheckbutton", font=("Helvetica", 18))

# Add the main app frame to the root window.
import app.frame

app_frame = app.frame.AppFrame(root)
app_frame.grid(sticky=tk.NSEW)
