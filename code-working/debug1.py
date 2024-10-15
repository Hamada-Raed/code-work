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
  
        # Random target area between 20 and 100 square units  
        self.target_area = random.randint(20, 100)  
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
  
        # Adjust area calculation: each keystroke counted as 10 units instead of 1  
        area *= 10  
  
        # Show the calculated area  
        result_label = tk.Label(self.root, text=f"Calculated Area: {area:.2f} sq. units")  
        result_label.pack()  
  
        # Disable further drawing after closing the shape  
        self.root.unbind("<KeyPress>")  
  
# Set up the GUI window  
root = tk.Tk()  
app = ShapeDrawer(root)  
root.mainloop() 


import tkinter as tk
import math
import random

class ShapeDrawer:
    def __init__(self, root):
        """Initialize the ShapeDrawer with the main application window."""
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
        self.points = [(self.x, self.y)]  # Store points in pixels

        # Random target area between 20 and 100 square units (even numbers only)
        self.target_area = random.choice([i for i in range(20, 101) if i % 2 == 0])  # Generate a random even number
        self.target_label = tk.Label(self.root, text=f"Target Area: {self.target_area} sq. units")
        self.target_label.pack()

        # Bind keys to movement
        self.root.bind("<KeyPress>", self.draw_line)

    def draw_line(self, event):
        """Draw a line on the canvas based on key press events.

        The movement direction is determined by the key pressed:
        W, A, S, D for cardinal directions and Q, E, Z, C for diagonals.
        If the shape is closed, the area is calculated.
        """
        # Directions where each keystroke moves 1 unit (1 unit = 10 pixels on the canvas)
        direction = {
            'w': (0, -10),  # Move up
            's': (0, 10),  # Move down
            'd': (10, 0),  # Move right
            'a': (-10, 0),  # Move left
            'e': (10, -10),  # Move top-right
            'q': (-10, -10),  # Move top-left
            'z': (-10, 10),  # Move bottom-left
            'c': (10, 10)   # Move bottom-right
        }

        # Get direction from key pressed
        if event.char.lower() in direction:
            dx, dy = direction[event.char.lower()]
            new_x = self.x + dx
            new_y = self.y + dy

            # Draw line on the canvas (10 pixels per keystroke)
            self.canvas.create_line(self.x, self.y, new_x, new_y, fill="black")

            # Update the current position (in pixels)
            self.x, self.y = new_x, new_y
            self.points.append((self.x, self.y))  # Store points in pixels

            # Check if the shape is closed (if the new point is near the starting point)
            if len(self.points) > 3 and self.is_shape_closed():
                self.calculate_area()

    def is_shape_closed(self):
        """Check if the current shape is closed by comparing the last point with the first point.

        Returns:
            bool: True if the shape is closed (last point is close to the first point),
                  False otherwise.
        """
        first_point = self.points[0]
        last_point = self.points[-1]
        # Check if the distance between the first and last points is within a small tolerance
        distance = math.sqrt((first_point[0] - last_point[0]) ** 2 + (first_point[1] - last_point[1]) ** 2)
        return distance < 10  # Tolerance of 10 pixels

    def calculate_area(self):
        """Calculate the area of the closed polygon using the Shoelace formula.

        Displays the calculated area and colors the shape based on the correctness
        of the area compared to the target area. If the calculated area is within 
        a tolerance of the target area, the shape is filled with green; otherwise, 
        it is filled with red. Disables further drawing after closing the shape.
        """
        # Calculate the area of the closed polygon using the Shoelace formula
        n = len(self.points)
        area = 0
        for i in range(n):
            x1, y1 = self.points[i]
            x2, y2 = self.points[(i + 1) % n]
            area += (x1 * y2) - (x2 * y1)
        area = abs(area) / 2.0  # Area in square pixels
        area /= 100  # Convert to square units (1 unit = 10 pixels)

        # Show the calculated area
        result_label = tk.Label(self.root, text=f"Calculated Area: {area:.2f} sq. units")
        result_label.pack()

        # Color the shape based on whether the area is correct
        if abs(area - self.target_area) < 0.1:
            self.canvas.create_polygon(self.points, fill="green")
        else:
            self.canvas.create_polygon(self.points, fill="red")

        # Disable further drawing after closing the shape
        self.root.unbind("<KeyPress>")

# Set up the GUI window
root = tk.Tk()
app = ShapeDrawer(root)
root.mainloop() 