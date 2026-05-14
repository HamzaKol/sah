import pygame

from constants import WHITE, BLUE
from pieceClasses import Pawn, Rook, Knight, Bishop, Queen, King


class Game:

    TILE_SIZE = 75

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.turn = "white"
        self.selected_piece = None

        self.last_move = None

        self.promoting_pawn = None

        self.white_pieces = []
        self.black_pieces = []

        self.create_pieces()

    def create_pieces(self):

        for col in range(8):
            self.white_pieces.append(Pawn(6, col, "white"))
            self.black_pieces.append(Pawn(1, col, "black"))

        self.white_pieces.append(Rook(7, 0, "white"))
        self.white_pieces.append(Rook(7, 7, "white"))

        self.black_pieces.append(Rook(0, 0, "black"))
        self.black_pieces.append(Rook(0, 7, "black"))

        self.white_pieces.append(Knight(7, 1, "white"))
        self.white_pieces.append(Knight(7, 6, "white"))

        self.black_pieces.append(Knight(0, 1, "black"))
        self.black_pieces.append(Knight(0, 6, "black"))

        self.white_pieces.append(Bishop(7, 2, "white"))
        self.white_pieces.append(Bishop(7, 5, "white"))

        self.black_pieces.append(Bishop(0, 2, "black"))
        self.black_pieces.append(Bishop(0, 5, "black"))

        self.white_pieces.append(Queen(7, 3, "white"))
        self.black_pieces.append(Queen(0, 3, "black"))

        self.white_pieces.append(King(7, 4, "white"))
        self.black_pieces.append(King(0, 4, "black"))

    def draw(self, win):

        for row in range(8):

            for col in range(8):

                color = WHITE

                if (row + col) % 2 == 1:
                    color = BLUE

                pygame.draw.rect(
                    win,
                    color,
                    (
                        self.x + col * self.TILE_SIZE,
                        self.y + row * self.TILE_SIZE,
                        self.TILE_SIZE,
                        self.TILE_SIZE
                    )
                )

        for piece in self.white_pieces:
            piece.draw(win, self.x, self.y)

        for piece in self.black_pieces:
            piece.draw(win, self.x, self.y)

        if self.selected_piece is not None:

            pygame.draw.rect(
                win,
                (255, 0, 0),
                (
                    self.x + self.selected_piece.col * self.TILE_SIZE,
                    self.y + self.selected_piece.row * self.TILE_SIZE,
                    self.TILE_SIZE,
                    self.TILE_SIZE
                ),
                3
            )
    
        if self.is_in_check("white"):

            king = self.get_king("white")

            pygame.draw.rect(
                win,
                (255, 0, 0),
                (
                    self.x + king.col * self.TILE_SIZE,
                    self.y + king.row * self.TILE_SIZE,
                    self.TILE_SIZE,
                    self.TILE_SIZE
                ),
                5
            )

        if self.is_in_check("black"):

            king = self.get_king("black")

            pygame.draw.rect(
                win,
                (255, 0, 0),
                (
                    self.x + king.col * self.TILE_SIZE,
                    self.y + king.row * self.TILE_SIZE,
                    self.TILE_SIZE,
                    self.TILE_SIZE
                ),
                5
            )
        self.draw_promotion_menu(win)

    def get_piece_at(self, row, col):

        for piece in self.white_pieces + self.black_pieces:

            if piece.row == row and piece.col == col:
                return piece

        return None

    def is_path_blocked(self, start_row, start_col, end_row, end_col):

        row_direction = 0
        col_direction = 0

        if end_row > start_row:
            row_direction = 1
        elif end_row < start_row:
            row_direction = -1

        if end_col > start_col:
            col_direction = 1
        elif end_col < start_col:
            col_direction = -1

        current_row = start_row + row_direction
        current_col = start_col + col_direction

        while (current_row, current_col) != (end_row, end_col):

            if self.get_piece_at(current_row, current_col) is not None:
                return True

            current_row += row_direction
            current_col += col_direction

        return False

    def handle_click(self, mouse_x, mouse_y):

        if self.promoting_pawn is not None:

            self.handle_promotion_click(mouse_x, mouse_y)
            return

        col = (mouse_x - self.x) // self.TILE_SIZE
        row = (mouse_y - self.y) // self.TILE_SIZE

        if not (0 <= row < 8 and 0 <= col < 8):
            return

        clicked_piece = self.get_piece_at(row, col)

        if self.selected_piece is None:

            if clicked_piece is not None:

                if clicked_piece.color == self.turn:
                    self.selected_piece = clicked_piece

            return
        
        if (
            self.selected_piece.obj == "King"
            and
            clicked_piece is not None
            and
            clicked_piece.obj == "Rook"
            and
            clicked_piece.color == self.selected_piece.color
        ):

            if self.can_castle(self.selected_piece, clicked_piece):

                king = self.selected_piece
                rook = clicked_piece

                if rook.col > king.col:
                    king.col = 6
                    rook.col = 5

                else:
                    king.col = 2
                    rook.col = 3

                king.has_moved = True
                rook.has_moved = True

                self.turn = (
                    "black"
                    if self.turn == "white"
                    else "white"
                )

            self.selected_piece = None
            return

        if clicked_piece is not None:

            if clicked_piece.color == self.selected_piece.color:
                self.selected_piece = clicked_piece
                return

        if self.selected_piece.obj == "Pawn":

            valid = self.valid_pawn_move(
                self.selected_piece,
                row,
                col
            )
        else:
            valid = self.selected_piece.valid_move(row, col)

        if valid:

            blocked = False

            if self.selected_piece.obj in ["Rook", "Bishop", "Queen"]:

                blocked = self.is_path_blocked(
                    self.selected_piece.row,
                    self.selected_piece.col,
                    row,
                    col
                )

            if not blocked:

                illegal = self.move_puts_king_in_check(
                    self.selected_piece,
                    row,
                    col
                )

                if not illegal:

                    if clicked_piece is not None:

                        if clicked_piece.color == "white":
                            self.white_pieces.remove(clicked_piece)
                        else:
                            self.black_pieces.remove(clicked_piece)
                    
                    if (
                        self.selected_piece.obj == "Pawn"
                        and
                        clicked_piece is None
                        and
                        self.selected_piece.col != col
                    ):
                        captured_pawn = self.get_piece_at(
                        self.selected_piece.row,
                        col
                        )

                        if captured_pawn is not None:

                            if captured_pawn.color == "white":
                                self.white_pieces.remove(captured_pawn)
                            else:
                                self.black_pieces.remove(captured_pawn)
                    
                    old_row = self.selected_piece.row
                    old_col = self.selected_piece.col

                    self.selected_piece.row = row
                    self.selected_piece.col = col

                    if self.selected_piece.obj == "Pawn":

                        if (
                            self.selected_piece.color == "white"
                            and
                            self.selected_piece.row == 0
                        ):

                            self.promoting_pawn = self.selected_piece

                        elif (
                            self.selected_piece.color == "black"
                            and
                            self.selected_piece.row == 7
                        ):

                            self.promoting_pawn = self.selected_piece

                    self.selected_piece.has_moved = True

                    self.last_move = (
                        self.selected_piece,
                        old_row,
                        old_col,
                        row,
                        col
                    )

                    self.turn = (
                        "black"
                        if self.turn == "white"
                        else "white"
)

                    if self.is_checkmate(self.turn):

                        print(f"{self.turn} is checkmated")

                    elif self.is_stalemate(self.turn):

                        print("Stalemate")

        self.selected_piece = None
    
    def valid_pawn_move(self, pawn, new_row, new_col):

        direction = -1 if pawn.color == "white" else 1

        clicked_piece = self.get_piece_at(new_row, new_col)

        if (
            new_col == pawn.col
            and
            new_row == pawn.row + direction
        ):

            if clicked_piece is None:
                return True

        start_row = 6 if pawn.color == "white" else 1

        if (
            pawn.row == start_row
            and
            new_col == pawn.col
            and
            new_row == pawn.row + direction * 2
        ):

            middle_piece = self.get_piece_at(
                pawn.row + direction,
                pawn.col
            )

            if clicked_piece is None and middle_piece is None:
                return True

        if (
            abs(new_col - pawn.col) == 1
            and
            new_row == pawn.row + direction
        ):

            if clicked_piece is not None:

                if clicked_piece.color != pawn.color:
                    return True

        if self.can_en_passant(pawn, new_row, new_col):
            return True

        return False
    
    def get_king(self, color):
        pieces = (
            self.white_pieces
            if color == "white"
            else self.black_pieces
        )

        for piece in pieces:

            if piece.obj == "King":
                return piece

        return None

    def is_in_check(self, color):

        king = self.get_king(color)

        if king is None:
            return False

        enemy_pieces = (
            self.black_pieces
            if color == "white"
            else self.white_pieces
        )

        for piece in enemy_pieces:

            if piece.obj == "Pawn":

                direction = -1 if piece.color == "white" else 1

                if (
                    king.row == piece.row + direction
                    and
                    abs(king.col - piece.col) == 1
                ):
                    return True

            else:

                if piece.valid_move(king.row, king.col):

                    blocked = False

                    if piece.obj in ["Rook", "Bishop", "Queen"]:

                        blocked = self.is_path_blocked(
                            piece.row,
                            piece.col,
                            king.row,
                            king.col
                        )

                    if not blocked:
                        return True

        return False

    def move_puts_king_in_check(self, piece, new_row, new_col):

        old_row = piece.row
        old_col = piece.col

        captured_piece = self.get_piece_at(new_row, new_col)

        if captured_piece is not None:

            if captured_piece.color == "white":
                self.white_pieces.remove(captured_piece)
            else:
                self.black_pieces.remove(captured_piece)

        piece.row = new_row
        piece.col = new_col

        in_check = self.is_in_check(piece.color)

        piece.row = old_row
        piece.col = old_col

        if captured_piece is not None:

            if captured_piece.color == "white":
                self.white_pieces.append(captured_piece)
            else:
                self.black_pieces.append(captured_piece)

        return in_check

    def has_legal_moves(self, color):

        pieces = (
            self.white_pieces
            if color == "white"
            else self.black_pieces
        )

        for piece in pieces:

            for row in range(8):

                for col in range(8):

                    target = self.get_piece_at(row, col)

                    if target is not None:

                        if target.color == color:
                            continue

                    if piece.obj == "Pawn":

                        valid = self.valid_pawn_move(
                            piece,
                            row,
                            col
                        )

                    else:

                        valid = piece.valid_move(row, col)

                    if not valid:
                        continue

                    blocked = False

                    if piece.obj in ["Rook", "Bishop", "Queen"]:

                        blocked = self.is_path_blocked(
                            piece.row,
                            piece.col,
                            row,
                            col
                        )

                    if blocked:
                        continue

                    illegal = self.move_puts_king_in_check(
                        piece,
                        row,
                        col
                    )

                    if not illegal:
                        return True

        return False

    def is_checkmate(self, color):

        return (
            self.is_in_check(color)
            and
            not self.has_legal_moves(color)
        )

    def is_stalemate(self, color):

        return (
            not self.is_in_check(color)
            and
            not self.has_legal_moves(color)
        )

    def can_castle(self, king, rook):

        if king.has_moved or rook.has_moved:
            return False

        if self.is_in_check(king.color):
            return False

        direction = 1 if rook.col > king.col else -1

        current_col = king.col + direction

        while current_col != rook.col:

            if self.get_piece_at(king.row, current_col) is not None:
                return False

            current_col += direction

        for i in range(1, 3):

            test_col = king.col + direction * i

            if self.move_puts_king_in_check(
                king,
                king.row,
                test_col
            ):
                return False

        return True
    
    def can_en_passant(self, pawn, new_row, new_col):

        if self.last_move is None:
            return False

        last_piece, old_row, old_col, row, col = self.last_move

        if last_piece.obj != "Pawn":
            return False

        if last_piece.color == pawn.color:
            return False

        if abs(old_row - row) != 2:
            return False

        if row != pawn.row:
            return False

        if abs(col - pawn.col) != 1:
            return False

        direction = -1 if pawn.color == "white" else 1

        return (
            new_row == pawn.row + direction
            and
            new_col == col
        )

    def draw_promotion_menu(self, win):

        if self.promoting_pawn is None:
            return

        menu_x = 620
        menu_y = 50

        pygame.draw.rect(
            win,
            (40, 40, 40),
            (menu_x, menu_y, 100, 320)
        )

        color = self.promoting_pawn.color

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
                menu_y + i * 75
            )
    def handle_promotion_click(self, mouse_x, mouse_y):

        menu_x = 620
        menu_y = 50

        if not (
            menu_x <= mouse_x <= menu_x + 100
        ):
            return

        option = (mouse_y - menu_y) // 75

        if option not in [0, 1, 2, 3]:
            return

        pawn = self.promoting_pawn

        if pawn.color == "white":
            pieces = self.white_pieces
        else:
            pieces = self.black_pieces

        row = pawn.row
        col = pawn.col
        color = pawn.color

        pieces.remove(pawn)

        if option == 0:
            pieces.append(Queen(row, col, color))

        elif option == 1:
            pieces.append(Rook(row, col, color))

        elif option == 2:
            pieces.append(Bishop(row, col, color))

        elif option == 3:
            pieces.append(Knight(row, col, color))

        self.promoting_pawn = None