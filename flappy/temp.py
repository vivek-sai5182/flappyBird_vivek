import pygame
import random
from random import randint

# Flappy Bird Class
class Flap(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        flapy = pygame.image.load("D:\python Games\\flappy\\flappy.png")
        self.image = flapy
        self.rect = self.image.get_rect(center=(400, 400))
        self.gravity = 0

    def player_input(self):
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            self.gravity = -4  # Stronger jump

    def gravityFunc(self):
        self.gravity += 0.2  # Faster fall
        self.rect.y += int(self.gravity)

        # Stop bird at ground level
        if self.rect.bottom >= 500:
            self.rect.bottom = 500
            self.gravity = 0

    def update(self):
        self.player_input()
        self.gravityFunc()

# Pipe Class
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        pipes = pygame.image.load("D:\python Games\\flappy\\pipes.png")
        self.image = pipes
        self.rect = self.image.get_rect(center=(x, randint(130, 400)))

    def animation(self):
        self.rect.x -= 4
        if self.rect.right < 0:
            self.kill()

    def update(self):
        self.animation()

# Initialization
pygame.init()
window = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

game_stat = True
run = True

# Class Instances
play_bird = pygame.sprite.GroupSingle()
play_bird.add(Flap())
ob_pipe = pygame.sprite.Group()

# Background
sky = pygame.image.load("D:\python Games\\flappy\\back_sky.jpg")

# User Events
piper = pygame.USEREVENT + 1
pygame.time.set_timer(piper, 1600)

# Game Loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == piper:
            ob_pipe.add(Pipe(850))  # Consistent pipe position

    if game_stat:
        window.blit(sky, (0, 0))
        play_bird.draw(window)
        play_bird.update()
        ob_pipe.draw(window)
        ob_pipe.update()

    # Updates
    clock.tick(60)
    pygame.display.update()
