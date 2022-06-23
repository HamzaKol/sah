import pygame
import os

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Azere lezi dole!")

SQUARE = pygame.Rect(0, 0, 75, 75)
squares = []


for i in range(8):
    red = []
    for j in range(8):
        red.append(pygame.Rect(i*75, j*75, 75, 75))
    squares.append(red)

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


def ally_colision(self, x, y):
    if self.color == 'white':
        for objekat in bijeli:
            if objekat.x == x and objekat.y == y:
                return objekat
    else:
        for objekat in crni:
            if objekat.x == x and objekat.y == y:
                return objekat
    return 'None'

def enemy_colision(self, x, y):
    if self.color == 'black':
        for objekat in bijeli:
            if objekat.x == x and objekat.y == y:
                return objekat
    else:
        for objekat in crni:
            if objekat.x == x and objekat.y == y:
                return objekat
    return 'None'


class Pawn:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.starix = x
        self.stariy = y
        if color == 'white':
            self.color = 'white'
            self.object = White_Pawn
        else:
            self.color = 'black'
            self.object = Black_Pawn

    def draw(self, win):
        win.blit(self.object, (self.x, self.y))

    def move(self):
        if self.color == "white":
            if ((self.stariy - 77.5) <= self.y + 37.5 <= (self.stariy + 2.5)) and (
                    self.starix - 77.5 <= self.x + 37.5 <= self.starix - 2.5):
                if(enemy_colision(self, self.starix - 75, self.stariy - 75) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix - 75, self.stariy - 75)
                    crni.pop(crni.index(za_brisanje))
                    self.x = self.starix - 75
                    self.y = self.stariy - 75
                    self.starix = self.starix - 75
                    self.stariy = self.stariy - 75
                    return True
                self.x = self.starix
                self.y = self.stariy
                return False
            if ((self.stariy - 77.5) <= self.y + 37.5 <= (self.stariy + 2.5)) and (
                    self.starix + 72.5 <= self.x + 37.5 <= self.starix + 147.5):
                if(enemy_colision(self, self.starix + 75, self.stariy - 75) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix + 75, self.stariy - 75)
                    crni.pop(crni.index(za_brisanje))
                    self.x = self.starix + 75
                    self.y = self.stariy - 75
                    self.starix = self.starix + 75
                    self.stariy = self.stariy - 75
                    return True
                self.x = self.starix
                self.y = self.stariy
                return False
            if self.stariy == 452.5:
                if ((self.stariy - 152.5) <= self.y + 37.5 <= (self.stariy - 72.5)) and (
                        self.starix - 2.5 <= self.x + 37.5 <= self.starix + 72.5):
                    if(ally_colision(self, self.starix, self.stariy - 150) != 'None' or enemy_colision(self, self.starix, self.stariy - 150) != 'None'):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    if (ally_colision(self, self.starix, self.stariy - 75) != 'None' or enemy_colision(self, self.starix,
                                                                                              self.stariy - 75) != 'None'):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    self.x = self.starix
                    self.y = self.stariy - 150
                    self.starix = self.x
                    self.stariy = self.y
                    return True
                elif (self.stariy - 75 <= self.y + 37.5 <= self.stariy) and (
                        self.starix - 2.5 <= self.x + 37.5 <= self.starix + 72.5):
                    if (ally_colision(self, self.starix, self.stariy - 75) != 'None' or enemy_colision(self, self.starix,
                                                                                              self.stariy - 75) != 'None'):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    self.x = self.starix
                    self.y = self.stariy - 75
                    self.starix = self.x
                    self.stariy = self.y
                    return True
                else:
                    self.x = self.starix
                    self.y = self.stariy
                    return False
            else:
                if (self.stariy - 77.5 <= self.y + 37.5 <= self.stariy + 2.5) and (
                        self.starix - 2.5 <= self.x + 37.5 <= self.starix + 72.5):
                    if (ally_colision(self, self.starix, self.stariy - 75) != 'None' or enemy_colision(self, self.starix,
                                                                                              self.stariy - 75) != 'None'):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    self.x = self.starix
                    self.y = self.stariy - 75
                    self.starix = self.x
                    self.stariy = self.y
                    return True
                else:
                    self.x = self.starix
                    self.y = self.stariy
                    return False
        else:
            if ((self.stariy + 2.5) <= self.y + 37.5 <= (self.stariy + 77.5)) and (
                    self.starix + 72.5 <= self.x + 37.5 <= self.starix + 147.5):
                if(enemy_colision(self, self.starix + 75, self.stariy + 75) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix + 75, self.stariy + 75)
                    bijeli.pop(bijeli.index(za_brisanje))
                    self.x = self.starix + 75
                    self.y = self.stariy + 75
                    self.starix = self.starix + 75
                    self.stariy = self.stariy + 75
                    return True
                self.x = self.starix
                self.y = self.stariy
                return False
            if ((self.stariy + 2.5) <= self.y + 37.5 <= (self.stariy + 77.5)) and (
                    self.starix - 2.5 <= self.x + 37.5 <= self.starix - 77.5):
                if(enemy_colision(self, self.starix - 75, self.stariy + 75) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix - 75, self.stariy + 75)
                    bijeli.pop(bijeli.index(za_brisanje))
                    self.x = self.starix - 75
                    self.y = self.stariy + 75
                    self.starix = self.starix - 75
                    self.stariy = self.stariy + 75
                    return True
                self.x = self.starix
                self.y = self.stariy
                return False
            if self.stariy == 77.5:
                if ((self.stariy + 147.5) <= self.y + 37.5 <= (self.stariy + 222.5)) and (
                        self.starix - 2.5 <= self.x + 37.5 <= self.starix + 72.5):
                    if (ally_colision(self, self.starix, self.stariy + 150) != 'None' or enemy_colision(self, self.starix,
                                                                                              self.stariy + 150) != 'None'):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    if (ally_colision(self, self.starix, self.stariy + 75) != 'None' or enemy_colision(self, self.starix,
                                                                                              self.stariy + 75) != 'None'):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    self.x = self.starix
                    self.y = self.stariy + 150
                    self.starix = self.x
                    self.stariy = self.y
                    return True
                elif (self.stariy + 72.5 <= self.y + 37.5 <= self.stariy + 147.5) and (
                        self.starix - 2.5 <= self.x + 37.5 <= self.starix + 72.5):
                    if (ally_colision(self, self.starix, self.stariy + 75) != 'None' or enemy_colision(self, self.starix,
                                                                                              self.stariy + 75) != 'None'):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    self.x = self.starix
                    self.y = self.stariy + 75
                    self.starix = self.x
                    self.stariy = self.y
                    return True
                else:
                    self.x = self.starix
                    self.y = self.stariy
                    return False
            else:
                if (self.stariy + 72.5 <= self.y + 37.5 <= self.stariy + 147.5) and (
                        self.starix - 2.5 <= self.x + 37.5 <= self.starix + 72.5):
                    if (ally_colision(self, self.starix, self.stariy + 75) != 'None' or enemy_colision(self, self.starix,
                                                                                              self.stariy + 75) != 'None'):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    self.x = self.starix
                    self.y = self.stariy + 75
                    self.starix = self.x
                    self.stariy = self.y
                    return True
                else:
                    self.x = self.starix
                    self.y = self.stariy
                    return False

