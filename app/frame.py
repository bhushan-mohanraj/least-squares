"""
The main application frame.
"""

import tkinter as tk
from tkinter import ttk

import app.constants


class AppFrame(ttk.Frame):
    """
    The main frame for the least squares app.
    """

    import app.settings

    def __init__(self, master, **kwargs):
        """
        Create the main frame.
        """

        super().__init__(master, **kwargs)

        settings_frame = app.settings.SettingsFrame(self)

        settings_frame.grid(
            row=0,
            column=0,
            padx=app.constants.PADDING_X,
            pady=app.constants.PADDING_Y,
            sticky=tk.NSEW,
        )

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
