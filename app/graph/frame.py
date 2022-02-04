"""
The graph frame for the application.
"""

import tkinter as tk
from tkinter import ttk

import app.constants
import app.graph.canvas


class GraphFrame(ttk.Frame):
    """
    The graph frame.
    """

    # Variables require that some root window exists.
    import app.variables

    def __init__(self, master, **kwargs):
        """
        Create the graph frame.
        """

        super().__init__(master, **kwargs)

        label = ttk.Label(
            self,
            text="Graph",
            style="Heading.TLabel",
        )

        label.grid(
            row=0,
            column=0,
            padx=app.constants.PADDING_X,
            pady=app.constants.PADDING_Y,
            sticky=tk.W,
        )

        canvas = app.graph.canvas.GraphCanvas(self)

        canvas.grid(
            row=1,
            column=0,
            padx=app.constants.PADDING_X,
            pady=app.constants.PADDING_Y,
            sticky=tk.EW + tk.S,
        )

        self.grid_columnconfigure(0, weight=1)
