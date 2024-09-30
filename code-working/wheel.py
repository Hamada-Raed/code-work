import pygame
import random
import math

pygame.init()

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Wheel of Luck")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER_COLOR = (100, 149, 237)

font = pygame.font.Font(None, 36)

wheel_radius = 250
center_x = screen_width // 2
center_y = screen_height // 2

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

spin_speed = 0
spin_angle = 0
deceleration = 0.1
is_spinning = False
result = None

button_width = 150
button_height = 50
button_x = (screen_width - button_width) // 2
button_y = screen_height - 100
spin_button = pygame.Rect(button_x, button_y, button_width, button_height)

def draw_wheel(angle):
    for i, section in enumerate(sections):
        start_angle = angle_per_section * i + angle
        end_angle = angle_per_section * (i + 1) + angle
        
        start_angle_rad = math.radians(start_angle)
        end_angle_rad = math.radians(end_angle)

        points = [(center_x, center_y)]
        for a in range(int(start_angle), int(end_angle) + 1):
            x = center_x + wheel_radius * math.cos(math.radians(a))
            y = center_y + wheel_radius * math.sin(math.radians(a))
            points.append((x, y))

        pygame.draw.polygon(screen, section["color"], points)

        text_angle = (start_angle + end_angle) / 2
        text_x = center_x + (wheel_radius // 2) * math.cos(math.radians(text_angle))
        text_y = center_y + (wheel_radius // 2) * math.sin(math.radians(text_angle))
        label = font.render(section["label"], True, WHITE)
        screen.blit(label, (text_x - label.get_width() // 2, text_y - label.get_height() // 2))

def draw_rotating_arrow(angle):
    arrow_length = 30
    arrow_angle = angle % 360

    arrow_x = center_x + (wheel_radius + arrow_length) * math.cos(math.radians(arrow_angle))
    arrow_y = center_y + (wheel_radius + arrow_length) * math.sin(math.radians(arrow_angle))

    pygame.draw.circle(screen, YELLOW, (int(arrow_x), int(arrow_y)), 10)

def get_result(final_angle):
    index = int((final_angle % 360) / angle_per_section)
    return sections[index]["label"]

def draw_button():
    mouse_pos = pygame.mouse.get_pos()
    if spin_button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, spin_button)
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, spin_button)

    button_text = font.render("SPIN", True, WHITE)
    screen.blit(button_text, (spin_button.x + (button_width - button_text.get_width()) // 2, spin_button.y + (button_height - button_text.get_height()) // 2))

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if spin_button.collidepoint(event.pos) and not is_spinning:
                spin_speed = random.uniform(10, 20)  
                is_spinning = True
                result = None

    if is_spinning:
        spin_angle += spin_speed
        spin_speed -= deceleration  
        if spin_speed <= 0:
            spin_speed = 0
            is_spinning = False
            result = get_result(spin_angle)

    draw_wheel(spin_angle)
    draw_rotating_arrow(spin_angle)
    draw_button()

    if result:
        result_text = font.render(f"Result: {result}", True, BLACK)
        screen.blit(result_text, (center_x - result_text.get_width() // 2, screen_height - 50))

    pygame.display.update()

pygame.quit()
