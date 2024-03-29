# Fale:
# neki win screen nakon checkmatea,
# neki meni, mozda ljepsi izgled malo, indikator za check,
# 50 move rule
# Zvukovi
# za_brisanje = "None" dodati u checkmated

import pygame
import os

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

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

def border_colision(x, y):
    if(x<0 or y<0 or x > 600 or y > 600):
        return True
    return False

def king_checked(pieces):
    for objekat in pieces:
        if objekat.color == "white":
            if objekat.obj == "Pawn":
                if enemy_colision(objekat, objekat.x + 75, objekat.y - 75) != "None":
                    if enemy_colision(objekat, objekat.x + 75, objekat.y - 75).obj == "King":
                        return objekat
                if enemy_colision(objekat, objekat.x - 75, objekat.y - 75) != "None":
                    if enemy_colision(objekat, objekat.x - 75, objekat.y - 75).obj == "King":
                        return objekat
        else:
            if objekat.obj == "Pawn":
                if enemy_colision(objekat, objekat.x + 75, objekat.y + 75) != "None":
                    if enemy_colision(objekat, objekat.x + 75, objekat.y + 75).obj == "King":
                        return objekat
                if enemy_colision(objekat, objekat.x - 75, objekat.y + 75) != "None":
                    if enemy_colision(objekat, objekat.x - 75, objekat.y + 75).obj == "King":
                        return objekat

        if objekat.obj == "Knight":
            if enemy_colision(objekat, objekat.x + 75, objekat.y + 150) != "None":
                if enemy_colision(objekat, objekat.x + 75, objekat.y + 150).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x - 75, objekat.y + 150) != "None":
                if enemy_colision(objekat, objekat.x - 75, objekat.y + 150).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x + 75, objekat.y - 150) != "None":
                if enemy_colision(objekat, objekat.x + 75, objekat.y - 150).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x - 75, objekat.y - 150) != "None":
                if enemy_colision(objekat, objekat.x - 75, objekat.y - 150).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x + 150, objekat.y + 75) != "None":
                if enemy_colision(objekat, objekat.x + 150, objekat.y + 75).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x + 150, objekat.y - 75) != "None":
                if enemy_colision(objekat, objekat.x + 150, objekat.y - 75).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x - 150, objekat.y + 75) != "None":
                if enemy_colision(objekat, objekat.x - 150, objekat.y + 75).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x - 150, objekat.y - 75) != "None":
                if enemy_colision(objekat, objekat.x - 150, objekat.y - 75).obj == "King":
                    return objekat

        if objekat.obj == "Bishop":
            novix = objekat.x
            noviy = objekat.y
            prvi = True
            drugi = True
            treci = True
            cetvrti = True
            for i in range(7):
                if prvi == True:
                    if enemy_colision(objekat, novix + (i * 75) + 75, noviy + (i * 75) + 75) != "None":
                        if enemy_colision(objekat, novix + (i * 75) + 75, noviy + (i * 75) + 75).obj == "King":
                            return objekat
                        else:
                            prvi = False
                if ally_colision(objekat, novix + (i * 75) + 75, noviy + (i * 75) + 75) != "None":
                    prvi = False

                if drugi == True:
                    if enemy_colision(objekat, novix + (i * 75) + 75, noviy - (i * 75) - 75) != "None":
                        if enemy_colision(objekat, novix + (i * 75) + 75, noviy - (i * 75) - 75).obj == "King":
                            return objekat
                        else:
                            drugi = False
                    if ally_colision(objekat, novix + (i * 75) + 75, noviy - (i * 75) - 75) != "None":
                        drugi = False

                if treci == True:
                    if enemy_colision(objekat, novix - (i * 75) - 75, noviy + (i * 75) + 75) != "None":
                        if enemy_colision(objekat, novix - (i * 75) - 75, noviy + (i * 75) + 75).obj == "King":
                            return objekat
                        else:
                            treci = False
                    if ally_colision(objekat, novix - (i * 75) - 75, noviy + (i * 75) + 75) != "None":
                        treci = False

                if cetvrti == True:
                    if enemy_colision(objekat, novix - (i * 75) - 75, noviy - (i * 75) - 75) != "None":
                        if enemy_colision(objekat, novix - (i * 75) - 75, noviy - (i * 75) - 75).obj == "King":
                            return objekat
                        else:
                            cetvrti = False
                    if ally_colision(objekat, novix - (i * 75) - 75, noviy - (i * 75) - 75) != "None":
                        cetvrti = False

        if objekat.obj == "Rook":
            novix = objekat.x
            noviy = objekat.y
            prvi = True
            drugi = True
            treci = True
            cetvrti = True
            for i in range(7):
                if prvi == True:
                    if enemy_colision(objekat, novix + (i * 75) + 75, noviy) != "None":
                        if enemy_colision(objekat, novix + (i * 75) + 75, noviy).obj == "King":
                            return objekat
                        else:
                            prvi = False
                if ally_colision(objekat, novix + (i * 75) + 75, noviy) != "None":
                    prvi = False

                if drugi == True:
                    if enemy_colision(objekat, novix, noviy - (i * 75) - 75) != "None":
                        if enemy_colision(objekat, novix, noviy - (i * 75) - 75).obj == "King":
                            return objekat
                        else:
                            drugi = False
                    if ally_colision(objekat, novix, noviy - (i * 75) - 75) != "None":
                        drugi = False

                if treci == True:
                    if enemy_colision(objekat, novix, noviy + (i * 75) + 75) != "None":
                        if enemy_colision(objekat, novix, noviy + (i * 75) + 75).obj == "King":
                            return objekat
                        else:
                            treci = False
                    if ally_colision(objekat, novix, noviy + (i * 75) + 75) != "None":
                        treci = False

                if cetvrti == True:
                    if enemy_colision(objekat, novix - (i * 75) - 75, noviy) != "None":
                        if enemy_colision(objekat, novix - (i * 75) - 75, noviy).obj == "King":
                            return objekat
                        else:
                            cetvrti = False
                    if ally_colision(objekat, novix - (i * 75) - 75, noviy) != "None":
                        cetvrti = False

        if objekat.obj == "Queen":
            novix = objekat.x
            noviy = objekat.y
            prvi = True
            drugi = True
            treci = True
            cetvrti = True
            peti = True
            sesti = True
            sedmi = True
            osmi = True
            for i in range(7):

                if prvi == True:
                    if enemy_colision(objekat, novix + (i * 75) + 75, noviy + (i * 75) + 75) != "None":
                        if enemy_colision(objekat, novix + (i * 75) + 75, noviy + (i * 75) + 75).obj == "King":
                            return objekat
                        else:
                            prvi = False
                if ally_colision(objekat, novix + (i * 75) + 75, noviy + (i * 75) + 75) != "None":
                    prvi = False

                if drugi == True:
                    if enemy_colision(objekat, novix + (i * 75) + 75, noviy - (i * 75) - 75) != "None":
                        if enemy_colision(objekat, novix + (i * 75) + 75, noviy - (i * 75) - 75).obj == "King":
                            return objekat
                        else:
                            drugi = False
                    if ally_colision(objekat, novix + (i * 75) + 75, noviy - (i * 75) - 75) != "None":
                        drugi = False

                if treci == True:
                    if enemy_colision(objekat, novix - (i * 75) - 75, noviy + (i * 75) + 75) != "None":
                        if enemy_colision(objekat, novix - (i * 75) - 75, noviy + (i * 75) + 75).obj == "King":
                            return objekat
                        else:
                            treci = False
                    if ally_colision(objekat, novix - (i * 75) - 75, noviy + (i * 75) + 75) != "None":
                        treci = False

                if cetvrti == True:
                    if enemy_colision(objekat, novix - (i * 75) - 75, noviy - (i * 75) - 75) != "None":
                        if enemy_colision(objekat, novix - (i * 75) - 75, noviy - (i * 75) - 75).obj == "King":
                            return objekat
                        else:
                            cetvrti = False
                    if ally_colision(objekat, novix - (i * 75) - 75, noviy - (i * 75) - 75) != "None":
                        cetvrti = False

                if peti == True:
                    if enemy_colision(objekat, novix + (i * 75) + 75, noviy) != "None":
                        if enemy_colision(objekat, novix + (i * 75) + 75, noviy).obj == "King":
                            return objekat
                        else:
                            peti = False
                if ally_colision(objekat, novix + (i * 75) + 75, noviy) != "None":
                    peti = False

                if sesti == True:
                    if enemy_colision(objekat, novix, noviy - (i * 75) - 75) != "None":
                        if enemy_colision(objekat, novix, noviy - (i * 75) - 75).obj == "King":
                            return objekat
                        else:
                            sesti = False
                    if ally_colision(objekat, novix, noviy - (i * 75) - 75) != "None":
                        sesti = False

                if sedmi == True:
                    if enemy_colision(objekat, novix, noviy + (i * 75) + 75) != "None":
                        if enemy_colision(objekat, novix, noviy + (i * 75) + 75).obj == "King":
                            return objekat
                        else:
                            sedmi = False
                    if ally_colision(objekat, novix, noviy + (i * 75) + 75) != "None":
                        sedmi = False

                if osmi == True:
                    if enemy_colision(objekat, novix - (i * 75) - 75, noviy) != "None":
                        if enemy_colision(objekat, novix - (i * 75) - 75, noviy).obj == "King":
                            return objekat
                        else:
                            osmi = False
                    if ally_colision(objekat, novix - (i * 75) - 75, noviy) != "None":
                        osmi = False

        if objekat.obj == "King":
            if enemy_colision(objekat, objekat.x + 75, objekat.y) != "None":
                if enemy_colision(objekat, objekat.x + 75, objekat.y).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x - 75, objekat.y) != "None":
                if enemy_colision(objekat, objekat.x - 75, objekat.y).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x, objekat.y + 75) != "None":
                if enemy_colision(objekat, objekat.x, objekat.y + 75).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x, objekat.y - 75) != "None":
                if enemy_colision(objekat, objekat.x, objekat.y - 75).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x + 75, objekat.y - 75) != "None":
                if enemy_colision(objekat, objekat.x + 75, objekat.y - 75).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x - 75, objekat.y - 75) != "None":
                if enemy_colision(objekat, objekat.x - 75, objekat.y - 75).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x - 75, objekat.y + 75) != "None":
                if enemy_colision(objekat, objekat.x - 75, objekat.y + 75).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x + 75, objekat.y + 75) != "None":
                if enemy_colision(objekat, objekat.x + 75, objekat.y + 75).obj == "King":
                    return objekat

    return "None"

