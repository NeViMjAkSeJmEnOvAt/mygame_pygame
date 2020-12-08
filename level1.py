import pygame
import random
from pygame import mixer
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 700
timer = 40
milisec = 0
background = pygame.image.load("source/level3.jpg")
pygame.display.set_caption('Superúžasná Hra Pog')

class Hrac(pygame.sprite.Sprite):
    def __init__(self):
        super(Hrac, self).__init__()
        self.surf = pygame.image.load("source/starship.png").convert()
        self.surf = pygame.transform.scale(self.surf, (100, 65))
        self.surf = pygame.transform.flip(self.surf, True, False)
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, pressed):
        if pressed[K_UP]:
            self.rect.move_ip(0, -3)
        if pressed[K_DOWN]:
            self.rect.move_ip(0, 3.5)
        if pressed[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed[K_RIGHT]:
            self.rect.move_ip(3.5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("source/enemy3.png")
        self.surf = pygame.transform.scale(self.surf, (50, 25))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 20),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        self.speed = random.uniform(2,5)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

mixer.init()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont('Comic Sans MS', 20)
infotext = font.render('Pro dokončení tohoto levelu potřebuješ přežít 60 sekund.', False, (255,255,255))
timetext1 = font.render("Čas: ", False, (255,255,255))

Pridat_nepritele = pygame.USEREVENT + 1
pygame.time.set_timer(Pridat_nepritele, 1200)

player = Hrac()

nepratele = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
#pygame.mixer.music.load("source/background_song.mp3")
#pygame.mixer.music.play(loops=-1)
#dead_sound = mixer.music.load("source/background_song.mp3")

running = True

while running:
    #pygame.time.delay(3)
    timetext2 = font.render(str(timer), False, (255, 255, 255))
    screen.blit(background, (0, 0))
    screen.blit(infotext, (0, 0))
    screen.blit(timetext1, (0, 30))

    print(milisec)
    print(timer)

    if milisec > 1000:
        timer -= 1
        milisec -= 1000

    if timer < 35: #hodnota 35, kvuli testovani
        import level2
        level2
        running = False

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

        elif event.type == Pridat_nepritele:
            new_enemy = Enemy()
            nepratele.add(new_enemy)
            all_sprites.add(new_enemy)


    screen.blit(timetext2, (45, 30))
    pressed = pygame.key.get_pressed()

    player.update(pressed)

    nepratele.update()

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, nepratele):
        #dead_sound
        player.kill()
        import main
        main
        running = False

    pygame.display.flip()
    milisec += pygame.time.Clock().tick_busy_loop(60)

mixer.music.stop()
mixer.quit()
pygame.quit()