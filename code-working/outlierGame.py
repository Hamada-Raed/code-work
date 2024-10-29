# # Import the necessary library, pygame, which is used for game development
# import pygame

# # Define some color constants
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)

# # Define a class for the balls
# class Ball:
#     # The constructor method for the Ball class
#     def __init__(self, x, y, radius, color):
#         # Initialize the x, y coordinates, radius, and color of the ball
#         self.x = x
#         self.y = y
#         self.radius = radius
#         self.color = color

#     # Method to draw the ball on the screen
#     def draw(self, s):
#         # Use pygame's draw.circle method to draw the ball
#         pygame.draw.circle(s, self.color, (self.x, self.y), self.radius)

#     # Method to check if the ball is clicked
#     def is_clicked(self, pos):
#         # Calculate the distance between the click position and the ball's center
#         distance = ((pos[0] - self.x) ** 2 + (pos[1] - self.y) ** 2) ** 0.5
#         # Return True if the distance is less than or equal to the ball's radius
#         return distance <= self.radius

# # Initialize the pygame library
# pygame.init()

# # Set the screen width and height
# s_w = 800
# s_h = 600
# # Create a screen with the specified width and height
# s = pygame.display.set_mode((s_w, s_h))
# # Set the caption of the screen
# pygame.display.set_caption("Color Chain")

# # Define the ball radius and spacing
# b_r = 20  
# ball_spacing = 5   

# # Initialize an empty list to store the balls
# balls = []
# # Define a list of colors
# colors = [RED, GREEN]

# # Create 20 balls with alternating colors and add them to the list
# for i in range(20):  
#     x = b_r + i * (b_r + ball_spacing)
#     y = s_h // 2
#     color = colors[i % 2]
#     balls.append(Ball(x, y, b_r, color))

# # Initialize variables to keep track of the selected ball and the game state
# selected_ball = None
# running = True
# game_won = False  

# # Main game loop
# while running:
#     # Handle events
#     for event in pygame.event.get():
#         # If the user closes the window, stop the game
#         if event.type == pygame.QUIT:
#             running = False
#         # If the user clicks the mouse and the game is not won
#         if event.type == pygame.MOUSEBUTTONDOWN and not game_won:
#             # Get the mouse position
#             pos = pygame.mouse.get_pos()
#             # Check if any ball is clicked
#             for ball in balls:
#                 if ball.is_clicked(pos):
#                     # If a ball is clicked and no ball is currently selected, select the ball
#                     if selected_ball is None:
#                         selected_ball = ball
#                     # If a ball is clicked and a ball is currently selected, swap the colors of the two balls
#                     else:
#                         temp_color = selected_ball.color
#                         selected_ball.color = ball.color
#                         ball.color = temp_color
#                         selected_ball = None  

#         # Check if the game is won (all balls are green)
#         if all(ball.color == GREEN for ball in balls):
#             game_won = True

#     # Fill the screen with white
#     s.fill(WHITE)

#     # Draw all the balls on the screen
#     for ball in balls:
#         ball.draw(s)

#     # If the game is won, display a congratulatory message
#     if game_won:
#         # Create a font object
#         font = pygame.font.Font(None, 36)  
#         # Render the text
#         text_surface = font.render("Congratulations! You won!", True, BLACK)
#         # Get the rectangle of the text
#         text_rect = text_surface.get_rect(center=(s_w // 2, s_h // 2))
#         # Draw the text on the screen
#         s.blit(text_surface, text_rect)

#     # Update the display
#     pygame.display.flip()

# # Quit the pygame library
# pygame.quit() 

# # Import the necessary library, pygame, which is used for game development
# import pygame

# # Define some color constants
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)

# # Define a class for the balls
# class Ball:
#     # The constructor method for the Ball class
#     def __init__(self, x, y, radius, color):
#         # Initialize the x, y coordinates, radius, and color of the ball
#         self.x = x
#         self.y = y
#         self.radius = radius
#         self.color = color

#     # Method to draw the ball on the screen
#     def draw(self, s):
#         # Use pygame's draw.circle method to draw the ball
#         pygame.draw.circle(s, self.color, (self.x, self.y), self.radius)

#     # Method to check if the ball is clicked
#     def is_clicked(self, pos):
#         # Calculate the distance between the click position and the ball's center
#         distance = ((pos[0] - self.x) ** 2 + (pos[1] - self.y) ** 2) ** 0.5
#         # Return True if the distance is less than or equal to the ball's radius
#         return distance <= self.radius

# # Initialize the pygame library
# pygame.init()

# # Set the screen width and height
# s_w = 800
# s_h = 600
# # Create a screen with the specified width and height
# s = pygame.display.set_mode((s_w, s_h))
# # Set the caption of the screen
# pygame.display.set_caption("Color Chain")

# # Define the ball radius and spacing
# b_r = 20  
# ball_spacing = 5   

# # Initialize an empty list to store the balls
# balls = []
# # Define a list of colors
# colors = [RED, GREEN]

# # Create 20 balls with alternating colors and add them to the list
# for i in range(20):  
#     x = b_r + i * (b_r + ball_spacing)
#     y = s_h // 2
#     color = colors[i % 2]
#     balls.append(Ball(x, y, b_r, color))

# # Initialize variables to keep track of the selected ball and the game state
# selected_ball = None
# running = True
# game_won = False  