class Knight:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.starix = x
        self.stariy = y
        if color == 'white':
            self.color = 'white'
            self.object = White_Knight
        else:
            self.color = 'black'
            self.object = Black_Knight

    def draw(self, win):
        win.blit(self.object, (self.x, self.y))

    def move(self):
        if ((self.stariy - 152.5) <= self.y + 37.5 <= (self.stariy - 72.5)):
            if (self.starix +72.5 <= self.x + 37.5 <= self.starix + 147.5):
                if (ally_colision(self, self.starix + 75, self.stariy - 150) != 'None'):
                    self.x = self.starix
                    self.y = self.stariy
                    return False
                if (enemy_colision(self, self.starix + 75, self.stariy - 150) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix + 75, self.stariy - 150)
                    if self.color == 'white':
                        crni.pop(crni.index(za_brisanje))
                    else:
                        bijeli.pop(bijeli.index(za_brisanje))
                self.x = self.starix + 75
                self.y = self.stariy - 150
                self.starix = self.x
                self.stariy = self.y
                return True

            elif (self.starix - 77.5 <= self.x + 37.5 <= self.starix - 2.5):
                if (ally_colision(self, self.starix - 75, self.stariy - 150) != 'None'):
                    self.x = self.starix
                    self.y = self.stariy
                    return False
                if (enemy_colision(self, self.starix - 75, self.stariy - 150) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix - 75, self.stariy - 150)
                    if self.color == 'white':
                        crni.pop(crni.index(za_brisanje))
                    else:
                        bijeli.pop(bijeli.index(za_brisanje))
                self.x = self.starix - 75
                self.y = self.stariy - 150
                self.starix = self.x
                self.stariy = self.y
                return True
            else:
                self.x = self.starix
                self.y = self.stariy
                return False
        elif((self.stariy + 147.5) <= self.y + 37.5 <= (self.stariy + 222.5)):
            if (self.starix + 72.5 <= self.x + 37.5 <= self.starix + 147.5):
                if (ally_colision(self, self.starix + 75, self.stariy + 150) != 'None'):
                    self.x = self.starix
                    self.y = self.stariy
                    return False
                if (enemy_colision(self, self.starix + 75, self.stariy + 150) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix + 75, self.stariy + 150)
                    if self.color == 'white':
                        crni.pop(crni.index(za_brisanje))
                    else:
                        bijeli.pop(bijeli.index(za_brisanje))
                self.x = self.starix + 75
                self.y = self.stariy + 150
                self.starix = self.x
                self.stariy = self.y
                return True
            elif (self.starix - 77.5 <= self.x + 37.5 <= self.starix - 2.5):
                if (ally_colision(self, self.starix - 75, self.stariy + 150) != 'None'):
                    self.x = self.starix
                    self.y = self.stariy
                    return False
                if (enemy_colision(self, self.starix - 75, self.stariy + 150) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix - 75, self.stariy + 150)
                    if self.color == 'white':
                        crni.pop(crni.index(za_brisanje))
                    else:
                        bijeli.pop(bijeli.index(za_brisanje))
                self.x = self.starix - 75
                self.y = self.stariy + 150
                self.starix = self.x
                self.stariy = self.y
                return True
            else:
                self.x = self.starix
                self.y = self.stariy
                return False
        elif (self.starix + 147.5 <= self.x + 37.5 <= self.starix + 222.5):
            if (self.stariy - 77.5 <= self.y + 37.5 <= self.stariy + 2.5):
                if (ally_colision(self, self.starix + 150, self.stariy - 75) != 'None'):
                    self.x = self.starix
                    self.y = self.stariy
                    return False
                if (enemy_colision(self, self.starix + 150, self.stariy - 75) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix + 150, self.stariy - 75)
                    if self.color == 'white':
                        crni.pop(crni.index(za_brisanje))
                    else:
                        bijeli.pop(bijeli.index(za_brisanje))
                self.x = self.starix + 150
                self.y = self.stariy - 75
                self.starix = self.x
                self.stariy = self.y
                return True
            elif (self.stariy + 72.5 <= self.y + 37.5 <= self.stariy + 147.5):
                if (ally_colision(self, self.starix + 150, self.stariy + 75) != 'None'):
                    self.x = self.starix
                    self.y = self.stariy
                    return False
                if (enemy_colision(self, self.starix + 150, self.stariy + 75) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix + 150, self.stariy + 75)
                    if self.color == 'white':
                        crni.pop(crni.index(za_brisanje))
                    else:
                        bijeli.pop(bijeli.index(za_brisanje))
                self.x = self.starix + 150
                self.y = self.stariy + 75
                self.starix = self.x
                self.stariy = self.y
                return True
            else:
                self.x = self.starix
                self.y = self.stariy
                return False



        elif (self.starix - 152.5 <= self.x + 37.5 <= self.starix + 77.5):
            if (self.stariy - 77.5 <= self.y + 37.5 <= self.stariy + 2.5):
                if (ally_colision(self, self.starix - 150, self.stariy - 75) != 'None'):
                    self.x = self.starix
                    self.y = self.stariy
                    return False
                if (enemy_colision(self, self.starix - 150, self.stariy - 75) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix - 150, self.stariy - 75)
                    if self.color == 'white':
                        crni.pop(crni.index(za_brisanje))
                    else:
                        bijeli.pop(bijeli.index(za_brisanje))
                self.x = self.starix - 150
                self.y = self.stariy - 75
                self.starix = self.x
                self.stariy = self.y
                return True
            elif (self.stariy + 72.5 <= self.y + 37.5 <= self.stariy + 147.5):
                if (ally_colision(self, self.starix - 150, self.stariy + 75) != 'None'):
                    self.x = self.starix
                    self.y = self.stariy
                    return False
                if (enemy_colision(self, self.starix - 150, self.stariy + 75) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix - 150, self.stariy + 75)
                    if self.color == 'white':
                        crni.pop(crni.index(za_brisanje))
                    else:
                        bijeli.pop(bijeli.index(za_brisanje))
                self.x = self.starix - 150
                self.y = self.stariy + 75
                self.starix = self.x
                self.stariy = self.y
                return True
            else:
                self.x = self.starix
                self.y = self.stariy
                return False
        else:
            self.x = self.starix
            self.y = self.stariy
            return False



