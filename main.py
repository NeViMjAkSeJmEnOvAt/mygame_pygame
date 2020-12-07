import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Hrac(pygame.sprite.Sprite):
    def __init__(self):
        super(Hrac, self).__init__()
        self.surf = pygame.Surface((100, 100))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    def update(self, pressed):
        if pressed[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed[K_RIGHT]:
            self.rect.move_ip(1, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Hrac()

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False
    pressed = pygame.key.get_pressed()

    player.update(pressed)

    screen.fill((0, 0, 0))

    screen.blit(player.surf, player.rect)

    pygame.display.flip()

pygame.quit()