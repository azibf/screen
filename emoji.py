import pygame
from pygame.draw import *

pygame.init()

FPS = 30
clock = pygame.time.Clock()
finished = False


def emoji():
    screen = pygame.display.set_mode((400, 400))
    screen.fill((135, 135, 135))

    circle(screen, (255, 255, 0), (200, 200), 100)  # мордочка
    circle(screen, (0, 0, 0), (200, 200), 100, 2)  # обводка мордочки
    circle(screen, (255, 0, 0), (250, 175), 20)  # глаз 1
    circle(screen, (255, 0, 0), (150, 175), 25)  # глаз 2
    circle(screen, (0, 0, 0), (250, 175), 5)  # зрачки
    circle(screen, (0, 0, 0), (150, 175), 5)
    circle(screen, (0, 0, 0), (250, 175), 20, 2)  # обводка глаза 1
    circle(screen, (0, 0, 0), (150, 175), 25, 2)  # обводка глаза 2
    rect(screen, (0, 0, 0), (125, 230, 150, 20))  # рот
    polygon(screen, (0, 0, 0), ((190, 160), (100, 150), (100, 140), (190, 150)))  # бровь 1
    polygon(screen, (0, 0, 0), ((300, 130), (210, 160), (210, 170), (300, 140)))  # бровь 2
    pygame.display.update()
