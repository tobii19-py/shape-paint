from canvas import Canvas
from shapes import Rectangle, Square

# Get canvas width and height from the user
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Create a dictionary of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

# Create the canvas using provided data
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:

    r1.draw(canvas)
    s1.draw(canvas)
    canvas.make('canvas.png')