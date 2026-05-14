import pygame

from constants import WIDTH, HEIGHT, FPS
from gameClass import Game

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

game = Game(0, 0)

run = True

while run:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            x, y = pygame.mouse.get_pos()

            game.handle_click(x, y)

    WIN.fill((30, 30, 30))

    game.draw(WIN)

    pygame.display.update()

pygame.quit()