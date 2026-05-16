import os

import pygame

WIDTH = 750
HEIGHT = 600

SIDE_MARGIN = 20
TOP_MARGIN = 120
SPACING = 20
MINI_SIZE = 180

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

FPS = 60

PIECE_WIDTH = 70
PIECE_HEIGHT = 70

White_Pawn_Image = pygame.image.load(os.path.join('pcs', 'white_pawn.png'))
White_Pawn = pygame.transform.rotate(pygame.transform.scale(White_Pawn_Image, (PIECE_WIDTH, PIECE_HEIGHT)), 0)

Black_Pawn_Image = pygame.image.load(os.path.join('pcs', 'black_pawn.png'))
Black_Pawn = pygame.transform.rotate(pygame.transform.scale(Black_Pawn_Image, (PIECE_WIDTH, PIECE_HEIGHT)), 0)

White_Knight_Image = pygame.image.load(os.path.join('pcs', 'white_knight.png'))
White_Knight = pygame.transform.rotate(pygame.transform.scale(White_Knight_Image, (PIECE_WIDTH, PIECE_HEIGHT)), 0)

Black_Knight_Image = pygame.image.load(os.path.join('pcs', 'black_knight.png'))
Black_Knight = pygame.transform.rotate(pygame.transform.scale(Black_Knight_Image, (PIECE_WIDTH, PIECE_HEIGHT)), 0)

White_Bishop_Image = pygame.image.load(os.path.join('pcs', 'white_bishop.png'))
White_Bishop = pygame.transform.rotate(pygame.transform.scale(White_Bishop_Image, (PIECE_WIDTH, PIECE_HEIGHT)), 0)

Black_Bishop_Image = pygame.image.load(os.path.join('pcs', 'black_bishop.png'))
Black_Bishop = pygame.transform.rotate(pygame.transform.scale(Black_Bishop_Image, (PIECE_WIDTH, PIECE_HEIGHT)), 0)

White_Rook_Image = pygame.image.load(os.path.join('pcs', 'white_rook.png'))
White_Rook = pygame.transform.rotate(pygame.transform.scale(White_Rook_Image, (PIECE_WIDTH, PIECE_HEIGHT)), 0)

Black_Rook_Image = pygame.image.load(os.path.join('pcs', 'black_rook.png'))
Black_Rook = pygame.transform.rotate(pygame.transform.scale(Black_Rook_Image, (PIECE_WIDTH, PIECE_HEIGHT)), 0)

White_Queen_Image = pygame.image.load(os.path.join('pcs', 'white_queen.png'))
White_Queen = pygame.transform.rotate(pygame.transform.scale(White_Queen_Image, (PIECE_WIDTH, PIECE_HEIGHT)), 0)

Black_Queen_Image = pygame.image.load(os.path.join('pcs', 'black_queen.png'))
Black_Queen = pygame.transform.rotate(pygame.transform.scale(Black_Queen_Image, (PIECE_WIDTH, PIECE_HEIGHT)), 0)

White_King_Image = pygame.image.load(os.path.join('pcs', 'white_king.png'))
White_King = pygame.transform.rotate(pygame.transform.scale(White_King_Image, (PIECE_WIDTH, PIECE_HEIGHT)), 0)

Black_King_Image = pygame.image.load(os.path.join('pcs', 'black_king.png'))
Black_King = pygame.transform.rotate(pygame.transform.scale(Black_King_Image, (PIECE_WIDTH, PIECE_HEIGHT)), 0)