def king_checkmated(pieces, potez):
    for objekat in pieces:
        za_brisanje = "None"
        if objekat.obj == "Pawn":
            if objekat.color == "white":
                if (ally_colision(objekat, objekat.x, objekat.y - 75) != "None" or enemy_colision(objekat, objekat.x, objekat.y - 75) != "None" or border_colision(objekat.x,
                                                                                                   objekat.y - 75)):
                    pass
                else:
                    objekat.y -= 75
                    if king_checked(crni) == "None":
                        objekat.y = objekat.stariy
                        return False
                objekat.y = objekat.stariy

                if(objekat.stariy == 452.5):
                    if (ally_colision(objekat, objekat.x, objekat.y - 150) != "None" or enemy_colision(objekat, objekat.x, objekat.y - 150) != "None" or border_colision(objekat.x, objekat.y - 150)):
                        pass
                    else:
                        objekat.y -= 150
                        if king_checked(crni) == "None":
                            objekat.y = objekat.stariy
                            return False
                    objekat.y = objekat.stariy

                if (ally_colision(objekat, objekat.x - 75, objekat.y - 75) != "None" or border_colision(objekat.x - 75, objekat.y - 75)):
                    pass
                else:
                    if(enemy_colision(objekat, objekat.x - 75, objekat.y - 75) != "None"):
                        objekat.x -= 75
                        objekat.y -= 75
                        za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                        crni.pop(crni.index(za_brisanje))
                        if king_checked(crni) == "None":
                            objekat.y = objekat.stariy
                            objekat.x = objekat.starix
                            crni.append(za_brisanje)
                            return False
                        crni.append(za_brisanje)
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy


                if (ally_colision(objekat, objekat.x + 75, objekat.y - 75) != "None" or border_colision(objekat.x + 75, objekat.y - 75)):
                    pass
                else:
                    if(enemy_colision(objekat, objekat.x + 75, objekat.y - 75) != "None"):
                        objekat.x += 75
                        objekat.y -= 75
                        za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                        crni.pop(crni.index(za_brisanje))
                        if king_checked(crni) == "None":
                            objekat.y = objekat.stariy
                            objekat.x = objekat.starix
                            crni.append(za_brisanje)
                            return False
                        crni.append(za_brisanje)
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy


                if (ally_colision(objekat, objekat.x - 75, objekat.y) != "None" or border_colision(objekat.x - 75, objekat.y - 75)):
                    pass
                else:
                    if(enemy_colision(objekat, objekat.x - 75, objekat.y) != "None"):
                        if (enemy_colision(objekat, objekat.x - 75, objekat.y)).obj == "Pawn":
                            if(enemy_colision(objekat, objekat.x - 75, objekat.y).enp == potez - 1):
                                za_brisanje = enemy_colision(objekat, objekat.x - 75, objekat.y)
                                objekat.x -= 75
                                objekat.y -= 75
                                crni.pop(crni.index(za_brisanje))
                                if king_checked(crni) == "None":
                                    objekat.y = objekat.stariy
                                    objekat.x = objekat.starix
                                    crni.append(za_brisanje)
                                    return False
                                crni.append(za_brisanje)
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy

                if (ally_colision(objekat, objekat.x + 75, objekat.y) != "None" or border_colision(objekat.x + 75, objekat.y - 75)):
                    pass
                else:
                    if(enemy_colision(objekat, objekat.x + 75, objekat.y) != "None"):
                        if(enemy_colision(objekat, objekat.x + 75, objekat.y)).obj == "Pawn":
                            if(enemy_colision(objekat, objekat.x + 75, objekat.y).enp == potez - 1):
                                za_brisanje = enemy_colision(objekat, objekat.x + 75, objekat.y)
                                objekat.x += 75
                                objekat.y -= 75
                                crni.pop(crni.index(za_brisanje))
                                if king_checked(crni) == "None":
                                    objekat.y = objekat.stariy
                                    objekat.x = objekat.starix
                                    crni.append(za_brisanje)
                                    return False
                                crni.append(za_brisanje)
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy




            else:

                if (ally_colision(objekat, objekat.x, objekat.y + 75) != "None" or enemy_colision(objekat, objekat.x, objekat.y + 75) != "None" or border_colision(objekat.x,
                                                                                                   objekat.y + 75)):
                    pass
                else:
                    objekat.y += 75
                    if king_checked(bijeli) == "None":
                        objekat.y = objekat.stariy
                        return False
                    objekat.y = objekat.stariy


                if (objekat.stariy == 77.5):
                    if (ally_colision(objekat, objekat.x, objekat.y + 150) != "None" or enemy_colision(objekat,
                                                                                                       objekat.x,
                                                                                                       objekat.y + 150) != "None" or border_colision(
                            objekat.x, objekat.y + 150)):
                        pass
                    else:
                        objekat.y += 150
                        if king_checked(bijeli) == "None":
                            objekat.y = objekat.stariy
                            return False
                    objekat.y = objekat.stariy

                if (ally_colision(objekat, objekat.x - 75, objekat.y + 75) != "None" or border_colision(objekat.x - 75, objekat.y + 75)):
                    pass
                else:
                    if(enemy_colision(objekat, objekat.x - 75, objekat.y + 75) != "None"):
                        objekat.x -= 75
                        objekat.y += 75
                        za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                        bijeli.pop(bijeli.index(za_brisanje))
                        if king_checked(bijeli) == "None":
                            objekat.y = objekat.stariy
                            objekat.x = objekat.starix
                            bijeli.append(za_brisanje)
                            return False
                        bijeli.append(za_brisanje)
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy


                if (ally_colision(objekat, objekat.x + 75, objekat.y + 75) != "None" or border_colision(objekat.x + 75, objekat.y + 75)):
                    pass
                else:
                    if(enemy_colision(objekat, objekat.x + 75, objekat.y + 75) != "None"):
                        objekat.x += 75
                        objekat.y += 75
                        za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                        bijeli.pop(bijeli.index(za_brisanje))
                        if king_checked(bijeli) == "None":
                            objekat.y = objekat.stariy
                            objekat.x = objekat.starix
                            bijeli.append(za_brisanje)
                            return False
                        bijeli.append(za_brisanje)
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy



                if (ally_colision(objekat, objekat.x - 75, objekat.y) != "None" or border_colision(objekat.x - 75, objekat.y + 75)):
                    pass
                else:
                    if(enemy_colision(objekat, objekat.x - 75, objekat.y) != "None"):
                        if (enemy_colision(objekat, objekat.x - 75, objekat.y)).obj == "Pawn":
                            if(enemy_colision(objekat, objekat.x - 75, objekat.y).enp == potez - 1):
                                za_brisanje = enemy_colision(objekat, objekat.x - 75, objekat.y)
                                objekat.x -= 75
                                objekat.y += 75
                                bijeli.pop(bijeli.index(za_brisanje))
                                if king_checked(bijeli) == "None":
                                    objekat.y = objekat.stariy
                                    objekat.x = objekat.starix
                                    bijeli.append(za_brisanje)
                                    return False
                                bijeli.append(za_brisanje)
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy

                if (ally_colision(objekat, objekat.x + 75, objekat.y) != "None" or border_colision(objekat.x + 75, objekat.y + 75)):
                    pass
                else:
                    if(enemy_colision(objekat, objekat.x + 75, objekat.y) != "None"):
                        if(enemy_colision(objekat, objekat.x + 75, objekat.y).enp == potez + 1):
                            if (enemy_colision(objekat, objekat.x + 75, objekat.y)).obj == "Pawn":
                                za_brisanje = enemy_colision(objekat, objekat.x + 75, objekat.y)
                                objekat.x += 75
                                objekat.y += 75
                                bijeli.pop(bijeli.index(za_brisanje))
                                if king_checked(bijeli) == "None":
                                    objekat.y = objekat.stariy
                                    objekat.x = objekat.starix
                                    bijeli.append(za_brisanje)
                                    return False
                                bijeli.append(za_brisanje)
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy

        if objekat.obj == "Knight":
            objekat.x -= 75
            objekat.y += 150
            if(enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
            if objekat.color == "white":
                if(za_brisanje != "None"):
                    crni.pop(crni.index(za_brisanje))
                if king_checked(crni) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)
                    return False
                objekat.x = objekat.starix
                objekat.y = objekat.stariy
                if (za_brisanje != "None"):
                    crni.append(za_brisanje)
            else:
                if (za_brisanje != "None"):
                    bijeli.pop(bijeli.index(za_brisanje))
                if king_checked(bijeli) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)
                    return False
                objekat.x = objekat.starix
                objekat.y = objekat.stariy
                if (za_brisanje != "None"):
                    bijeli.append(za_brisanje)

            objekat.x -= 75
            objekat.y -= 150
            if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
            if objekat.color == "white":
                if (za_brisanje != "None"):
                    crni.pop(crni.index(za_brisanje))
                if king_checked(crni) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)
                    return False
                objekat.x = objekat.starix
                objekat.y = objekat.stariy
                if (za_brisanje != "None"):
                    crni.append(za_brisanje)
            else:
                if (za_brisanje != "None"):
                    bijeli.pop(bijeli.index(za_brisanje))
                if king_checked(bijeli) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)
                    return False
            objekat.x = objekat.starix
            objekat.y = objekat.stariy
            if (za_brisanje != "None"):
                bijeli.append(za_brisanje)

            objekat.x += 75
            objekat.y += 150
            if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
            if objekat.color == "white":
                if (za_brisanje != "None"):
                    crni.pop(crni.index(za_brisanje))
                if king_checked(crni) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)
                    return False
                objekat.x = objekat.starix
                objekat.y = objekat.stariy
                if(za_brisanje != "None"):
                    crni.append(za_brisanje)
            else:
                if(za_brisanje != "None"):
                    bijeli.pop(bijeli.index(za_brisanje))
                if king_checked(bijeli) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)
                    return False
            objekat.x = objekat.starix
            objekat.y = objekat.stariy
            if(za_brisanje != "None"):
                bijeli.append(za_brisanje)

            objekat.x += 75
            objekat.y -= 150
            if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
            if objekat.color == "white":
                if(za_brisanje != "None"):
                    crni.pop(crni.index(za_brisanje))
                if king_checked(crni) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)
                    return False
                objekat.x = objekat.starix
                objekat.y = objekat.stariy
                if(za_brisanje != "None"):
                    crni.append(za_brisanje)
            else:
                if(za_brisanje != "None"):
                    bijeli.pop(bijeli.index(za_brisanje))
                if king_checked(bijeli) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)
                    return False
            objekat.x = objekat.starix
            objekat.y = objekat.stariy
            if(za_brisanje != "None"):
                bijeli.append(za_brisanje)

            objekat.x -= 150
            objekat.y += 75
            if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
            if objekat.color == "white":
                if(za_brisanje != "None"):
                    crni.pop(crni.index(za_brisanje))
                if king_checked(crni) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)
                    return False
                objekat.x = objekat.starix
                objekat.y = objekat.stariy
                if(za_brisanje != "None"):
                    crni.append(za_brisanje)
            else:
                if(za_brisanje != "None"):
                    bijeli.pop(bijeli.index(za_brisanje))
                if king_checked(bijeli) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)
                    return False
            objekat.x = objekat.starix
            objekat.y = objekat.stariy
            if(za_brisanje != "None"):
                bijeli.append(za_brisanje)

            objekat.x -= 150
            objekat.y -= 75
            if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
            if objekat.color == "white":
                if(za_brisanje != "None"):
                    crni.pop(crni.index(za_brisanje))
                if king_checked(crni) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)
                    return False
                objekat.x = objekat.starix
                objekat.y = objekat.stariy
                if(za_brisanje != "None"):
                    crni.append(za_brisanje)
            else:
                if(za_brisanje != "None"):
                    bijeli.pop(bijeli.index(za_brisanje))
                if king_checked(bijeli) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)
                    return False
            objekat.x = objekat.starix
            objekat.y = objekat.stariy
            if(za_brisanje != "None"):
                bijeli.append(za_brisanje)

            objekat.x += 150
            objekat.y += 75
            if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
            if objekat.color == "white":
                if(za_brisanje != "None"):
                    crni.pop(crni.index(za_brisanje))
                if king_checked(crni) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)
                    return False
                objekat.x = objekat.starix
                objekat.y = objekat.stariy
                if(za_brisanje != "None"):
                    crni.append(za_brisanje)
            else:
                if(za_brisanje != "None"):
                    bijeli.pop(bijeli.index(za_brisanje))
                if king_checked(bijeli) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)
                    return False
            objekat.x = objekat.starix
            objekat.y = objekat.stariy
            if(za_brisanje != "None"):
                bijeli.append(za_brisanje)

            objekat.x += 150
            objekat.y -= 75
            if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
            if objekat.color == "white":
                if(za_brisanje != "None"):
                    crni.pop(crni.index(za_brisanje))
                if king_checked(crni) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)
                    return False
                objekat.x = objekat.starix
                objekat.y = objekat.stariy
                if(za_brisanje != "None"):
                    crni.append(za_brisanje)
            else:
                if(za_brisanje != "None"):
                    bijeli.pop(bijeli.index(za_brisanje))
                if king_checked(bijeli) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)
                    return False
            objekat.x = objekat.starix
            objekat.y = objekat.stariy
            if(za_brisanje != "None"):
                bijeli.append(za_brisanje)
        if objekat.obj == "Bishop":
            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if(kraj == 1):
                    break
                objekat.x = objekat.starix + (i * 75)
                objekat.y = objekat.stariy + (i * 75)
                if (ally_colision(objekat, objekat.x + 75, objekat.y + 75) != "None"):
                    kraj = 1
                    continue
                objekat.x += 75
                objekat.y += 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)  #Ovdje si
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.x = objekat.starix - (i * 75)
                objekat.y = objekat.stariy + (i * 75)
                if (ally_colision(objekat, objekat.x - 75, objekat.y + 75) != "None"):
                    kraj = 1
                    continue
                objekat.x -= 75
                objekat.y += 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.x = objekat.starix + (i * 75)
                objekat.y = objekat.stariy - (i * 75)
                if (ally_colision(objekat, objekat.x + 75, objekat.y - 75) != "None"):
                    kraj = 1
                    continue
                objekat.x += 75
                objekat.y -= 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.x = objekat.starix - (i * 75)
                objekat.y = objekat.stariy - (i * 75)
                if (ally_colision(objekat, objekat.x - 75, objekat.y - 75) != "None"):
                    kraj = 1
                    continue
                objekat.x -= 75
                objekat.y -= 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy
        if objekat.obj == "Rook":
            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.x = objekat.starix + (i * 75)
                if (ally_colision(objekat, objekat.x + 75, objekat.y) != "None"):
                    kraj = 1
                    continue
                objekat.x += 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)  # Ovdje si
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)
            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.x = objekat.starix - (i * 75)
                if (ally_colision(objekat, objekat.x - 75, objekat.y) != "None"):
                    kraj = 1
                    continue
                objekat.x -= 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.y = objekat.stariy + (i * 75)
                if (ally_colision(objekat, objekat.x, objekat.y + 75) != "None"):
                    kraj = 1
                    continue
                objekat.y += 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.y = objekat.stariy - (i * 75)
                if (ally_colision(objekat, objekat.x, objekat.y - 75) != "None"):
                    kraj = 1
                    continue
                objekat.y -= 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy
        if objekat.obj == "Queen":
            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.x = objekat.starix + (i * 75)
                objekat.y = objekat.stariy + (i * 75)
                if (ally_colision(objekat, objekat.x + 75, objekat.y + 75) != "None"):
                    kraj = 1
                    continue
                objekat.x += 75
                objekat.y += 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)  # Ovdje si
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.x = objekat.starix - (i * 75)
                objekat.y = objekat.stariy + (i * 75)
                if (ally_colision(objekat, objekat.x - 75, objekat.y + 75) != "None"):
                    kraj = 1
                    continue
                objekat.x -= 75
                objekat.y += 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.x = objekat.starix + (i * 75)
                objekat.y = objekat.stariy - (i * 75)
                if (ally_colision(objekat, objekat.x + 75, objekat.y - 75) != "None"):
                    kraj = 1
                    continue
                objekat.x += 75
                objekat.y -= 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.x = objekat.starix - (i * 75)
                objekat.y = objekat.stariy - (i * 75)
                if (ally_colision(objekat, objekat.x - 75, objekat.y - 75) != "None"):
                    kraj = 1
                    continue
                objekat.x -= 75
                objekat.y -= 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.x = objekat.starix + (i * 75)
                if (ally_colision(objekat, objekat.x + 75, objekat.y) != "None"):
                    kraj = 1
                    continue
                objekat.x += 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)  # Ovdje si
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)
            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.x = objekat.starix - (i * 75)
                if (ally_colision(objekat, objekat.x - 75, objekat.y) != "None"):
                    kraj = 1
                    continue
                objekat.x -= 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.y = objekat.stariy + (i * 75)
                if (ally_colision(objekat, objekat.x, objekat.y + 75) != "None"):
                    kraj = 1
                    continue
                objekat.y += 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.y = objekat.stariy - (i * 75)
                if (ally_colision(objekat, objekat.x, objekat.y - 75) != "None"):
                    kraj = 1
                    continue
                objekat.y -= 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy
        if objekat.obj == "King":
            if (ally_colision(objekat, objekat.x + 75, objekat.y) != "None" or border_colision(objekat.x + 75, objekat.y)):
                pass
            else:
                objekat.x += 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            if (ally_colision(objekat, objekat.x - 75, objekat.y) != "None" or border_colision(objekat.x - 75, objekat.y)):
                pass
            else:
                objekat.x -= 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            if (ally_colision(objekat, objekat.x, objekat.y + 75) != "None" or border_colision(objekat.x, objekat.y + 75)):
                pass
            else:
                objekat.y += 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            if (ally_colision(objekat, objekat.x, objekat.y - 75) != "None" or border_colision(objekat.x, objekat.y - 75)):
                pass
            else:
                objekat.y -= 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            if (ally_colision(objekat, objekat.x + 75, objekat.y + 75) != "None" or border_colision(objekat.x + 75, objekat.y + 75)):
                pass
            else:
                objekat.x += 75
                objekat.y += 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            if (ally_colision(objekat, objekat.x + 75, objekat.y - 75) != "None" or border_colision(objekat.x + 75, objekat.y - 75)):
                pass
            else:
                objekat.x += 75
                objekat.y -= 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            if (ally_colision(objekat, objekat.x - 75, objekat.y + 75) != "None" or border_colision(objekat.x - 75, objekat.y + 75)):
                pass
            else:
                objekat.x -= 75
                objekat.y += 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            if (ally_colision(objekat, objekat.x - 75, objekat.y - 75) != "None" or border_colision(objekat.x - 75, objekat.y - 75)):
                pass
            else:
                objekat.x -= 75
                objekat.y -= 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

    return True

