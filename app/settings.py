"""
The settings frame for the application.
"""

import tkinter as tk
from tkinter import ttk

import app.constants


class SettingsFrame(ttk.Frame):
    """
    The settings frame.
    """

    def __init__(self, master, **kwargs):
        """
        Create the settings frame.
        """

        super().__init__(master, **kwargs)

        self.label = ttk.Label(
            self,
            text="Settings",
            font=app.constants.LARGE_FONT,
        )

        self.label.grid(
            row=0,
            column=0,
            padx=app.constants.PADDING_X,
            pady=app.constants.PADDING_Y,
            sticky=tk.W,
        )

        self.grid_columnconfigure(0, weight=1)
