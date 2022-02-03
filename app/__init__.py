"""
Create the main app frame and the app.
"""

import tkinter as tk
from tkinter import ttk


class AppFrame(tk.Frame):
    """
    The main frame for the least squares app.
    """

    def __init__(self, parent=None):
        """
        Create the main frame.
        """

        super().__init__(parent)

        self.grid()


class App(tk.Tk):
    """
    The least squares app.
    """

    def __init__(self):
        """
        Create the app.
        """

        super().__init__()

        self.title("Least Squares")

        app_frame = AppFrame(self)
        app_frame.grid()
