"""
The graph canvas for the application.
"""

import tkinter as tk
from tkinter import ttk

import app.constants


class GraphCanvas(tk.Canvas):
    """
    The graph canvas.
    """

    def __init__(self, master, **kwargs):
        """
        Create the graph canvas.
        """

        super().__init__(master, **kwargs)

        # Set the background color to white,
        # since the canvas is a classic Tkinter widget.
        self["background"] = "white"