# # Main game loop
# while running:
#     # Handle events
#     for event in pygame.event.get():
#         # If the user closes the window, stop the game
#         if event.type == pygame.QUIT:
#             running = False
#         # If the user clicks the mouse and the game is not won
#         if event.type == pygame.MOUSEBUTTONDOWN and not game_won:
#             # Get the mouse position
#             pos = pygame.mouse.get_pos()
#             # Check if any ball is clicked
#             for ball in balls:
#                 if ball.is_clicked(pos):
#                     # If a ball is clicked and no ball is currently selected, select the ball
#                     if selected_ball is None:
#                         selected_ball = ball
#                     # If a ball is clicked and a ball is currently selected, swap the colors of the two balls
#                     else:
#                         temp_color = selected_ball.color
#                         selected_ball.color = ball.color
#                         ball.color = temp_color
#                         selected_ball = None  

#         # Check if the game is won (all balls are green)
#         if all(ball.color == GREEN for ball in balls):
#             game_won = True

#     # Fill the screen with white
#     s.fill(WHITE)

#     # Draw all the balls on the screen
#     for ball in balls:
#         ball.draw(s)

#     # If the game is won, display a congratulatory message
#     if game_won:
#         # Create a font object
#         font = pygame.font.Font(None, 36)  
#         # Render the text
#         text_surface = font.render("Congratulations! You won!", True, BLACK)
#         # Get the rectangle of the text
#         text_rect = text_surface.get_rect(center=(s_w // 2, s_h // 2))
#         # Draw the text on the screen
#         s.blit(text_surface, text_rect)

#     # Update the display
#     pygame.display.flip()

# # Quit the pygame library
# pygame.quit() 

import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Shape:
    def __init__(self, x, y, size, color, shape_type):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.shape_type = shape_type
        self.velocity = [random.randint(-3, 3), random.randint(-3, 3)]
        self.is_moving = True

    def draw(self, screen):
        if self.shape_type == 'rectangle':
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
        elif self.shape_type == 'square':
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
        elif self.shape_type == 'triangle':
            points = [(self.x + self.size/2, self.y),
                      (self.x, self.y + self.size),
                      (self.x + self.size, self.y + self.size)]
            pygame.draw.polygon(screen, self.color, points)
        elif self.shape_type == 'star':
            points = [(self.x + self.size/2, self.y),
                      (self.x + self.size/3, self.y + self.size/3),
                      (self.x, self.y + self.size/2),
                      (self.x + self.size/3, self.y + 2*self.size/3),
                      (self.x + self.size/2, self.y + self.size),
                      (self.x + 2*self.size/3, self.y + 2*self.size/3),
                      (self.x + self.size, self.y + self.size/2),
                      (self.x + 2*self.size/3, self.y + self.size/3)]
            pygame.draw.polygon(screen, self.color, points)

    def move(self):
        if self.is_moving:
            self.x += self.velocity[0]
            self.y += self.velocity[1]

            if self.x <= 0 or self.x >= WIDTH:
                self.velocity[0] *= -1
            if self.y <= 0 or self.y >= HEIGHT:
                self.velocity[1] *= -1

class Ball:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = GREEN

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shape Fusion Game")
clock = pygame.time.Clock()

shapes = []
for _ in range(10):
    x = random.randint(50, WIDTH - 50)
    y = random.randint(50, HEIGHT - 50)
    size = random.randint(20, 50)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    shape_type = random.choice(['rectangle', 'square', 'triangle'])
    shapes.append(Shape(x, y, size, color, shape_type))

ball = Ball(WIDTH // 2, HEIGHT // 2, 20)

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for shape in shapes:
                if shape.x <= event.pos[0] <= shape.x + shape.size and shape.y <= event.pos[1] <= shape.y + shape.size:
                    shape.is_moving = not shape.is_moving
            if ball.x - ball.size <= event.pos[0] <= ball.x + ball.size and ball.y - ball.size <= event.pos[1] <= ball.y + ball.size:
                if ball.color == GREEN:
                    ball.color = RED
                    for shape in shapes:
                        shape.is_moving = False
                else:
                    ball.color = GREEN
                    for shape in shapes:
                        shape.is_moving = True

    for shape in shapes:
        shape.move()

    for shape in shapes:
        shape.draw(screen)

    ball.draw(screen)

    for i in range(len(shapes)):
        for j in range(i + 1, len(shapes)):
            shape1 = shapes[i]
            shape2 = shapes[j]
            if shape1.shape_type == 'triangle' or shape2.shape_type == 'triangle':
                # Collision detection for triangle
                if pygame.Rect(shape1.x, shape1.y, shape1.size, shape1.size).colliderect(pygame.Rect(shape2.x, shape2.y, shape2.size, shape2.size)):
                    new_size = (shape1.size + shape2.size) // 2
                    new_color = ((shape1.color[0] + shape2.color[0]) // 2, (shape1.color[1] + shape2.color[1]) // 2, (shape1.color[2] + shape2.color[2]) // 2)
                    new_shape = Shape(shape1.x, shape1.y, new_size, new_color, 'star')
                    shapes.append(new_shape)
                    shapes.remove(shape1)
                    shapes.remove(shape2)
                    break
            else:
                distance = math.sqrt((shape1.x - shape2.x)**2 + (shape1.y - shape2.y)**2)
                if distance <= shape1.size / 2 + shape2.size / 2:
                    new_size = (shape1.size + shape2.size) // 2
                    new_color = ((shape1.color[0] + shape2.color[0]) // 2, (shape1.color[1] + shape2.color[1]) // 2, (shape1.color[2] + shape2.color[2]) // 2)
                    new_shape = Shape(shape1.x, shape1.y, new_size, new_color, 'star')
                    shapes.append(new_shape)
                    shapes.remove(shape1)
                    shapes.remove(shape2)
                    break

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()