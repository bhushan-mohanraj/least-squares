# Least Squares

A demonstration of the method of least squares.

# Development

## Notes

- Certain Python imports are made within classes
because Tkinter requires that operations like creating variables
occur only after some `tk.Tk` window has been initialized.

### To Do

- Fix `pylint` warnings.
- Fix the arrows (cut off) in the graph.
- Fix the colors (too bold) in the graph.
- Allow the user to drag points around,
and calculate the optimal slope and intercept
with NumPy or similar libraries.

## Environment (Python 3.10)

### macOS

```
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

## Before Commit

```
python -m pylint app
python -m black app
```
