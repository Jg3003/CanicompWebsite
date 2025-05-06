import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Grid variables
ROWS, COLS = 3, 3
CELL_SIZE = WIDTH // COLS

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Fonts
font = pygame.font.Font(None, 120)

# Game variables
board = [[None for _ in range(COLS)] for _ in range(ROWS)]
current_player = "X"

def draw_grid():
    for x in range(1, COLS):
        pygame.draw.line(screen, BLACK, (x * CELL_SIZE, 0), (x * CELL_SIZE, HEIGHT), 5)
    for y in range(1, ROWS):
        pygame.draw.line(screen, BLACK, (0, y * CELL_SIZE), (WIDTH, y * CELL_SIZE), 5)

def draw_marks():
    for row in range(ROWS):
        for col in range(COLS):
            mark = board[row][col]
            if mark:
                color = RED if mark == "X" else BLUE
                text = font.render(mark, True, color)
                text_rect = text.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(text, text_rect)

def check_winner():
    # Check rows and columns
    for i in range(ROWS):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0]:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i]:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2]:
        return board[0][2]

    # Check for a tie
    if all(board[row][col] for row in range(ROWS) for col in range(COLS)):
        return "Tie"

    return None

def reset_game():
    global board, current_player
    board = [[None for _ in range(COLS)] for _ in range(ROWS)]
    current_player = "X"

# Main loop
running = True
winner = None
while running:
    screen.fill(WHITE)
    draw_grid()
    draw_marks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not winner:
            x, y = event.pos
            col, row = x // CELL_SIZE, y // CELL_SIZE
            if not board[row][col]:
                board[row][col] = current_player
                winner = check_winner()
                current_player = "O" if current_player == "X" else "X"
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reset_game()
            winner = None

    if winner:
        text = font.render(f"{winner} wins!" if winner != "Tie" else "It's a tie!", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()