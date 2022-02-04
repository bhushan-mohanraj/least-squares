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

    # A helper variable for incrementing the row number,
    # which equals -1 since it increases before each access
    # and the first row number must be 0.
    _row_number = -1

    # Variables require that some root window exists.
    import app.variables

    def __init__(self, master, **kwargs):
        """
        Create the settings frame.
        """

        super().__init__(master, **kwargs)

        label = ttk.Label(
            self,
            text="Settings",
            style="Heading.TLabel",
        )

        label.grid(
            row=self.row_number,
            column=0,
            padx=app.constants.PADDING_X,
            pady=app.constants.PADDING_Y,
            sticky=tk.W,
        )

        self.approximation_m_label = ttk.Label(
            self,
            text="Slope: " + str(round(app.variables.approximation_m.get(), 2)),
        )

        app.variables.approximation_m.trace(
            "w",
            self.set_approximation_m_label,
        )

        self.approximation_m_label.grid(
            row=self.row_number,
            column=0,
            padx=app.constants.PADDING_X,
            pady=app.constants.PADDING_Y,
            sticky=tk.W,
        )

        approximation_m_scale = ttk.Scale(
            self,
            orient=tk.HORIZONTAL,
            variable=app.variables.approximation_m,
            from_=0.0,
            to=5.0,
        )

        approximation_m_scale.grid(
            row=self.row_number,
            column=0,
            padx=app.constants.PADDING_X,
            pady=(0, app.constants.PADDING_Y),
            sticky=tk.EW,
        )

        self.approximation_b_label = ttk.Label(
            self,
            text="Intercept: " + str(round(app.variables.approximation_b.get(), 2)),
        )

        app.variables.approximation_b.trace(
            "w",
            self.set_approximation_b_label,
        )

        self.approximation_b_label.grid(
            row=self.row_number,
            column=0,
            padx=app.constants.PADDING_X,
            pady=app.constants.PADDING_Y,
            sticky=tk.W,
        )

        approximation_b_scale = ttk.Scale(
            self,
            orient=tk.HORIZONTAL,
            variable=app.variables.approximation_b,
            from_=0.0,
            to=5.0,
        )

        approximation_b_scale.grid(
            row=self.row_number,
            column=0,
            padx=app.constants.PADDING_X,
            pady=(0, app.constants.PADDING_Y),
            sticky=tk.EW,
        )

        display_residual_squares_check = ttk.Checkbutton(
            self,
            text="Display Residual Squares",
            variable=app.variables.display_residual_squares,
        )

        display_residual_squares_check.grid(
            row=self.row_number,
            column=0,
            padx=app.constants.PADDING_X,
            pady=app.constants.PADDING_Y,
            sticky=tk.W,
        )

        display_optimal_line_check = ttk.Checkbutton(
            self,
            text="Display Optimal Line",
            variable=app.variables.display_optimal_line,
        )

        display_optimal_line_check.grid(
            row=self.row_number,
            column=0,
            padx=app.constants.PADDING_X,
            pady=app.constants.PADDING_Y,
            sticky=tk.W,
        )

        self.grid_columnconfigure(0, weight=1)

    @property
    def row_number(self):
        """
        Increment and return the current row number.
        """

        self._row_number += 1

        return self._row_number

    def set_approximation_m_label(self, *args):
        """
        Set the label for the slope label.
        """

        self.approximation_m_label.config(
            text="Slope: " + str(round(app.variables.approximation_m.get(), 2)),
        )

    def set_approximation_b_label(self, *args):
        """
        Set the label for the intercept label.
        """

        self.approximation_b_label.config(
            text="Intercept: " + str(round(app.variables.approximation_b.get(), 2)),
        )
