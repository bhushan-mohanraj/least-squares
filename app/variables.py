"""
Variables used throughout the app.
"""

import tkinter as tk


# The slope and intercept of the optimal line
# that minimizes the sum of squared residuals.
optimal_m = tk.DoubleVar()
optimal_b = tk.DoubleVar()

# The slope and intercept of the approximation line
# that the user sets through the app settings.
approximation_m = tk.DoubleVar()
approximation_b = tk.DoubleVar()

# The sum of squared residuals for the approximation line.
approximation_area = tk.DoubleVar()

# Display the squares for each residual.
display_squares = tk.BooleanVar()
display_squares.set(tk.FALSE)

# Display the optimal line
# that minimizes the sum of squared residuals.
display_optimal_line = tk.BooleanVar()
display_optimal_line.set(tk.FALSE)