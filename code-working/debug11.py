import tkinter as tk
import math
import random


class ShapeDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("Geometric Shape Drawer")

        # Canvas to draw shapes
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.pack()

        # Instructions for the user
        self.instructions = tk.Label(self.root, text="Use W, A, S, D, Q, E, Z, C to draw the shape")
        self.instructions.pack()

        # Variables to track position and points
        self.x, self.y = 200, 200  # Start at the center of the canvas
        self.points = [(self.x / 10, self.y / 10)]  # Store points to calculate the area (in units, not pixels)

        # Random target area between 5 and 50 square units
        self.target_area = random.randint(5, 50)
        self.target_label = tk.Label(self.root, text=f"Target Area: {self.target_area} sq. units")
        self.target_label.pack()

        # Bind keys to movement
        self.root.bind("<KeyPress>", self.draw_line)

    def draw_line(self, event):
        # Directions where each keystroke moves 1 unit (1 unit = 10 pixels on the canvas)
        direction = {
            'w': (0, -1),  # Move up
            's': (0, 1),  # Move down
            'd': (1, 0),  # Move right
            'a': (-1, 0),  # Move left
            'e': (1, -1),  # Move top-right
            'q': (-1, -1),  # Move top-left
            'z': (-1, 1),  # Move bottom-left
            'c': (1, 1)   # Move bottom-right
        }

        # Get direction from key pressed
        if event.char.lower() in direction:
            dx, dy = direction[event.char.lower()]
            new_x = self.x + dx * 10  # Move by 10 pixels for visual clarity
            new_y = self.y + dy * 10

            # Draw line on the canvas (10 pixels per keystroke)
            self.canvas.create_line(self.x, self.y, new_x, new_y, fill="black")

            # Update the current position (in geometric units, not pixels)
            self.x, self.y = new_x, new_y
            self.points.append((self.x / 10, self.y / 10))  # Store points in geometric units

            # Check if the shape is closed (if the new point is near the starting point)
            if len(self.points) > 3 and self.is_shape_closed():
                self.calculate_area()

    def is_shape_closed(self):
        """ Check if the current shape is closed by comparing the last point with the first point. """
        first_point = self.points[0]
        last_point = self.points[-1]
        # Check if the distance between the first and last points is within a small tolerance
        distance = math.sqrt((first_point[0] - last_point[0]) ** 2 + (first_point[1] - last_point[1]) ** 2)
        return distance < 1  # Tolerance of 1 geometric unit

    def calculate_area(self):
        # Calculate the area of the closed polygon using the Shoelace formula
        n = len(self.points)
        area = 0
        for i in range(n):
            x1, y1 = self.points[i]
            x2, y2 = self.points[(i + 1) % n]
            area += (x1 * y2) - (x2 * y1)
        area = abs(area) / 2.0  # Area in geometric units

        # Show the calculated area
        result_label = tk.Label(self.root, text=f"Calculated Area: {area:.2f} sq. units")
        result_label.pack()

        # Fill the shape with color based on area correctness
        fill_color = "green" if abs(area - self.target_area) < 0.1 else "red"
        self.canvas.create_polygon([p[0] * 10 for p in self.points], [p[1] * 10 for p in self.points], fill=fill_color, outline="black")

        # Disable further drawing after closing the shape
        self.root.unbind("<KeyPress>")

# Set up the GUI window
root = tk.Tk()
app = ShapeDrawer(root)
root.mainloop()