"""
Create the main app frame and the app.
"""

import tkinter as tk
from tkinter import ttk

import app.constants
import app.settings


class AppFrame(ttk.Frame):
    """
    The main frame for the least squares app.
    """

    def __init__(self, master, **kwargs):
        """
        Create the main frame.
        """

        super().__init__(master, **kwargs)

        self.settings_frame = app.settings.SettingsFrame(self)

        self.settings_frame.grid(
            row=0,
            column=0,
            padx=app.constants.PADDING_X,
            pady=app.constants.PADDING_Y,
            sticky=tk.NSEW,
        )

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)


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

        self.app_frame = AppFrame(self)
        self.app_frame.grid(sticky=tk.NSEW)

        self.grid_columnconfigure(0, weight=1)
