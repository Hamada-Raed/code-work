import pygame
import random
import sys

pygame.init()

# Game settings
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Fixed: size must be passed as a tuple
pygame.display.set_caption("Poker-Inspired Grid Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Font
font = pygame.font.SysFont("Arial", 24)

# Deck of cards
deck = [(rank, suit) for rank in range(1, 14) for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]]

# Grid for the game
grid = [[None for _ in range(4)] for _ in range(4)]

# Bet tracking
bet = {"row": None, "column": None, "diagonal": None}

# Player balance
balance = 100

# Function to deal cards
def deal_cards():
    global deck, grid
    random.shuffle(deck)
    index = 0

    for row in range(4):
        for col in range(4):
            x = col * (WIDTH // 4)  # Fixed typo from WDITH to WIDTH
            y = row * (HEIGHT // 4)
            pygame.draw.rect(screen, BLACK, (x, y, WIDTH // 4, HEIGHT // 4), 2)
            card = deck[index]
            grid[row][col] = card  # Assign card to the grid
            index += 1

# Function to evaluate hand
def evaluate_hand(cards):
    ranks = [card[0] for card in cards]
    suits = [card[1] for card in cards]

    rank_count = {rank: ranks.count(rank) for rank in ranks}

    if 4 in rank_count.values():
        return "4-of-a-kind"
    elif 3 in rank_count.values() and 2 in rank_count.values():
        return "Full House"
    elif 3 in rank_count.values():
        return "Three of a Kind"
    elif list(rank_count.values()).count(2) == 2:
        return "Two Pair"
    elif 2 in rank_count.values():
        return "Pair"

    if len(set(suits)) == 1:
        return "Flush"

    return "High Card"

# Function to retrieve cards for the current bet
def get_bet_cards():
    cards = []
    if bet["row"] is not None:
        cards = grid[bet["row"]]
    elif bet["column"] is not None:
        cards = [grid[row][bet["column"]] for row in range(4)]
    elif bet["diagonal"] == "left":
        cards = [grid[i][i] for i in range(4)]
    elif bet["diagonal"] == "right":
        cards = [grid[i][3 - i] for i in range(4)]
    return cards

# Function to draw the grid
def draw_grid():
    for row in range(4):
        for col in range(4):
            x = col * (WIDTH // 4)
            y = row * (HEIGHT // 4)
            pygame.draw.rect(screen, BLACK, (x, y, WIDTH // 4, HEIGHT // 4), 2)  # Draws the grid lines
            card = grid[row][col]
            if card:
                card_text = font.render(f"{card[0]} {card[1][0]}", True, BLUE)  # Renders the card details
                screen.blit(card_text, (x + 10, y + 10))  # Places the card in the correct spot

# Main game loop
running = True
game_message = "Place a bet on a row, column, or diagonal"
deal_cards()

while running:
    screen.fill(WHITE)
    balance_text = font.render(f"Balance: {balance}", True, BLACK)
    screen.blit(balance_text, (10, 10))
    message_text = font.render(game_message, True, BLACK)
    screen.blit(message_text, (10, 50))

    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                bet["row"] = 0
                game_message = "Bet on Row 1"

            elif event.key == pygame.K_2:
                bet["row"] = 1
                game_message = "Bet on Row 2"

            elif event.key == pygame.K_3:
                bet["row"] = 2
                game_message = "Bet on Row 3"

            elif event.key == pygame.K_4:
                bet["row"] = 3
                game_message = "Bet on Row 4"

            elif event.key == pygame.K_q:
                bet["column"] = 0
                game_message = "Bet on Column 1"

            elif event.key == pygame.K_w:
                bet["column"] = 1
                game_message = "Bet on Column 2"

            elif event.key == pygame.K_e:
                bet["column"] = 2
                game_message = "Bet on Column 3"

            elif event.key == pygame.K_r:
                bet["column"] = 3
                game_message = "Bet on Column 4"

            elif event.key == pygame.K_a:
                bet["diagonal"] = "left"
                game_message = "Bet on Left Diagonal"

            elif event.key == pygame.K_s:
                bet["diagonal"] = "right"
                game_message = "Bet on Right Diagonal"

            if event.key == pygame.K_SPACE and any(bet.values()):
                cards = get_bet_cards()
                if cards:
                    hand = evaluate_hand(cards)
                    if hand == "4-of-a-kind":
                        balance += 50
                        game_message = f"You won with {hand}! (+$50)"

                    elif hand == "Full House":
                        balance += 40
                        game_message = f"You won with {hand}! (+$40)"

                    elif hand == "Three of a Kind":
                        balance += 30
                        game_message = f"You won with {hand}! (+$30)"

                    elif hand == "Two Pair":
                        balance += 25
                        game_message = f"You won with {hand}! (+$25)"

                    elif hand == "Pair":
                        balance += 15
                        game_message = f"You won with {hand}! (+$15)"

                    else:
                        balance -= 10
                        game_message = f"You lost! {hand}! (-$10)"
                else:
                    game_message = "Select a row, column, or diagonal to bet on."

    pygame.display.update()

pygame.quit()
sys.exit()
