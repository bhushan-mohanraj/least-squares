# Least Squares

A demonstration of the method of least squares.

# Development

## Notes

- Certain Python imports are made within classes
because Tkinter requires that operations like creating variables
only occur after some `tk.Tk` window has been declared.

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