class Bishop:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.starix = x
        self.stariy = y
        if color == 'white':
            self.color = 'white'
            self.object = White_Bishop
        else:
            self.color = 'black'
            self.object = Black_Bishop

    def draw(self, win):
        win.blit(self.object, (self.x, self.y))
    def move(self):

        novix = self.starix
        noviy = self.stariy
        for i in range(7):
            if (ally_colision(self, novix - 75, noviy - 75) != 'None'):
                break
            if(noviy - 77.5 <= self.y + 37.5 <= noviy - 2.5):
                if(novix - 77.5 <= self.x + 37.5 <= novix - 2.5):
                    if (ally_colision(self, novix + 75, noviy + 75) != 'None'):
                        break
                    if (enemy_colision(self, novix - 75, noviy - 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix - 75, noviy - 75)
                        if(self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix - 75
                    self.y = noviy - 75
                    self.starix = novix - 75
                    self.stariy = noviy - 75
                    return True
            novix -= 75
            noviy -= 75
        novix = self.starix
        noviy = self.stariy
        for i in range(7):
            if (ally_colision(self, novix + 75, noviy - 75) != 'None'):
                break
            if (noviy - 77.5 <= self.y + 37.5 <= noviy - 2.5):
                if(novix + 72.5 <= self.x + 37.5 <= novix + 147.5):
                    if (ally_colision(self, novix + 75, noviy + 75) != 'None'):
                        break
                    if (enemy_colision(self, novix + 75, noviy - 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix + 75, noviy - 75)
                        if(self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix + 75
                    self.y = noviy - 75
                    self.starix = novix + 75
                    self.stariy = noviy - 75
                    return True
            novix += 75
            noviy -= 75
        novix = self.starix
        noviy = self.stariy
        for i in range(7):
            if (ally_colision(self, novix - 75, noviy + 75) != 'None'):
                break
            if (noviy + 72.5 <= self.y + 37.5 <= noviy + 147.5):
                if (novix - 77.5 <= self.x + 37.5 <= novix - 2.5):
                    if (ally_colision(self, novix + 75, noviy + 75) != 'None'):
                        break
                    if (enemy_colision(self, novix - 75, noviy + 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix - 75, noviy + 75)
                        if(self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix - 75
                    self.y = noviy + 75
                    self.starix = novix - 75
                    self.stariy = noviy + 75
                    return True
            novix -= 75
            noviy += 75
        novix = self.starix
        noviy = self.stariy
        for i in range(7):
            if (ally_colision(self, novix + 75, noviy + 75) != 'None'):
                break
            if (noviy + 72.5 <= self.y + 37.5 <= noviy + 147.5):
                if (novix + 72.5 <= self.x + 37.5 <= novix + 147.5):
                    if (ally_colision(self, novix + 75, noviy + 75) != 'None'):
                        break
                    if (enemy_colision(self, novix + 75, noviy + 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix + 75, noviy + 75)
                        if(self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix + 75
                    self.y = noviy + 75
                    self.starix = novix + 75
                    self.stariy = noviy + 75
                    return True
            novix += 75
            noviy += 75
        self.x = self.starix
        self.y = self.stariy
        return False




class Rook:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.starix = x
        self.stariy = y
        if color == 'white':
            self.color = 'white'
            self.object = White_Rook
        else:
            self.color = 'black'
            self.object = Black_Rook

    def draw(self, win):
        win.blit(self.object, (self.x, self.y))

    def move(self):
        noviy = self.stariy
        novix = self.starix
        for i in range(7):
            if (ally_colision(self, novix, noviy - 75) != 'None'):
                break
            if (noviy - 77.5 <= self.y + 37.5 <= noviy - 2.5):
                if (novix - 2.5 <= self.x + 37.5 <= novix + 72.5):
                    if (ally_colision(self, novix, noviy - 75) != 'None'):
                        break
                    if (enemy_colision(self, novix, noviy - 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix, noviy - 75)
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix
                    self.y = noviy - 75
                    self.starix = novix
                    self.stariy = noviy - 75
                    return True
            noviy -= 75
        noviy = self.stariy

        for i in range(7):
            if (ally_colision(self, novix, noviy + 75) != 'None'):
                break
            if (noviy + 72.5 <= self.y + 37.5 <= noviy + 147.5):
                if (novix - 2.5 <= self.x + 37.5 <= novix + 72.5):
                    if (ally_colision(self, novix, noviy + 75) != 'None'):
                        break
                    if (enemy_colision(self, novix, noviy + 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix, noviy + 75)
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix
                    self.y = noviy + 75
                    self.starix = novix
                    self.stariy = noviy + 75
                    return True
            noviy += 75
        noviy = self.stariy

        for i in range(7):
            if (ally_colision(self, novix  - 75, noviy) != 'None'):
                break
            if(novix - 77.5 <= self.x + 37.5 <= novix - 2.5):
                if (noviy - 2.5 <= self.y + 37.5 <= noviy + 72.5):
                    if (ally_colision(self, novix - 75, noviy) != 'None'):
                        break
                    if (enemy_colision(self, novix - 75, noviy) != 'None'):
                        za_brisanje = enemy_colision(self, novix - 75, noviy)
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix - 75
                    self.y = noviy
                    self.starix = novix - 75
                    self.stariy = noviy
                    return True
            novix -= 75
        novix = self.starix

        for i in range(7):
            if (ally_colision(self, novix  + 75, noviy) != 'None'):
                break
            if(novix + 72.5 <= self.x + 37.5 <= novix + 147.5):
                if (noviy - 2.5 <= self.y + 37.5 <= noviy + 72.5):
                    if (ally_colision(self, novix + 75, noviy) != 'None'):
                        break
                    if (enemy_colision(self, novix + 75, noviy) != 'None'):
                        za_brisanje = enemy_colision(self, novix + 75, noviy)
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix + 75
                    self.y = noviy
                    self.starix = novix + 75
                    self.stariy = noviy
                    return True
            novix += 75

        self.x = self.starix
        self.y = self.stariy
        return False


class Queen:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.starix = x
        self.stariy = y
        if color == 'white':
            self.color = 'white'
            self.object = White_Queen
        else:
            self.color = 'black'
            self.object = Black_Queen

    def draw(self, win):
        win.blit(self.object, (self.x, self.y))

    def move(self):
        noviy = self.stariy
        novix = self.starix
        for i in range(7):
            if (ally_colision(self, novix, noviy - 75) != 'None'):
                break
            if (noviy - 77.5 <= self.y + 37.5 <= noviy - 2.5):
                if (novix - 2.5 <= self.x + 37.5 <= novix + 72.5):
                    if (ally_colision(self, novix, noviy - 75) != 'None'):
                        break
                    if (enemy_colision(self, novix, noviy - 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix, noviy - 75)
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix
                    self.y = noviy - 75
                    self.starix = novix
                    self.stariy = noviy - 75
                    return True
            noviy -= 75
        noviy = self.stariy

        for i in range(7):
            if (ally_colision(self, novix, noviy + 75) != 'None'):
                break
            if (noviy + 72.5 <= self.y + 37.5 <= noviy + 147.5):
                if (novix - 2.5 <= self.x + 37.5 <= novix + 72.5):
                    if (ally_colision(self, novix, noviy + 75) != 'None'):
                        break
                    if (enemy_colision(self, novix, noviy + 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix, noviy + 75)
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix
                    self.y = noviy + 75
                    self.starix = novix
                    self.stariy = noviy + 75
                    return True
            noviy += 75
        noviy = self.stariy

        for i in range(7):
            if (ally_colision(self, novix - 75, noviy) != 'None'):
                break
            if (novix - 77.5 <= self.x + 37.5 <= novix - 2.5):
                if (noviy - 2.5 <= self.y + 37.5 <= noviy + 72.5):
                    if (ally_colision(self, novix - 75, noviy) != 'None'):
                        break
                    if (enemy_colision(self, novix - 75, noviy) != 'None'):
                        za_brisanje = enemy_colision(self, novix - 75, noviy)
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix - 75
                    self.y = noviy
                    self.starix = novix - 75
                    self.stariy = noviy
                    return True
            novix -= 75
        novix = self.starix

        for i in range(7):
            if (ally_colision(self, novix + 75, noviy) != 'None'):
                break
            if (novix + 72.5 <= self.x + 37.5 <= novix + 147.5):
                if (noviy - 2.5 <= self.y + 37.5 <= noviy + 72.5):
                    if (ally_colision(self, novix + 75, noviy) != 'None'):
                        break
                    if (enemy_colision(self, novix + 75, noviy) != 'None'):
                        za_brisanje = enemy_colision(self, novix + 75, noviy)
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix + 75
                    self.y = noviy
                    self.starix = novix + 75
                    self.stariy = noviy
                    return True
            novix += 75
        novix = self.starix
        noviy = self.stariy
        for i in range(7):
            if (ally_colision(self, novix - 75, noviy - 75) != 'None'):
                break
            if (noviy - 77.5 <= self.y + 37.5 <= noviy - 2.5):
                if (novix - 77.5 <= self.x + 37.5 <= novix - 2.5):
                    if (ally_colision(self, novix + 75, noviy + 75) != 'None'):
                        break
                    if (enemy_colision(self, novix - 75, noviy - 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix - 75, noviy - 75)
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix - 75
                    self.y = noviy - 75
                    self.starix = novix - 75
                    self.stariy = noviy - 75
                    return True
            novix -= 75
            noviy -= 75
        novix = self.starix
        noviy = self.stariy
        for i in range(7):
            if (ally_colision(self, novix + 75, noviy - 75) != 'None'):
                break
            if (noviy - 77.5 <= self.y + 37.5 <= noviy - 2.5):
                if (novix + 72.5 <= self.x + 37.5 <= novix + 147.5):
                    if (ally_colision(self, novix + 75, noviy + 75) != 'None'):
                        break
                    if (enemy_colision(self, novix + 75, noviy - 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix + 75, noviy - 75)
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix + 75
                    self.y = noviy - 75
                    self.starix = novix + 75
                    self.stariy = noviy - 75
                    return True
            novix += 75
            noviy -= 75
        novix = self.starix
        noviy = self.stariy
        for i in range(7):
            if (ally_colision(self, novix - 75, noviy + 75) != 'None'):
                break
            if (noviy + 72.5 <= self.y + 37.5 <= noviy + 147.5):
                if (novix - 77.5 <= self.x + 37.5 <= novix - 2.5):
                    if (ally_colision(self, novix + 75, noviy + 75) != 'None'):
                        break
                    if (enemy_colision(self, novix - 75, noviy + 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix - 75, noviy + 75)
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix - 75
                    self.y = noviy + 75
                    self.starix = novix - 75
                    self.stariy = noviy + 75
                    return True
            novix -= 75
            noviy += 75
        novix = self.starix
        noviy = self.stariy
        for i in range(7):
            if (ally_colision(self, novix + 75, noviy + 75) != 'None'):
                break
            if (noviy + 72.5 <= self.y + 37.5 <= noviy + 147.5):
                if (novix + 72.5 <= self.x + 37.5 <= novix + 147.5):
                    if (ally_colision(self, novix + 75, noviy + 75) != 'None'):
                        break
                    if (enemy_colision(self, novix + 75, noviy + 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix + 75, noviy + 75)
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix + 75
                    self.y = noviy + 75
                    self.starix = novix + 75
                    self.stariy = noviy + 75
                    return True
            novix += 75
            noviy += 75
        self.x = self.starix
        self.y = self.stariy
        return False


class King:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.starix = x
        self.stariy = y
        if color == 'white':
            self.color = 'white'
            self.object = White_King
        else:
            self.color = 'black'
            self.object = Black_King

    def draw(self, win):
        win.blit(self.object, (self.x, self.y))

    def move(self):
        if (self.stariy - 77.5 <= self.y + 37.5 <= self.stariy + 2.5) and (
                self.starix - 2.5 <= self.x + 37.5 <= self.starix + 72.5):
            if (ally_colision(self, self.starix, self.stariy - 75) != 'None'):
                self.x = self.starix
                self.y = self.stariy
                return False
            if (enemy_colision(self, self.starix, self.stariy - 75) != 'None'):
                za_brisanje = enemy_colision(self, self.starix, self.stariy - 75)
                if (self.color == 'white'):
                    crni.pop(crni.index(za_brisanje))
                else:
                    bijeli.pop(bijeli.index(za_brisanje))
            self.x = self.starix
            self.y = self.stariy - 75
            self.starix = self.x
            self.stariy = self.y
            return True
        elif (self.stariy + 72.5 <= self.y + 37.5 <= self.stariy + 147.5) and (
                        self.starix - 2.5 <= self.x + 37.5 <= self.starix + 72.5):
            if (ally_colision(self, self.starix, self.stariy + 75) != 'None'):
                self.x = self.starix
                self.y = self.stariy
                return False
            if (enemy_colision(self, self.starix, self.stariy + 75) != 'None'):
                za_brisanje = enemy_colision(self, self.starix, self.stariy + 75)
                if (self.color == 'white'):
                    crni.pop(crni.index(za_brisanje))
                else:
                    bijeli.pop(bijeli.index(za_brisanje))
            self.x = self.starix
            self.y = self.stariy + 75
            self.starix = self.x
            self.stariy = self.y
            return True
        elif (self.starix - 77.5 <= self.x + 37.5 <= self.starix - 2.5) and (
                        self.stariy - 2.5 <= self.y + 37.5 <= self.stariy + 72.5):
            if (ally_colision(self, self.starix - 75, self.stariy) != 'None'):
                self.x = self.starix
                self.y = self.stariy
                return False
            if (enemy_colision(self, self.starix - 75, self.stariy) != 'None'):
                za_brisanje = enemy_colision(self, self.starix - 75, self.stariy)
                if (self.color == 'white'):
                    crni.pop(crni.index(za_brisanje))
                else:
                    bijeli.pop(bijeli.index(za_brisanje))
            self.x = self.starix - 75
            self.y = self.stariy
            self.starix = self.x
            self.stariy = self.y
            return True
        elif (self.starix + 72.5 <= self.x + 37.5 <= self.starix + 147.5) and (
                        self.stariy - 2.5 <= self.y + 37.5 <= self.stariy + 72.5):
            if (ally_colision(self, self.starix + 75, self.stariy) != 'None'):
                self.x = self.starix
                self.y = self.stariy
                return False
            if (enemy_colision(self, self.starix + 75, self.stariy) != 'None'):
                za_brisanje = enemy_colision(self, self.starix + 75, self.stariy)
                if (self.color == 'white'):
                    crni.pop(crni.index(za_brisanje))
                else:
                    bijeli.pop(bijeli.index(za_brisanje))
            self.x = self.starix + 75
            self.y = self.stariy
            self.starix = self.x
            self.stariy = self.y
            return True
        elif (self.stariy - 77.5 <= self.y + 37.5 <= self.stariy + 2.5) and (self.starix - 77.5 <= self.x + 37.5 <= self.starix - 2.5):
            if (ally_colision(self, self.starix - 75, self.stariy - 75) != 'None'):
                self.x = self.starix
                self.y = self.stariy
                return False
            if (enemy_colision(self, self.starix - 75, self.stariy - 75) != 'None'):
                za_brisanje = enemy_colision(self, self.starix - 75, self.stariy - 75)
                if (self.color == 'white'):
                    crni.pop(crni.index(za_brisanje))
                else:
                    bijeli.pop(bijeli.index(za_brisanje))
            self.x = self.starix - 75
            self.y = self.stariy - 75
            self.starix = self.x
            self.stariy = self.y
            return True
        elif (self.stariy - 77.5 <= self.y + 37.5 <= self.stariy + 2.5) and (self.starix + 72.5 <= self.x + 37.5 <= self.starix + 147.5):
            if (ally_colision(self, self.starix + 75, self.stariy - 75) != 'None'):
                self.x = self.starix
                self.y = self.stariy
                return False
            if (enemy_colision(self, self.starix + 75, self.stariy - 75) != 'None'):
                za_brisanje = enemy_colision(self, self.starix + 75, self.stariy - 75)
                if (self.color == 'white'):
                    crni.pop(crni.index(za_brisanje))
                else:
                    bijeli.pop(bijeli.index(za_brisanje))
            self.x = self.starix + 75
            self.y = self.stariy - 75
            self.starix = self.x
            self.stariy = self.y
            return True
        elif (self.stariy + 72.5 <= self.y + 37.5 <= self.stariy + 147.5) and (self.starix - 77.5 <= self.x + 37.5 <= self.starix - 2.5):
            if (ally_colision(self, self.starix - 75, self.stariy + 75) != 'None'):
                self.x = self.starix
                self.y = self.stariy
                return False
            if (enemy_colision(self, self.starix - 75, self.stariy + 75) != 'None'):
                za_brisanje = enemy_colision(self, self.starix - 75, self.stariy + 75)
                if (self.color == 'white'):
                    crni.pop(crni.index(za_brisanje))
                else:
                    bijeli.pop(bijeli.index(za_brisanje))
            self.x = self.starix - 75
            self.y = self.stariy + 75
            self.starix = self.x
            self.stariy = self.y
            return True
        elif (self.stariy + 72.5 <= self.y + 37.5 <= self.stariy + 147.5) and (self.starix + 72.5 <= self.x + 37.5 <= self.starix + 147.5):
            if (ally_colision(self, self.starix + 75, self.stariy + 75) != 'None'):
                self.x = self.starix
                self.y = self.stariy
                return False
            if (enemy_colision(self, self.starix + 75, self.stariy + 75) != 'None'):
                za_brisanje = enemy_colision(self, self.starix + 75, self.stariy + 75)
                if (self.color == 'white'):
                    crni.pop(crni.index(za_brisanje))
                else:
                    bijeli.pop(bijeli.index(za_brisanje))
            self.x = self.starix + 75
            self.y = self.stariy + 75
            self.starix = self.x
            self.stariy = self.y
            return True
        else:
            self.x = self.starix
            self.y = self.stariy
            return False

    def Check(self):
        if self.color == "white":
            for objekat in crni:
                if type(objekat) == Pawn:
                    if type(enemy_colision(objekat, objekat.starix + 75, objekat.stariy + 75)) == King:
                        return True
                    if type(enemy_colision(objekat, objekat.starix - 75, objekat.stariy + 75)) == King:
                        return True
                if type(objekat) == Bishop:
                    novix = self.starix
                    noviy = self.stariy
                    for i in range(7):
                        if type(ally_colision(objekat, novix + 75, noviy + 75)) != 'None':
                            break
                        if type(enemy_colision(objekat, novix + 75, noviy + 75)) == King:
                            return True
                        novix += 75
                        noviy += 75
                    novix = self.starix
                    noviy = self.stariy
                    for i in range(7):
                        if type(ally_colision(objekat, novix - 75, noviy + 75)) != 'None':
                            break
                        if type(enemy_colision(objekat, novix - 75, noviy + 75)) == King:
                            return True
                        novix -= 75
                        noviy += 75
                    novix = self.starix
                    noviy = self.stariy
                    for i in range(7):
                        if type(ally_colision(objekat, novix + 75, noviy - 75)) != 'None':
                            break
                        if type(enemy_colision(objekat, novix + 75, noviy - 75)) == King:
                            return True
                        novix += 75
                        noviy -= 75
                    novix = self.starix
                    noviy = self.stariy
                    for i in range(7):
                        if type(ally_colision(objekat, novix - 75, noviy - 75)) != 'None':
                            break
                        if type(enemy_colision(objekat, novix - 75, noviy - 75)) == King:
                            return True
                        novix -= 75
                        noviy -= 75
            return False

        else:
            pass



bijeli = []
crni = []


bijeli.append(King(2.5 + 300, 2.5 + 525, 'white'))
crni.append(King(2.5 + 300, 2.5, 'black'))

for i in range(8):
    bijeli.append(Pawn(2.5 + i*75, 450 + 2.5, 'white'))

for i in range(8):
    crni.append(Pawn(2.5 + i*75, 75 + 2.5, 'black'))


bijeli.append(Knight(2.5 + 75, 2.5 + 525, 'white'))
bijeli.append(Knight(2.5 + 75 + 375, 2.5 + 525, 'white'))


crni.append(Knight(2.5 + 75, 2.5, 'black'))
crni.append(Knight(2.5 + 75 + 375, 2.5, 'black'))


bijeli.append(Bishop(2.5 + 150, 2.5 + 525, 'white'))
bijeli.append(Bishop(2.5 + 375, 2.5 + 525, 'white'))


crni.append(Bishop(2.5 + 150, 2.5, 'black'))
crni.append(Bishop(2.5 + 375, 2.5, 'black'))



bijeli.append(Rook(2.5, 2.5 + 525, 'white'))
bijeli.append(Rook(2.5 + 525, 2.5 + 525, 'white'))


crni.append(Rook(2.5, 2.5, 'black'))
crni.append(Rook(2.5 + 525, 2.5, 'black'))

bijeli.append(Queen(2.5 + 225, 2.5 + 525, 'white'))
crni.append(Queen(2.5 + 225, 2.5, 'black'))



def draw_window():
    WIN.fill(WHITE)
    for i in range(len(squares)):
        for j in range(8):
            if (i+j) % 2 == 0:
                pygame.draw.rect(WIN, WHITE, squares[i][j])
            else:
                pygame.draw.rect(WIN, BLUE, squares[i][j])

    for objekat in bijeli:
        objekat.draw(WIN)
    for objekat in crni:
        objekat.draw(WIN)
    pygame.display.update()




def main():
    potez = 1
    clock = pygame.time.Clock()
    run = True
    pressed = False
    objekat = "None"
    while run:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed = True
                x, y = pygame.mouse.get_pos()
                if(potez % 2 == 1):
                    for piece in bijeli:
                        if (piece.x - 2.5 < x < piece.x + 72.5 and piece.y - 2.5 < y < piece.y + 72.5):
                            objekat = piece
                            break
                else:
                    for piece in crni:
                        if (piece.x - 2.5 < x < piece.x + 72.5 and piece.y - 2.5 < y < piece.y + 72.5):
                            objekat = piece
                            break
            if event.type == pygame.MOUSEMOTION:
                mouseMove = event.rel
                if pressed == True and objekat != "None":
                    objekat.x += mouseMove[0]
                    objekat.y += mouseMove[1]
            if event.type == pygame.MOUSEBUTTONUP:
                pressed = False
                if objekat != "None":
                    if(potez%2 == 1):
                        if bijeli[0].Check() == False:
                            print(bijeli[0].Check())
                            moved = objekat.move()
                        else:
                            objekat.x = objekat.starix
                            objekat.y = objekat.stariy
                    else:
                        if crni[0].Check() == False:
                            print(bijeli[0].Check())
                            moved = objekat.move()
                        else:
                            objekat.x = objekat.starix
                            objekat.y = objekat.stariy
                    if moved:
                        potez += 1
                objekat = "None"


        draw_window()



if __name__ == "__main__":
    main()