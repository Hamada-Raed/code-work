import pygame
import random
import math

# Initialize pygame
pygame.init()

# Set up display
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Wheel of Luck")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Font setup
font = pygame.font.Font(None, 36)

# Wheel properties
wheel_radius = 250
center_x = screen_width // 2
center_y = screen_height // 2

# Sections and their labels
sections = [
    {"label": "$100", "color": RED},
    {"label": "$50", "color": GREEN},
    {"label": "Lose", "color": BLUE},
    {"label": "Better Luck", "color": BLACK},
    {"label": "$200", "color": GREEN},
    {"label": "Lose Half", "color": RED},
]

num_sections = len(sections)
angle_per_section = 360 / num_sections

# Variables to control the spin
spin_speed = 0
spin_angle = 0
deceleration = 0.1
is_spinning = False
result = None

# Function to draw the wheel
def draw_wheel(angle):
    for i, section in enumerate(sections):
        # Calculate angles for each section
        start_angle = angle_per_section * i + angle
        end_angle = angle_per_section * (i + 1) + angle
        pygame.draw.arc(screen, section["color"], 
            (center_x - wheel_radius, center_y - wheel_radius, wheel_radius * 2, wheel_radius * 2), 
            math.radians(start_angle), math.radians(end_angle), wheel_radius)

# Function to determine the result
def get_result(final_angle):
    index = int((final_angle % 360) / angle_per_section)
    return sections[index]["label"]

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_spinning:
                spin_speed = random.uniform(10, 20)  # Random speed for the wheel
                is_spinning = True
                result = None

    if is_spinning:
        spin_angle += spin_speed
        spin_speed -= deceleration  # Slow down the spin
        if spin_speed <= 0:
            spin_speed = 0
            is_spinning = False
            result = get_result(spin_angle)  # Get the result when the wheel stops spinning

    draw_wheel(spin_angle)

    # Display the result
    if result:
        result_text = font.render(f"Result: {result}", True, BLACK)
        screen.blit(result_text, (center_x - result_text.get_width() // 2, screen_height - 50))

    pygame.display.update()

# Quit pygame
pygame.quit()
