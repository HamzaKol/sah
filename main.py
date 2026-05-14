# Fale:
# neki win screen nakon checkmatea,
# neki meni, mozda ljepsi izgled malo, indikator za check,
# 50 move rule
# Zvukovi
# za_brisanje = "None" dodati u checkmated

import pygame

from kingHelperFunctions import king_checked, king_checkmated
from pieceClasses import Bishop, King, Knight, Pawn, Queen, Rook
from constants import BLUE, FPS, HEIGHT, WHITE, WIDTH, bijeli, crni

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

SQUARE = pygame.Rect(0, 0, 75, 75)
squares = []


for i in range(8):
    red = []
    for j in range(8):
        red.append(pygame.Rect(i*75, j*75, 75, 75))
    squares.append(red)

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