class Pawn:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.starix = x
        self.stariy = y
        self.enp = 0
        self.obj = "Pawn"
        if color == 'white':
            self.color = 'white'
            self.object = White_Pawn
        else:
            self.color = 'black'
            self.object = Black_Pawn

    def draw(self, win):
        win.blit(self.object, (self.x, self.y))

    def move(self, potez):
        if self.color == "white":
            if ((self.stariy - 77.5) <= self.y + 37.5 <= (self.stariy + 2.5)) and (
                    self.starix - 77.5 <= self.x + 37.5 <= self.starix - 2.5):
                if((enemy_colision(self, self.starix - 75, self.stariy)) != "None"):   #EnPassant lijevi
                    if(enemy_colision(self, self.starix - 75, self.stariy)).obj == "Pawn":
                        if enemy_colision(self, self.starix - 75, self.stariy).enp == (potez-1):
                            self.x = self.starix - 75
                            self.y = self.stariy - 75
                            za_brisanje = enemy_colision(self, self.starix - 75, self.stariy)
                            crni.pop(crni.index(za_brisanje))
                            if king_checked(crni) != "None" or border_colision(self.x, self.y):
                                self.x = self.starix
                                self.y = self.stariy
                                crni.append(za_brisanje)
                                return False
                            self.starix = self.starix - 75
                            self.stariy = self.stariy - 75
                            return True
                if(enemy_colision(self, self.starix - 75, self.stariy - 75) != 'None'):
                    self.x = self.starix - 75
                    self.y = self.stariy - 75
                    za_brisanje = enemy_colision(self, self.starix - 75, self.stariy - 75)
                    crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        crni.append(za_brisanje)
                        return False
                    self.starix = self.starix - 75
                    self.stariy = self.stariy - 75
                    return True
                self.x = self.starix
                self.y = self.stariy
                return False
            if ((self.stariy - 77.5) <= self.y + 37.5 <= (self.stariy + 2.5)) and (
                    self.starix + 72.5 <= self.x + 37.5 <= self.starix + 147.5):

                if ((enemy_colision(self, self.starix + 75, self.stariy)) != "None"):  # EnPassant desni
                    if (enemy_colision(self, self.starix + 75, self.stariy)).obj == "Pawn":
                        if enemy_colision(self, self.starix + 75, self.stariy).enp == (potez - 1):
                            self.x = self.starix + 75
                            self.y = self.stariy - 75
                            za_brisanje = enemy_colision(self, self.starix + 75, self.stariy)
                            crni.pop(crni.index(za_brisanje))
                            if king_checked(crni) != "None" or border_colision(self.x, self.y):
                                self.x = self.starix
                                self.y = self.stariy
                                crni.append(za_brisanje)
                                return False
                            self.starix = self.starix + 75
                            self.stariy = self.stariy - 75
                            return True

                if(enemy_colision(self, self.starix + 75, self.stariy - 75) != 'None'):
                    self.x = self.starix + 75
                    self.y = self.stariy - 75
                    za_brisanje = enemy_colision(self, self.starix + 75, self.stariy - 75)
                    crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        crni.append(za_brisanje)
                        return False
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
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    self.starix = self.x
                    self.stariy = self.y
                    self.enp = potez
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
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
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
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    self.starix = self.x
                    self.stariy = self.y
                    return True
                else:
                    self.x = self.starix
                    self.y = self.stariy
                    return False
        else:
            if ((self.stariy + 77.5) <= self.y + 37.5 <= (self.stariy + 152.5)) and (
                    self.starix + 72.5 <= self.x + 37.5 <= self.starix + 147.5):
                if ((enemy_colision(self, self.starix + 75, self.stariy)) != "None"):  # EnPassant desni
                    if (enemy_colision(self, self.starix + 75, self.stariy)).obj == "Pawn":
                        if enemy_colision(self, self.starix + 75, self.stariy).enp == (potez - 1):
                            self.x = self.starix + 75
                            self.y = self.stariy + 75
                            za_brisanje = enemy_colision(self, self.starix + 75, self.stariy)
                            bijeli.pop(bijeli.index(za_brisanje))
                            if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                                self.x = self.starix
                                self.y = self.stariy
                                bijeli.append(za_brisanje)
                                return False
                            self.starix = self.starix + 75
                            self.stariy = self.stariy + 75
                            return True

                if(enemy_colision(self, self.starix + 75, self.stariy + 75) != 'None'):
                    self.x = self.starix + 75
                    self.y = self.stariy + 75
                    za_brisanje = enemy_colision(self, self.starix + 75, self.stariy + 75)
                    bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        bijeli.append(za_brisanje)
                        return False
                    self.starix = self.starix + 75
                    self.stariy = self.stariy + 75
                    return True
                self.x = self.starix
                self.y = self.stariy
                return False
            if ((self.stariy + 77.5) <= self.y + 37.5 <= (self.stariy + 152.5)) and (
                    self.starix - 77.5 <= self.x + 37.5 <= self.starix - 2.5):

                if ((enemy_colision(self, self.starix - 75, self.stariy)) != "None"):  # EnPassant lijevi
                    if (enemy_colision(self, self.starix - 75, self.stariy)).obj == "Pawn":
                        if enemy_colision(self, self.starix - 75, self.stariy).enp == (potez - 1):
                            self.x = self.starix - 75
                            self.y = self.stariy + 75
                            za_brisanje = enemy_colision(self, self.starix - 75, self.stariy)
                            bijeli.pop(bijeli.index(za_brisanje))
                            if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                                self.x = self.starix
                                self.y = self.stariy
                                bijeli.append(za_brisanje)
                                return False
                            self.starix = self.starix - 75
                            self.stariy = self.stariy + 75
                            return True

                if(enemy_colision(self, self.starix - 75, self.stariy + 75) != 'None'):
                    self.x = self.starix - 75
                    self.y = self.stariy + 75
                    za_brisanje = enemy_colision(self, self.starix - 75, self.stariy + 75)
                    bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        bijeli.append(za_brisanje)
                        return False
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
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    self.starix = self.x
                    self.stariy = self.y
                    self.enp = potez
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
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
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
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
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
        self.obj = "Knight"
        if color == 'white':
            self.color = 'white'
            self.object = White_Knight
        else:
            self.color = 'black'
            self.object = Black_Knight

    def draw(self, win):
        win.blit(self.object, (self.x, self.y))

    def move(self, potez):
        kontrola = 0
        if ((self.stariy - 152.5) <= self.y + 37.5 <= (self.stariy - 72.5)):
            if (self.starix +72.5 <= self.x + 37.5 <= self.starix + 147.5):
                if (ally_colision(self, self.starix + 75, self.stariy - 150) != 'None'):
                    self.x = self.starix
                    self.y = self.stariy
                    return False

                self.x = self.starix + 75
                self.y = self.stariy - 150

                if (enemy_colision(self, self.starix + 75, self.stariy - 150) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix + 75, self.stariy - 150)
                    kontrola = 1
                    if self.color == 'white':
                        crni.pop(crni.index(za_brisanje))
                    else:
                        bijeli.pop(bijeli.index(za_brisanje))

                if self.color == "white":
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            crni.append(za_brisanje)
                        return False
                else:
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            bijeli.append(za_brisanje)
                        return False

                self.starix = self.x
                self.stariy = self.y
                return True

            elif (self.starix - 77.5 <= self.x + 37.5 <= self.starix - 2.5):
                if (ally_colision(self, self.starix - 75, self.stariy - 150) != 'None'):
                    self.x = self.starix
                    self.y = self.stariy
                    return False
                self.x = self.starix - 75
                self.y = self.stariy - 150

                if (enemy_colision(self, self.starix - 75, self.stariy - 150) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix - 75, self.stariy - 150)
                    kontrola = 1
                    if self.color == 'white':
                        crni.pop(crni.index(za_brisanje))
                    else:
                        bijeli.pop(bijeli.index(za_brisanje))

                if self.color == "white":
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            crni.append(za_brisanje)
                        return False
                else:
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            bijeli.append(za_brisanje)
                        return False
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
                self.x = self.starix + 75
                self.y = self.stariy + 150
                if (enemy_colision(self, self.starix + 75, self.stariy + 150) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix + 75, self.stariy + 150)
                    kontrola = 1
                    if self.color == 'white':
                        crni.pop(crni.index(za_brisanje))
                    else:
                        bijeli.pop(bijeli.index(za_brisanje))
                if self.color == "white":
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            crni.append(za_brisanje)
                        return False
                else:
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            bijeli.append(za_brisanje)
                        return False

                self.starix = self.x
                self.stariy = self.y
                return True
            elif (self.starix - 77.5 <= self.x + 37.5 <= self.starix - 2.5):
                if (ally_colision(self, self.starix - 75, self.stariy + 150) != 'None'):
                    self.x = self.starix
                    self.y = self.stariy
                    return False
                self.x = self.starix - 75
                self.y = self.stariy + 150

                if (enemy_colision(self, self.starix - 75, self.stariy + 150) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix - 75, self.stariy + 150)
                    kontrola = 1
                    if self.color == 'white':
                        crni.pop(crni.index(za_brisanje))
                    else:
                        bijeli.pop(bijeli.index(za_brisanje))

                if self.color == "white":
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            crni.append(za_brisanje)
                        return False
                else:
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            bijeli.append(za_brisanje)
                        return False

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
                self.x = self.starix + 150
                self.y = self.stariy - 75
                if (enemy_colision(self, self.starix + 150, self.stariy - 75) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix + 150, self.stariy - 75)
                    kontrola = 1
                    if self.color == 'white':
                        crni.pop(crni.index(za_brisanje))
                    else:
                        bijeli.pop(bijeli.index(za_brisanje))
                if self.color == "white":
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            crni.append(za_brisanje)
                        return False
                else:
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            bijeli.append(za_brisanje)
                        return False
                self.starix = self.x
                self.stariy = self.y
                return True
            elif (self.stariy + 72.5 <= self.y + 37.5 <= self.stariy + 147.5):
                if (ally_colision(self, self.starix + 150, self.stariy + 75) != 'None'):
                    self.x = self.starix
                    self.y = self.stariy
                    return False

                self.x = self.starix + 150
                self.y = self.stariy + 75
                if (enemy_colision(self, self.starix + 150, self.stariy + 75) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix + 150, self.stariy + 75)
                    kontrola = 1
                    if self.color == 'white':
                        crni.pop(crni.index(za_brisanje))
                    else:
                        bijeli.pop(bijeli.index(za_brisanje))
                if self.color == "white":
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            crni.append(za_brisanje)
                        return False
                else:
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            bijeli.append(za_brisanje)
                        return False

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

                self.x = self.starix - 150
                self.y = self.stariy - 75
                if (enemy_colision(self, self.starix - 150, self.stariy - 75) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix - 150, self.stariy - 75)
                    kontrola = 1
                    if self.color == 'white':
                        crni.pop(crni.index(za_brisanje))
                    else:
                        bijeli.pop(bijeli.index(za_brisanje))
                if self.color == "white":
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            crni.append(za_brisanje)
                        return False
                else:
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            bijeli.append(za_brisanje)
                        return False

                self.starix = self.x
                self.stariy = self.y
                return True
            elif (self.stariy + 72.5 <= self.y + 37.5 <= self.stariy + 147.5):
                if (ally_colision(self, self.starix - 150, self.stariy + 75) != 'None'):
                    self.x = self.starix
                    self.y = self.stariy
                    return False

                self.x = self.starix - 150
                self.y = self.stariy + 75
                if (enemy_colision(self, self.starix - 150, self.stariy + 75) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix - 150, self.stariy + 75)
                    kontrola = 1
                    if self.color == 'white':
                        crni.pop(crni.index(za_brisanje))
                    else:
                        bijeli.pop(bijeli.index(za_brisanje))
                if self.color == "white":
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            crni.append(za_brisanje)
                        return False
                else:
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            bijeli.append(za_brisanje)
                        return False

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
        self.obj = "Bishop"
        if color == 'white':
            self.color = 'white'
            self.object = White_Bishop
        else:
            self.color = 'black'
            self.object = Black_Bishop

    def draw(self, win):
        win.blit(self.object, (self.x, self.y))
    def move(self, potez):
        kontrola = 0
        novix = self.starix
        noviy = self.stariy
        for i in range(7):
            if (ally_colision(self, novix - 75, noviy - 75) != 'None'):
                break
            if(noviy - 77.5 <= self.y + 37.5 <= noviy - 2.5):
                if(novix - 77.5 <= self.x + 37.5 <= novix - 2.5):
                    if (ally_colision(self, novix - 75, noviy - 75) != 'None'):
                        break
                    if (enemy_colision(self, novix - 75, noviy - 75) != 'None'):
                        kontrola = 1
                        za_brisanje = enemy_colision(self, novix - 75, noviy - 75)
                        if(self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix - 75
                    self.y = noviy - 75
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix - 75
                    self.stariy = noviy - 75
                    return True
            if (enemy_colision(self, novix - 75, noviy - 75) != 'None'):
                break
            novix -= 75
            noviy -= 75
        kontrola = 0
        novix = self.starix
        noviy = self.stariy
        for i in range(7):
            if (ally_colision(self, novix + 75, noviy - 75) != 'None'):
                break
            if (noviy - 77.5 <= self.y + 37.5 <= noviy - 2.5):
                if(novix + 72.5 <= self.x + 37.5 <= novix + 147.5):
                    if (ally_colision(self, novix + 75, noviy - 75) != 'None'):
                        break
                    if (enemy_colision(self, novix + 75, noviy - 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix + 75, noviy - 75)
                        kontrola = 1
                        if(self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix + 75
                    self.y = noviy - 75
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix + 75
                    self.stariy = noviy - 75
                    return True
            if (enemy_colision(self, novix + 75, noviy - 75) != 'None'):
                break
            novix += 75
            noviy -= 75
        kontrola = 0
        novix = self.starix
        noviy = self.stariy
        for i in range(7):
            if (ally_colision(self, novix - 75, noviy + 75) != 'None'):
                break
            if (noviy + 72.5 <= self.y + 37.5 <= noviy + 147.5):
                if (novix - 77.5 <= self.x + 37.5 <= novix - 2.5):
                    if (ally_colision(self, novix - 75, noviy + 75) != 'None'):
                        break
                    if (enemy_colision(self, novix - 75, noviy + 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix - 75, noviy + 75)
                        kontrola = 1
                        if(self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix - 75
                    self.y = noviy + 75
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix - 75
                    self.stariy = noviy + 75
                    return True
            if (enemy_colision(self, novix - 75, noviy + 75) != 'None'):
                break
            novix -= 75
            noviy += 75
        kontrola = 0
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
                        kontrola = 1
                        if(self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix + 75
                    self.y = noviy + 75
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix + 75
                    self.stariy = noviy + 75
                    return True
            if (enemy_colision(self, novix + 75, noviy + 75) != 'None'):
                break
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
        self.castle = 0
        self.obj = "Rook"
        if color == 'white':
            self.color = 'white'
            self.object = White_Rook
        else:
            self.color = 'black'
            self.object = Black_Rook

    def draw(self, win):
        win.blit(self.object, (self.x, self.y))

    def move(self, potez):
        kontrola = 0
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
                        kontrola = 1
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix
                    self.y = noviy - 75
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix
                    self.stariy = noviy - 75
                    self.castle = potez
                    return True
            if (enemy_colision(self, novix, noviy - 75) != 'None'):
                break
            noviy -= 75
        kontrola = 0
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
                        kontrola = 1
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix
                    self.y = noviy + 75
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix
                    self.stariy = noviy + 75
                    self.castle = potez
                    return True
            if (enemy_colision(self, novix, noviy + 75) != 'None'):
                break
            noviy += 75
        kontrola = 0
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
                        kontrola = 1
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix - 75
                    self.y = noviy
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix - 75
                    self.stariy = noviy
                    self.castle = potez
                    return True
            if (enemy_colision(self, novix  - 75, noviy) != 'None'):
                break
            novix -= 75
        kontrola = 0
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
                        kontrola = 1
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix + 75
                    self.y = noviy
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix + 75
                    self.stariy = noviy
                    self.castle = potez
                    return True
            if (enemy_colision(self, novix  + 75, noviy) != 'None'):
                break
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
        self.obj = "Queen"
        if color == 'white':
            self.color = 'white'
            self.object = White_Queen
        else:
            self.color = 'black'
            self.object = Black_Queen

    def draw(self, win):
        win.blit(self.object, (self.x, self.y))

    def move(self, potez):
        kontrola = 0
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
                        kontrola = 1
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix
                    self.y = noviy - 75
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix
                    self.stariy = noviy - 75
                    return True
            if (enemy_colision(self, novix, noviy - 75) != 'None'):
                break
            noviy -= 75
        kontrola = 0
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
                        kontrola = 1
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix
                    self.y = noviy + 75
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix
                    self.stariy = noviy + 75
                    return True
            if (enemy_colision(self, novix, noviy + 75) != 'None'):
                break
            noviy += 75
        kontrola = 0
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
                        kontrola = 1
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix - 75
                    self.y = noviy
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix - 75
                    self.stariy = noviy
                    return True
            if (enemy_colision(self, novix - 75, noviy) != 'None'):
                break
            novix -= 75
        kontrola = 0
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
                        kontrola = 1
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix + 75
                    self.y = noviy
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix + 75
                    self.stariy = noviy
                    return True
            if (enemy_colision(self, novix + 75, noviy) != 'None'):
                break
            novix += 75
        kontrola = 0
        novix = self.starix
        noviy = self.stariy
        for i in range(7):
            if (ally_colision(self, novix - 75, noviy - 75) != 'None'):
                break
            if (noviy - 77.5 <= self.y + 37.5 <= noviy - 2.5):
                if (novix - 77.5 <= self.x + 37.5 <= novix - 2.5):
                    if (ally_colision(self, novix - 75, noviy - 75) != 'None'):
                        break
                    if (enemy_colision(self, novix - 75, noviy - 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix - 75, noviy - 75)
                        kontrola = 1
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix - 75
                    self.y = noviy - 75
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix - 75
                    self.stariy = noviy - 75
                    return True
            if (enemy_colision(self, novix - 75, noviy - 75) != 'None'):
                break
            novix -= 75
            noviy -= 75
        kontrola = 0
        novix = self.starix
        noviy = self.stariy
        for i in range(7):
            if (ally_colision(self, novix + 75, noviy - 75) != 'None'):
                break
            if (noviy - 77.5 <= self.y + 37.5 <= noviy - 2.5):
                if (novix + 72.5 <= self.x + 37.5 <= novix + 147.5):
                    if (ally_colision(self, novix + 75, noviy - 75) != 'None'):
                        break
                    if (enemy_colision(self, novix + 75, noviy - 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix + 75, noviy - 75)
                        kontrola = 1
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix + 75
                    self.y = noviy - 75
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix + 75
                    self.stariy = noviy - 75
                    return True
            if (enemy_colision(self, novix + 75, noviy - 75) != 'None'):
                break
            novix += 75
            noviy -= 75
        kontrola = 0
        novix = self.starix
        noviy = self.stariy
        for i in range(7):
            if (ally_colision(self, novix - 75, noviy + 75) != 'None'):
                break
            if (noviy + 72.5 <= self.y + 37.5 <= noviy + 147.5):
                if (novix - 77.5 <= self.x + 37.5 <= novix - 2.5):
                    if (ally_colision(self, novix - 75, noviy + 75) != 'None'):
                        break
                    if (enemy_colision(self, novix - 75, noviy + 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix - 75, noviy + 75)
                        kontrola = 1
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix - 75
                    self.y = noviy + 75
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix - 75
                    self.stariy = noviy + 75
                    return True
            if (enemy_colision(self, novix - 75, noviy + 75) != 'None'):
                break
            novix -= 75
            noviy += 75
        kontrola = 0
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
                        kontrola = 1
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix + 75
                    self.y = noviy + 75
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix + 75
                    self.stariy = noviy + 75
                    return True
            if (enemy_colision(self, novix + 75, noviy + 75) != 'None'):
                break
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
        self.castle = 0
        self.obj = "King"
        if color == 'white':
            self.color = 'white'
            self.object = White_King
        else:
            self.color = 'black'
            self.object = Black_King

    def draw(self, win):
        win.blit(self.object, (self.x, self.y))

    def move(self, potez):
        kontrola = 0
        if self.castle == 0:
            if (self.starix + 147.5 <= self.x + 37.5 <= self.starix + 222.5) and (     #desni castle
                    self.stariy - 2.5 <= self.y + 37.5 <= self.stariy + 72.5):
                self.x = self.starix
                self.y = self.stariy
                if self.color == "white":
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                else:
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                noviy = self.stariy
                novix = self.starix + 75
                for i in range(4):
                    if enemy_colision(self, novix, noviy) != "None":
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    if ally_colision(self, novix, noviy)!= "None":
                        if ally_colision(self, novix, noviy).obj != "Rook":
                            self.x = self.starix
                            self.y = self.stariy
                            return False
                        if ally_colision(self, novix, noviy).castle != 0:
                            self.x = self.starix
                            self.y = self.stariy
                            return False
                        else:

                            self.x = self.starix + 75
                            self.y = self.stariy
                            if self.color == "white":
                                if king_checked(crni) != "None" or border_colision(self.x, self.y):
                                    self.x = self.starix
                                    self.y = self.stariy
                                    return False
                            else:
                                if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                                    self.x = self.starix
                                    self.y = self.stariy
                                    return False
                            self.x = self.starix + 150
                            if self.color == "white":
                                if king_checked(crni) != "None" or border_colision(self.x, self.y):
                                    self.x = self.starix
                                    self.y = self.stariy
                                    return False
                            else:
                                if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                                    self.x = self.starix
                                    self.y = self.stariy
                                    return False
                            self.starix += 150
                            self.castle = potez
                            ally_colision(self, novix, noviy).starix -= 150
                            ally_colision(self, novix, noviy).x -= 150
                            return True
                    novix += 75

            if (self.starix - 152.5 <= self.x + 37.5 <= self.starix - 77.5) and (         #lijevi castle
                    self.stariy - 2.5 <= self.y + 37.5 <= self.stariy + 72.5):
                self.x = self.starix
                self.y = self.stariy
                if self.color == "white":
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                else:
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                noviy = self.stariy
                novix = self.starix - 75
                for i in range(4):
                    if enemy_colision(self, novix, noviy) != "None":
                        return False
                    if ally_colision(self, novix, noviy)!= "None":
                        if ally_colision(self, novix, noviy).obj != "Rook":
                            return False
                        if ally_colision(self, novix, noviy).castle != 0:
                            return False
                        else:
                            self.x = self.starix - 75
                            if self.color == "white":
                                if king_checked(crni) != "None" or border_colision(self.x, self.y):
                                    self.x = self.starix
                                    self.y = self.stariy
                                    return False
                            else:
                                if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                                    self.x = self.starix
                                    self.y = self.stariy
                                    return False
                            self.x = self.starix - 150
                            if self.color == "white":
                                if king_checked(crni) != "None" or border_colision(self.x, self.y):
                                    self.x = self.starix
                                    self.y = self.stariy
                                    return False
                            else:
                                if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                                    self.x = self.starix
                                    self.y = self.stariy
                                    return False
                            ally_colision(self, novix, noviy).starix += 225
                            ally_colision(self, novix, noviy).x += 225
                            self.y = self.stariy
                            self.starix -= 150
                            self.castle = potez
                            return True
                    novix -= 75

        if (self.stariy - 77.5 <= self.y + 37.5 <= self.stariy + 2.5) and (
                self.starix - 2.5 <= self.x + 37.5 <= self.starix + 72.5):
            if (ally_colision(self, self.starix, self.stariy - 75) != 'None'):
                self.x = self.starix
                self.y = self.stariy
                return False
            if (enemy_colision(self, self.starix, self.stariy - 75) != 'None'):
                za_brisanje = enemy_colision(self, self.starix, self.stariy - 75)
                kontrola = 1
                if (self.color == 'white'):
                    crni.pop(crni.index(za_brisanje))
                else:
                    bijeli.pop(bijeli.index(za_brisanje))
            self.x = self.starix
            self.y = self.stariy - 75
            if self.color == "white":
                if king_checked(crni) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        crni.append(za_brisanje)
                    return False
            else:
                if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        bijeli.append(za_brisanje)
                    return False
            self.starix = self.x
            self.stariy = self.y
            self.castle = potez
            return True
        elif (self.stariy + 72.5 <= self.y + 37.5 <= self.stariy + 147.5) and (
                        self.starix - 2.5 <= self.x + 37.5 <= self.starix + 72.5):
            if (ally_colision(self, self.starix, self.stariy + 75) != 'None'):
                self.x = self.starix
                self.y = self.stariy
                return False
            if (enemy_colision(self, self.starix, self.stariy + 75) != 'None'):
                za_brisanje = enemy_colision(self, self.starix, self.stariy + 75)
                kontrola = 1
                if (self.color == 'white'):
                    crni.pop(crni.index(za_brisanje))
                else:
                    bijeli.pop(bijeli.index(za_brisanje))
            self.x = self.starix
            self.y = self.stariy + 75
            if self.color == "white":
                if king_checked(crni) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        crni.append(za_brisanje)
                    return False
            else:
                if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        bijeli.append(za_brisanje)
                    return False
            self.starix = self.x
            self.stariy = self.y
            self.castle = potez
            return True
        elif (self.starix - 77.5 <= self.x + 37.5 <= self.starix - 2.5) and (
                        self.stariy - 2.5 <= self.y + 37.5 <= self.stariy + 72.5):
            if (ally_colision(self, self.starix - 75, self.stariy) != 'None'):
                self.x = self.starix
                self.y = self.stariy
                return False
            if (enemy_colision(self, self.starix - 75, self.stariy) != 'None'):
                za_brisanje = enemy_colision(self, self.starix - 75, self.stariy)
                kontrola = 1
                if (self.color == 'white'):
                    crni.pop(crni.index(za_brisanje))
                else:
                    bijeli.pop(bijeli.index(za_brisanje))
            self.x = self.starix - 75
            self.y = self.stariy
            if self.color == "white":
                if king_checked(crni) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        crni.append(za_brisanje)
                    return False
            else:
                if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        bijeli.append(za_brisanje)
                    return False
            self.starix = self.x
            self.stariy = self.y
            self.castle = potez
            return True
        elif (self.starix + 72.5 <= self.x + 37.5 <= self.starix + 147.5) and (
                        self.stariy - 2.5 <= self.y + 37.5 <= self.stariy + 72.5):
            if (ally_colision(self, self.starix + 75, self.stariy) != 'None'):
                self.x = self.starix
                self.y = self.stariy
                return False
            if (enemy_colision(self, self.starix + 75, self.stariy) != 'None'):
                za_brisanje = enemy_colision(self, self.starix + 75, self.stariy)
                kontrola = 1
                if (self.color == 'white'):
                    crni.pop(crni.index(za_brisanje))
                else:
                    bijeli.pop(bijeli.index(za_brisanje))
            self.x = self.starix + 75
            self.y = self.stariy
            if self.color == "white":
                if king_checked(crni) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        crni.append(za_brisanje)
                    return False
            else:
                if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        bijeli.append(za_brisanje)
                    return False
            self.starix = self.x
            self.stariy = self.y
            self.castle = potez
            return True
        elif (self.stariy - 77.5 <= self.y + 37.5 <= self.stariy + 2.5) and (self.starix - 77.5 <= self.x + 37.5 <= self.starix - 2.5):
            if (ally_colision(self, self.starix - 75, self.stariy - 75) != 'None'):
                self.x = self.starix
                self.y = self.stariy
                return False
            if (enemy_colision(self, self.starix - 75, self.stariy - 75) != 'None'):
                za_brisanje = enemy_colision(self, self.starix - 75, self.stariy - 75)
                kontrola = 1
                if (self.color == 'white'):
                    crni.pop(crni.index(za_brisanje))
                else:
                    bijeli.pop(bijeli.index(za_brisanje))
            self.x = self.starix - 75
            self.y = self.stariy - 75
            if self.color == "white":
                if king_checked(crni) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        crni.append(za_brisanje)
                    return False
            else:
                if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        bijeli.append(za_brisanje)
                    return False
            self.starix = self.x
            self.stariy = self.y
            self.castle = potez
            return True
        elif (self.stariy - 77.5 <= self.y + 37.5 <= self.stariy + 2.5) and (self.starix + 72.5 <= self.x + 37.5 <= self.starix + 147.5):
            if (ally_colision(self, self.starix + 75, self.stariy - 75) != 'None'):
                self.x = self.starix
                self.y = self.stariy
                return False
            if (enemy_colision(self, self.starix + 75, self.stariy - 75) != 'None'):
                za_brisanje = enemy_colision(self, self.starix + 75, self.stariy - 75)
                kontrola = 1
                if (self.color == 'white'):
                    crni.pop(crni.index(za_brisanje))
                else:
                    bijeli.pop(bijeli.index(za_brisanje))
            self.x = self.starix + 75
            self.y = self.stariy - 75
            if self.color == "white":
                if king_checked(crni) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        crni.append(za_brisanje)
                    return False
            else:
                if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        bijeli.append(za_brisanje)
                    return False
            self.starix = self.x
            self.stariy = self.y
            self.castle = potez
            return True
        elif (self.stariy + 72.5 <= self.y + 37.5 <= self.stariy + 147.5) and (self.starix - 77.5 <= self.x + 37.5 <= self.starix - 2.5):
            if (ally_colision(self, self.starix - 75, self.stariy + 75) != 'None'):
                self.x = self.starix
                self.y = self.stariy
                return False
            if (enemy_colision(self, self.starix - 75, self.stariy + 75) != 'None'):
                za_brisanje = enemy_colision(self, self.starix - 75, self.stariy + 75)
                kontrola = 1
                if (self.color == 'white'):
                    crni.pop(crni.index(za_brisanje))
                else:
                    bijeli.pop(bijeli.index(za_brisanje))
            self.x = self.starix - 75
            self.y = self.stariy + 75
            if self.color == "white":
                if king_checked(crni) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        crni.append(za_brisanje)
                    return False
            else:
                if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        bijeli.append(za_brisanje)
                    return False
            self.starix = self.x
            self.stariy = self.y
            self.castle = potez
            return True
        elif (self.stariy + 72.5 <= self.y + 37.5 <= self.stariy + 147.5) and (self.starix + 72.5 <= self.x + 37.5 <= self.starix + 147.5):
            if (ally_colision(self, self.starix + 75, self.stariy + 75) != 'None'):
                self.x = self.starix
                self.y = self.stariy
                return False
            if (enemy_colision(self, self.starix + 75, self.stariy + 75) != 'None'):
                za_brisanje = enemy_colision(self, self.starix + 75, self.stariy + 75)
                kontrola = 1
                if (self.color == 'white'):
                    crni.pop(crni.index(za_brisanje))
                else:
                    bijeli.pop(bijeli.index(za_brisanje))
            self.x = self.starix + 75
            self.y = self.stariy + 75
            if self.color == "white":
                if king_checked(crni) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        crni.append(za_brisanje)
                    return False
            else:
                if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        bijeli.append(za_brisanje)
                    return False
            self.starix = self.x
            self.stariy = self.y
            self.castle = potez
            return True
        else:
            self.x = self.starix
            self.y = self.stariy
            return False

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

promotion = []
promotion.append(Queen(2.5, 2.5, 'white'))
promotion.append(Queen(2.5, 2.5, 'black'))
promotion.append(Rook(2.5, 2.5 + 75, 'white'))
promotion.append(Rook(2.5, 2.5 + 75, 'black'))
promotion.append(Bishop(2.5, 2.5 + 150, 'white'))
promotion.append(Bishop(2.5, 2.5 + 150, 'black'))
promotion.append(Knight(2.5, 2.5 + 225, 'white'))
promotion.append(Knight(2.5, 2.5 + 225, 'black'))


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
    promo = "None"
    while run:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
            if(promo == "None"):
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
                    moved = False

                    if objekat != "None":
                        if(potez%2 == 1):
                            moved = objekat.move(potez)
                        else:
                            moved = objekat.move(potez)
                        if moved:
                            if(objekat.obj == 'Pawn'):
                                if objekat.y == 2.5:
                                    promo = objekat
                                if objekat.y == 527.5:
                                    promo = objekat

                            potez += 1
                        if(king_checked(bijeli) != "None"):
                            print(king_checkmated(crni, potez))
                            if(king_checkmated(crni, potez) == True):
                                print("Black checkmated")
                        elif (king_checked(crni) != "None"):
                            if (king_checkmated(bijeli, potez) == True):
                                print("White checkmated")
                        else:
                            if ((king_checkmated(bijeli, potez) == True) or (king_checkmated(crni, potez) == True)):
                                print("Stalemate")
                    objekat = "None"
            else:
                WIN.fill(BLUE)
                for prom in promotion:
                    if promo.color == "white":
                        if(prom.color == "white"):
                            prom.draw(WIN)
                    else:
                        if (prom.color == "black"):
                            prom.draw(WIN)
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pressed = True
                    x, y = pygame.mouse.get_pos()
                    if 0 <= x <= 75 and 0<y<75:
                        if(promo.color == "white"):
                            bijeli.append(Queen(promo.x, 2.5, 'white'))
                            bijeli.pop(bijeli.index(promo))
                        else:
                            crni.append(Queen(promo.x, 527.5, 'black'))
                            crni.pop(crni.index(promo))
                        promo = "None"
                        continue
                    if 0 <= x <= 75 and 75 < y < 150:
                        if (promo.color == "white"):
                            bijeli.append(Rook(promo.x, 2.5, 'white'))
                            bijeli.pop(bijeli.index(promo))
                        else:
                            crni.append(Rook(promo.x, 527.5, 'black'))
                            crni.pop(crni.index(promo))
                        promo = "None"
                        continue
                    if 0 <= x <= 75 and 150 < y < 225:
                        if (promo.color == "white"):
                            bijeli.append(Bishop(promo.x, 2.5, 'white'))
                            bijeli.pop(bijeli.index(promo))
                        else:
                            crni.append(Bishop(promo.x, 527.5, 'black'))
                            crni.pop(crni.index(promo))
                        promo = "None"
                        continue
                    if 0 <= x <= 75 and 225 < y < 300:
                        if (promo.color == "white"):
                            bijeli.append(Knight(promo.x, 2.5, 'white'))
                            bijeli.pop(bijeli.index(promo))
                        else:
                            crni.append(Knight(promo.x, 527.5, 'black'))
                            crni.pop(crni.index(promo))
                        promo = "None"
                        continue



        if(promo == "None"):
            draw_window()



if __name__ == "__main__":
    main()