"""
The graph canvas for the application.
"""

import tkinter as tk
from tkinter import ttk

import app.constants


# The points to plot.
POINTS = [
    (-4, 1),
    (1, -2),
    (2, 7),
    (7, 3),
    (9, 8),
]


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

        # Draw the canvas elements when the canvas loads
        # or whenever the user resizes the canvas window.
        self.bind("<Configure>", self.draw)

        # Redraw the approximation line
        # whenever the user changes the parameters.
        app.variables.approximation_m.trace(
            "w",
            self.draw_approximation_line,
        )

        app.variables.approximation_b.trace(
            "w",
            self.draw_approximation_line,
        )

        # Redraw the residual squares
        # whenever the user changes the parameters.
        app.variables.approximation_m.trace(
            "w",
            self.draw_residual_squares,
        )

        app.variables.approximation_b.trace(
            "w",
            self.draw_residual_squares,
        )

        app.variables.display_residual_squares.trace(
            "w",
            self.draw_residual_squares,
        )

    def draw(self, event):
        """
        Draw the canvas elements.
        """

        self.draw_axes()
        self.draw_approximation_line()
        self.draw_points()
        self.draw_residual_squares()

    def convert_coordinates(self, x, y):
        """
        Convert from the displayed coordinate system
        to the Tkinter canvas coordinate system.
        """

        width = self.winfo_width()
        height = self.winfo_height()

        # Move the x and y coordinates into the system
        # with its origin at the bottom-left corner,
        # since the axes display the ranges from -5 to 10.
        x += 5
        y += 5

        # Since the positive vertical direction is downward
        # in the Tkinter canvas coordinate system,
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
            width=2,
            arrow=tk.BOTH,
        )

        self.y_axis_id = self.create_line(
            *self.convert_coordinates(0, -5),
            *self.convert_coordinates(0, 10),
            width=2,
            arrow=tk.BOTH,
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
            width=2,
            fill="blue",
        )

    def draw_points(self, *args):
        """
        Draw the points to plot.
        """

        # Delete the old points if they exist.
        for point_id in getattr(self, "point_ids", []):
            self.delete(point_id)

        # Draw the new points and store their IDs.
        self.point_ids = []

        for point in POINTS:
            # Determine the center coordinates.
            point_x, point_y = self.convert_coordinates(*point)

            # Draw the point as an oval.
            point_id = self.create_oval(
                point_x - 6,
                point_y - 6,
                point_x + 6,
                point_y + 6,
                fill="red",
                outline="red",
            )

            self.point_ids.append(point_id)

    def draw_residual_squares(self, *args):
        """
        Draw the residual squares if desired
        and calculate and display the sum of squared residuals.
        """

        # Delete the old residual squares if they exist.
        for residual_square_id in getattr(self, "residual_square_ids", []):
            self.delete(residual_square_id)

        # The residual values for the points.
        residuals = []

        # Draw the new residual squares and store their IDs if desired.
        self.residual_square_ids = []

        # The approximation slope and intercept.
        m = app.variables.approximation_m.get()
        b = app.variables.approximation_b.get()

        for point in POINTS:
            point_x, point_y = point

            # Determine the residual.
            residual = (point_x * m + b) - point_y

            residuals.append(residual)

            if app.variables.display_residual_squares.get():
                # Draw the square left of points above the line.
                if residual < 0:
                    residual_square_id = self.create_rectangle(
                        *self.convert_coordinates(
                            point_x + residual,
                            point_y + residual,
                        ),
                        *self.convert_coordinates(
                            point_x,
                            point_y,
                        ),
                        width=2,
                        outline="red",
                    )

                # Draw the square right of points below the line.
                else:
                    residual_square_id = self.create_rectangle(
                        *self.convert_coordinates(
                            point_x,
                            point_y,
                        ),
                        *self.convert_coordinates(
                            point_x + residual,
                            point_y + residual,
                        ),
                        width=2,
                        outline="red",
                    )

                self.residual_square_ids.append(residual_square_id)

        # Calculate and display the sum of squared residuals.
        approximation_area = sum([residual**2 for residual in residuals])

        app.variables.approximation_area.set(approximation_area)
