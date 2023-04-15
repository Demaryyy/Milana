import pygame
from config import *
from Board import Board

pygame.init()
board = Board(W, H, 200)
screen = pygame.display.set_mode((W, H))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.click(event.pos)
            

    screen.fill('white')
    board.render(screen)
    pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit
        exit()
