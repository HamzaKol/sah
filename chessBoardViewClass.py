import pygame

from constants import BLUE, WHITE
from pieceClasses import Bishop, Knight, Queen, Rook


class ChessBoardView:

    def __init__(
        self,
        game,
        x,
        y,
        size,
        interactive=True
    ):

        self.game = game

        self.x = x
        self.y = y

        self.size = size

        self.tile_size = size // 8

        self.interactive = interactive

    def draw(self, win):

        self.draw_board(win)
        self.draw_pieces(win)
        self.draw_selected_piece(win)
        self.draw_check(win)
        self.draw_promotion_menu(win)
        self.draw_game_over(win)

    def draw_board(self, win):

        for row in range(8):

            for col in range(8):

                color = WHITE

                if (row + col) % 2 == 1:
                    color = BLUE

                pygame.draw.rect(
                    win,
                    color,
                    (
                        self.x + col * self.tile_size,
                        self.y + row * self.tile_size,
                        self.tile_size,
                        self.tile_size
                    )
                )

    def draw_pieces(self, win):

        for piece in self.game.white_pieces:
            piece.draw(
                win,
                self.x,
                self.y,
                self.tile_size
            )

        for piece in self.game.black_pieces:
            piece.draw(
                win,
                self.x,
                self.y,
                self.tile_size
            )

    def draw_selected_piece(self, win):
        if self.game.selected_piece is not None:

            pygame.draw.rect(
                win,
                (255, 0, 0),
                (
                    self.x + self.game.selected_piece.col * self.tile_size,
                    self.y + self.game.selected_piece.row * self.tile_size,
                    self.tile_size,
                    self.tile_size
                ),
                3
            )
    
    def draw_check(self, win):

        if self.game.is_in_check("white"):

            king = self.game.get_king("white")

            pygame.draw.rect(
                win,
                (255, 0, 0),
                (
                    self.x + king.col * self.tile_size,
                    self.y + king.row * self.tile_size,
                    self.tile_size,
                    self.tile_size
                ),
                5
            )

        if self.game.is_in_check("black"):

            king = self.game.get_king("black")

            pygame.draw.rect(
                win,
                (255, 0, 0),
                (
                    self.x + king.col * self.tile_size,
                    self.y + king.row * self.tile_size,
                    self.tile_size,
                    self.tile_size
                ),
                5
            )
    
    def handle_click(self, mouse_x, mouse_y):

        if not self.interactive:
            return

        if self.game.promoting_pawn is not None:

            self.handle_promotion_click(
                mouse_x,
                mouse_y
            )

            return

        col = (mouse_x - self.x) // self.tile_size
        row = (mouse_y - self.y) // self.tile_size

        if not (0 <= row < 8 and 0 <= col < 8):
            return

        self.game.handle_click(row, col)
    
    def handle_promotion_click(
        self,
        mouse_x,
        mouse_y
    ):

        menu_x = self.x + self.size + 20
        menu_y = self.y

        if not (
            menu_x <= mouse_x <= menu_x + 100
        ):
            return

        option = (mouse_y - menu_y) // self.tile_size

        promotion_options = [
            "Queen",
            "Rook",
            "Bishop",
            "Knight"
        ]

        if not (
            0 <= option < 4
        ):
            return

        selected_piece = promotion_options[option]

        self.game.promote_pawn(
            selected_piece
        )

    def draw_promotion_menu(self, win):

        if self.game.promoting_pawn is None:
            return

        menu_x = self.x + self.size + 20
        menu_y = self.y

        pygame.draw.rect(
            win,
            (40, 40, 40),
            (
                menu_x,
                menu_y,
                self.tile_size + 20,
                self.tile_size * 4
            )
        )

        color = self.game.promoting_pawn.color

        pieces = [
            Queen(0, 0, color),
            Rook(0, 0, color),
            Bishop(0, 0, color),
            Knight(0, 0, color)
        ]

        for i, piece in enumerate(pieces):

            piece.draw(
                win,
                menu_x,
                menu_y + i * self.tile_size,
                self.tile_size,
                use_board_position=False
            )

    def draw_game_over(self, win):

        if not self.game.game_over:
            return

        overlay = pygame.Surface(
            (self.size, self.size)
        )

        overlay.set_alpha(180)

        overlay.fill((0, 0, 0))

        win.blit(
            overlay,
            (self.x, self.y)
        )

        font_size = max(24, self.tile_size)

        font = pygame.font.SysFont(
            "arial",
            font_size
        )

        if self.game.is_draw:

            text = font.render(
                "Draw",
                True,
                (255, 255, 255)
            )

        else:

            text = font.render(
                f"{self.game.winner.capitalize()} Wins",
                True,
                (255, 255, 255)
            )

        text_rect = text.get_rect(
            center=(
                self.x + self.size // 2,
                self.y + self.size // 2
            )
        )

        win.blit(text, text_rect)