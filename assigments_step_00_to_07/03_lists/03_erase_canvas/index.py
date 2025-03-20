import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser"""
    eraser_x, eraser_y = canvas.coords(eraser)[:2]  # Get eraser position

    # Check overlapping objects
    overlapping_objects = canvas.find_overlapping(
        eraser_x, eraser_y, eraser_x + ERASER_SIZE, eraser_y + ERASER_SIZE
    )

    # Turn overlapping objects white
    for obj in overlapping_objects:
        if obj != eraser:
            canvas.itemconfig(obj, fill='white')

def on_mouse_move(event):
    """Move the eraser with the mouse and erase objects"""
    canvas.coords(eraser, event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
    erase_objects(canvas, eraser)

# Create Tkinter Window
root = tk.Tk()
root.title("Grid Eraser")

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

# Create Grid
for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):
        canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill='blue')

# Create Eraser
eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill='pink')

# Bind Mouse Movement to Eraser
canvas.bind('<Motion>', on_mouse_move)

# Start the application
root.mainloop()
