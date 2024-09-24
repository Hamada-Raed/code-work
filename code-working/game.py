import random 
import pygame 
import sys 

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collect Points Game") 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

player_size = 50
player_x = WIDTH // 2 
player_y = HEIGHT - 2 * player_size
player_speed = 5 

object_size = 50
object_x = random.randint(0, WIDTH - object_size)
object_y = 0
object_speed = 5

points = 0 
money = 0 
point_to_money_ratio = 10

font = pygame.font.SysFont("Arial", 24)

running = True

while running: 
    pygame.time.delay(30)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and player_x - player_speed > 0: 
        player_x -= player_speed 
        
    if keys[pygame.K_RIGHT] and player_x + player_speed < WIDTH - player_size: 
        player_x += player_speed 
        
    object_y += object_speed 
    
    if object_y > HEIGHT: 
        object_x = random.randint(0, WIDTH - object_size)
        object_y = 0 
        
    if (player_x < object_x < player_x + player_size or player_x < object_x + object_size < player_x + player_size) and (player_y < object_y + object_size < player_y + player_size): 
        points += 1 
        object_x = random.randint(0, WIDTH - object_size)
        object_y = 0
        
    if points >= point_to_money_ratio: 
        money += points // point_to_money_ratio 
        points %= point_to_money_ratio
        
    screen.fill(WHITE)
    
    pygame.draw.rect(screen, RED, (object_x, object_y, object_size, object_size))
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_size, player_size))
    
    points_text = font.render(f"Points: {points}", True, BLACK)
    money_text = font.render(f"Money: {money}", True, BLACK)
    screen.blit(points_text, (10, 10))
    screen.blit(money_text, (10, 40))
    
    pygame.display.update()
    
pygame.quit()
sys.exit()
