import pygame 
import random 
import sys 


pygame.init()


WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("4x4 Grid Gambling Game")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255) 

font = pygame.font.SysFont("Arial", 24) 

balance = 4

GRID_SIZE = 4 
CELL_SIZE = WIDTH // GRID_SIZE

grid_bets = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

dice_result = (0,0)

def draw_grid():
    for row in range(GRID_SIZE): 
        for col in range(GRID_SIZE): 
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            pygame.draw.rect(screen, BLACK, (x,y, CELL_SIZE, CELL_SIZE), 2)
            if grid_bets[row][col] > 0: 
                bet_text = font.render(f"${grid_bets[row][col]}", True, BLUE) 
                screen.blit(bet_text, (x+10, y+10))
                
def roll_dice(): 
    return random.randint(1,6), random.randint(1,6)

def check_win(dice): 
    return dice[0] == row + 1 and dice[1] == col + 1

running = True
selected_row, selected_col = None, None
game_message = "Please a bet by clicking a cell and pressing 1 -9 to bet" 

while running: 
    screen.fill(WHITE)
    draw_grid()
    balance_text = font.render(f"Balance: ${balance}", True, BLACK)
    screen.blit(balance_text, (10, 50))
    dice_text = font.render(f"Dice Result: {dice_result[0]}, {dice_result[1]}", True, BLACK)
    screen.blit(dice_text, (10,90)) 
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
            
        if event.type == pygame.MOUSEBUTTONDOWN: 
            mouse_x, mouse_y = pygame.mouse.get_pos()
            selected_row = mouse_y // CELL_SIZE
            selected_col = mouse_x // CELL_SIZE
    
        if event.type == pygame.KEYDOWN: 
            if event.unicode.isdigit() and selected_row is not None and selected_col is not None: 
                bet_amount = int(event.unicode)
                if bet_amount <= balance :
                    grid_bets[selected_row][selected_col] = bet_amount
                    balance -= bet_amount
                    game_message = f"Placed ${bet_amount} on cell ({selected_row +1}, {selected_col +1})"
                    
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
            if selected_row is not None and selected_col is not None and grid_bets[selected_row][selected_col] > 0: 
                dice_result = roll_dice() 
                if check_win(dice_result): 
                    win_amount = grid_bets[selected_row][selected_col] * 2 
                    balance += win_amount 
                    game_message = f"You won ${win_amount} on cell {selected_row +1}, {selected_col+1}"
                else: 
                    game_message = f"You lost your bet on cell ({selected_row +1}, {selected_col +1})"
                    
                grid_bets[selected_row][selected_col] = 0
                
        if balance <= 0: 
            game_message = "Game Over! You ran out of money."
            running = False
        
        pygame.display.update() 
        
pygame.quit()
sys.exit() 
                
                
                
                





    
                    