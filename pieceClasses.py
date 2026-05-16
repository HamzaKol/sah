
import pygame

from constants import Black_Bishop, Black_King, Black_Knight, Black_Pawn, Black_Queen, Black_Rook, White_Bishop, White_King, White_Knight, White_Pawn, White_Queen, White_Rook


class Pawn:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.obj = "Pawn"
        self.has_moved = False

        if color == "white":
            self.object = White_Pawn
        else:
            self.object = Black_Pawn

    def draw(self, win, board_x, board_y, tile_size, use_board_position=True):

        if use_board_position:

            draw_x = board_x + self.col * tile_size
            draw_y = board_y + self.row * tile_size

        else:

            draw_x = board_x
            draw_y = board_y

        scaled_image = pygame.transform.scale(
            self.object,
            (tile_size, tile_size)
)

        win.blit(scaled_image, (draw_x, draw_y))


    def valid_move(self, new_row, new_col):

        direction = -1 if self.color == "white" else 1
        if (
            new_col == self.col
            and
            new_row == self.row + direction
        ):
            return True

        if self.color == "white":
            start_row = 6
        else:
            start_row = 1

        if (
            self.row == start_row
            and
            new_col == self.col
            and
            new_row == self.row + direction * 2
        ):
            return True

        return False

class Knight:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.obj = "Knight"
        self.has_moved = False

        if color == "white":
            self.object = White_Knight
        else:
            self.object = Black_Knight
    
    def draw(self, win, board_x, board_y, tile_size, use_board_position=True):

        if use_board_position:

            draw_x = board_x + self.col * tile_size
            draw_y = board_y + self.row * tile_size

        else:

            draw_x = board_x
            draw_y = board_y

        scaled_image = pygame.transform.scale(
            self.object,
            (tile_size, tile_size)
)

        win.blit(scaled_image, (draw_x, draw_y))

    def valid_move(self, new_row, new_col):

        row_diff = abs(self.row - new_row)
        col_diff = abs(self.col - new_col)

        return (
            (row_diff == 2 and col_diff == 1)
            or
            (row_diff == 1 and col_diff == 2)
        )

class Bishop:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.obj = "Bishop"
        self.has_moved = False

        if color == "white":
            self.object = White_Bishop
        else:
            self.object = Black_Bishop

    def draw(self, win, board_x, board_y, tile_size, use_board_position=True):

        if use_board_position:

            draw_x = board_x + self.col * tile_size
            draw_y = board_y + self.row * tile_size

        else:

            draw_x = board_x
            draw_y = board_y

        scaled_image = pygame.transform.scale(
            self.object,
            (tile_size, tile_size)
)

        win.blit(scaled_image, (draw_x, draw_y))

    def valid_move(self, new_row, new_col):

        row_diff = abs(self.row - new_row)
        col_diff = abs(self.col - new_col)

        return row_diff == col_diff

class Rook:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.obj = "Rook"
        self.has_moved = False

        if color == "white":
            self.object = White_Rook
        else:
            self.object = Black_Rook

    def draw(self, win, board_x, board_y, tile_size, use_board_position=True):

        if use_board_position:

            draw_x = board_x + self.col * tile_size
            draw_y = board_y + self.row * tile_size

        else:

            draw_x = board_x
            draw_y = board_y

        scaled_image = pygame.transform.scale(
            self.object,
            (tile_size, tile_size)
)

        win.blit(scaled_image, (draw_x, draw_y))

    def valid_move(self, new_row, new_col):

        return (
            self.row == new_row
            or
            self.col == new_col
        )

class Queen:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.obj = "Queen"
        self.has_moved = False

        if color == "white":
            self.object = White_Queen
        else:
            self.object = Black_Queen
        
    def draw(self, win, board_x, board_y, tile_size, use_board_position=True):

        if use_board_position:

            draw_x = board_x + self.col * tile_size
            draw_y = board_y + self.row * tile_size

        else:

            draw_x = board_x
            draw_y = board_y

        scaled_image = pygame.transform.scale(
            self.object,
            (tile_size, tile_size)
)

        win.blit(scaled_image, (draw_x, draw_y))

    def valid_move(self, new_row, new_col):

        row_diff = abs(self.row - new_row)
        col_diff = abs(self.col - new_col)

        return (
            self.row == new_row
            or
            self.col == new_col
            or
            row_diff == col_diff
        )

class King:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.obj = "King"
        self.has_moved = False

        if color == "white":
            self.object = White_King
        else:
            self.object = Black_King
    
    def draw(self, win, board_x, board_y, tile_size, use_board_position=True):

        if use_board_position:

            draw_x = board_x + self.col * tile_size
            draw_y = board_y + self.row * tile_size

        else:

            draw_x = board_x
            draw_y = board_y

        scaled_image = pygame.transform.scale(
            self.object,
            (tile_size, tile_size)
)

        win.blit(scaled_image, (draw_x, draw_y))

    def valid_move(self, new_row, new_col):

        row_diff = abs(self.row - new_row)
        col_diff = abs(self.col - new_col)

        return row_diff <= 1 and col_diff <= 1
    
