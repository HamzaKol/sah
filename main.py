import pygame

from chessBoardViewClass import ChessBoardView
from constants import MINI_SIZE, SPACING, TOP_MARGIN
from gameClass import ChessGame


pygame.init()

WIDTH = 1400
HEIGHT = 900

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Multi Board Test")

FPS = 60

clock = pygame.time.Clock()

main_game = ChessGame()

main_board = ChessBoardView(
    game=main_game,
    x=350,
    y=120,
    size=640,
    interactive=True
)

mini_boards = []
mini_positions = []

for i in range(3):

    y = TOP_MARGIN + i * (MINI_SIZE + SPACING)

    mini_positions.append((20, y))
    mini_positions.append((1180, y))

for x, y in mini_positions:

    game = ChessGame()

    # test moves
    game.play_move("e2e4")
    game.play_move("e7e5")

    board = ChessBoardView(
        game=game,
        x=x,
        y=y,
        size=180,
        interactive=False
    )

    mini_boards.append(board)

run = True

while run:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = pygame.mouse.get_pos()

            if main_board.interactive:

                main_board.handle_click(
                    mouse_x,
                    mouse_y
                )
    WIN.fill((30, 30, 30))

    main_board.draw(WIN)

    for board in mini_boards:
        board.draw(WIN)

    pygame.display.update()

pygame.quit()