import pygame

# BOARD
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MOCHA = (103, 80, 65)
CREAM = (248, 240, 227)
BLUE = (0, 0, 255)

# PIECE DIMENSIONS
DIM = (80, 80)

# PIECES
# pawns
W_PAWN = pygame.transform.scale(pygame.image.load("assets/w_pawn.png"), DIM)
B_PAWN = pygame.transform.scale(pygame.image.load("assets/b_pawn.png"), DIM)

# rooks
W_ROOK = pygame.transform.scale(pygame.image.load("assets/w_rook.png"), DIM)
B_ROOK = pygame.transform.scale(pygame.image.load("assets/b_rook.png"), DIM)

# bishops
W_BISHOP = pygame.transform.scale(pygame.image.load("assets/w_bishop.png"), DIM)
B_BISHOP = pygame.transform.scale(pygame.image.load("assets/b_bishop.png"), DIM)

# knights
W_KNIGHT = pygame.transform.scale(pygame.image.load("assets/w_knight.png"), DIM)
B_KNIGHT = pygame.transform.scale(pygame.image.load("assets/b_knight.png"), DIM)

# queens
W_QUEEN = pygame.transform.scale(pygame.image.load("assets/w_queen.png"), DIM)
B_QUEEN = pygame.transform.scale(pygame.image.load("assets/b_queen.png"), DIM)

# kings
W_KING = pygame.transform.scale(pygame.image.load("assets/w_king.png"), DIM)
B_KING = pygame.transform.scale(pygame.image.load("assets/b_king.png"), DIM)
