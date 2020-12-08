import pygame
from pygame.locals import (
    K_ESCAPE,
    QUIT,
    KEYDOWN,
    K_SPACE
)
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800



pygame.init()
pygame.font.init()
running = True
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
image = pygame.image.load("source/space.jpg")
font = pygame.font.SysFont('Comic Sans MS', 35)
text = font.render('Pro vstup do hry zmáčnki SPACE', False, (255,255,255))


while running:
    screen.blit(image, (0, 0))
    screen.blit(text, (125 , SCREEN_HEIGHT /2))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_SPACE:
                import level1
                level1
                running = False

        elif event.type == QUIT:
            running = False

    pygame.display.flip()

pygame.quit()