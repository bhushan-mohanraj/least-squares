"""
Create the main app frame and the app.
"""

import tkinter as tk
from tkinter import ttk

import app.constants


root = tk.Tk()

root.title("Least Squares")
root.minsize(720, 540)
root.grid_columnconfigure(0, weight=1)

style = ttk.Style(root)

style.configure("TLabel", font=("Helvetica", 18))
style.configure("Heading.TLabel", font=("Helvetica", 36, "bold"))

style.configure("TCheckbutton", font=("Helvetica", 18))


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


app_frame = AppFrame(root)
app_frame.grid(sticky=tk.NSEW)
