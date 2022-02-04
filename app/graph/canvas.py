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

    # Variables require that some root window exists.
    import app.variables

    def __init__(self, master, **kwargs):
        """
        Create the graph canvas.
        """

        super().__init__(master, **kwargs)

        # Set the background color to white,
        # since the canvas is a classic Tkinter widget.
        self["background"] = "white"

        self.bind("<Configure>", self.draw)

        app.variables.approximation_m.trace(
            "w",
            self.draw_approximation_line,
        )

        app.variables.approximation_b.trace(
            "w",
            self.draw_approximation_line,
        )

    def draw(self, event):
        """
        Draw the canvas elements when the canvas loads
        or whenever the user resizes the canvas window
        (which corresponds to the "Configure" event).
        """

        # The coordinate system of the Tkinter canvas
        # has its origin at the top-left corner.

        self.draw_axes()
        self.draw_approximation_line()

    def convert_coordinates(self, x, y):
        """
        Convert from the displayed coordinate system
        to the Tkinter canvas coordinate system.
        """

        width = self.winfo_width()
        height = self.winfo_height()

        # Move the x and y coordinates into the system
        # with the same scale as the displayed system
        # but with its origin at the bottom-left corner,
        # since the axes display the ranges from -5 to 10
        # in the horizontal and vertical directions.
        x += 5
        y += 5

        # Since the positive vertical direction is downward
        # for the actual canvas coordinate system,
        # the y coordinate must be flipped.
        y = 15 - y

        # Scale the coordinates as needed.
        x = x / 15 * width
        y = y / 15 * height

        return x, y

    def draw_axes(self):
        """
        Draw the axes to display the ranges from -5 to 10
        in the horizontal and vertical directions.
        """

        # Delete the old axes if they exist.
        self.delete(getattr(self, "x_axis_id", None))
        self.delete(getattr(self, "y_axis_id", None))

        # Draw the new axes and store their IDs.
        self.x_axis_id = self.create_line(
            *self.convert_coordinates(-5, 0),
            *self.convert_coordinates(10, 0),
        )

        self.y_axis_id = self.create_line(
            *self.convert_coordinates(0, -5),
            *self.convert_coordinates(0, 10),
        )

    def draw_approximation_line(self, *args):
        """
        Draw the approximation line from the slope and intercept.
        """

        # Delete the old approximation line if it exists.
        self.delete(getattr(self, "approximation_line_id", None))

        # Draw the new approximation line and store its ID.
        m = app.variables.approximation_m.get()
        b = app.variables.approximation_b.get()

        self.approximation_line_id = self.create_line(
            *self.convert_coordinates(-5, -5 * m + b),
            *self.convert_coordinates(10, 10 * m + b),
        )
