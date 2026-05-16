import pygame

from constants import WHITE, BLUE
from pieceClasses import Pawn, Rook, Knight, Bishop, Queen, King


class ChessGame:

    def __init__(self):

        self.turn = "white"
        self.selected_piece = None

        self.game_over = False
        self.winner = None
        self.is_draw = False

        self.last_move = None

        self.promoting_pawn = None

        self.move_history = []
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

    def handle_click(self, row, col):

        if self.game_over:
            return

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

                    notation = self.create_move_notation(
                        old_row,
                        old_col,
                        row,
                        col
                    )

                    self.move_history.append(notation)

                    self.turn = (
                        "black"
                        if self.turn == "white"
                        else "white"
)

                    if self.is_checkmate(self.turn):

                        self.game_over = True

                        self.winner = (
                            "black"
                            if self.turn == "white"
                            else "white"
                        )

                    elif self.is_stalemate(self.turn):

                        self.game_over = True
                        self.is_draw = True

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

    
    def promote_pawn(self, piece_type):

        pawn = self.promoting_pawn

        if pawn is None:
            return

        if pawn.color == "white":
            pieces = self.white_pieces
        else:
            pieces = self.black_pieces

        row = pawn.row
        col = pawn.col
        color = pawn.color

        pieces.remove(pawn)

        if piece_type == "Queen":
            pieces.append(
                Queen(row, col, color)
            )

        elif piece_type == "Rook":
            pieces.append(
                Rook(row, col, color)
            )

        elif piece_type == "Bishop":
            pieces.append(
                Bishop(row, col, color)
            )

        elif piece_type == "Knight":
            pieces.append(
                Knight(row, col, color)
            )

        self.promoting_pawn = None
    
    def board_to_chess_notation(self, row, col):

        file = chr(ord('a') + col)
        rank = str(8 - row)

        return file + rank

    def create_move_notation(
        self,
        start_row,
        start_col,
        end_row,
        end_col
    ):

        start = self.board_to_chess_notation(
            start_row,
            start_col
        )

        end = self.board_to_chess_notation(
            end_row,
            end_col
        )

        return start + end
    
    def chess_to_board(self, notation):

        file = notation[0]
        rank = notation[1]

        col = ord(file) - ord('a')
        row = 8 - int(rank)

        return row, col

    def play_move(self, notation):

        start = notation[:2]
        end = notation[2:4]

        promotion_piece = None

        if len(notation) == 5:
            promotion_piece = notation[4]

        start_row, start_col = self.chess_to_board(start)
        end_row, end_col = self.chess_to_board(end)

        piece = self.get_piece_at(
            start_row,
            start_col
        )

        if piece is None:
            return False

        target = self.get_piece_at(
            end_row,
            end_col
        )

        if (
            piece.obj == "King"
            and
            abs(end_col - start_col) == 2
        ):

            if end_col > start_col:

                rook = self.get_piece_at(
                    start_row,
                    7
                )

                if rook is not None:

                    rook.col = 5
                    rook.has_moved = True

            else:

                rook = self.get_piece_at(
                    start_row,
                    0
                )

                if rook is not None:

                    rook.col = 3
                    rook.has_moved = True

        if (
            piece.obj == "Pawn"
            and
            target is None
            and
            start_col != end_col
        ):

            captured_pawn = self.get_piece_at(
                start_row,
                end_col
            )

            if captured_pawn is not None:

                if captured_pawn.color == "white":
                    self.white_pieces.remove(captured_pawn)
                else:
                    self.black_pieces.remove(captured_pawn)

        if target is not None:

            if target.color == "white":
                self.white_pieces.remove(target)
            else:
                self.black_pieces.remove(target)

        piece.row = end_row
        piece.col = end_col

        piece.has_moved = True

        if (
            piece.obj == "Pawn"
            and
            (
                end_row == 0
                or
                end_row == 7
            )
        ):

            if piece.color == "white":
                pieces = self.white_pieces
            else:
                pieces = self.black_pieces

            pieces.remove(piece)

            if promotion_piece == "r":
                pieces.append(
                    Rook(end_row, end_col, piece.color)
                )

            elif promotion_piece == "b":
                pieces.append(
                    Bishop(end_row, end_col, piece.color)
                )

            elif promotion_piece == "n":
                pieces.append(
                    Knight(end_row, end_col, piece.color)
                )

            else:

                pieces.append(
                    Queen(end_row, end_col, piece.color)
                )

        self.last_move = (
            piece,
            start_row,
            start_col,
            end_row,
            end_col
        )

        self.move_history.append(notation)

        self.turn = (
            "black"
            if self.turn == "white"
            else "white"
        )

        if self.is_checkmate(self.turn):

            self.game_over = True

            self.winner = (
                "black"
                if self.turn == "white"
                else "white"
            )

        elif self.is_stalemate(self.turn):

            self.game_over = True
            self.is_draw = True

        return True