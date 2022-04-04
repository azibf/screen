import pygame
import math
from pygame.draw import *
from pygame.color import *
from random import randint, choice
from math import pi
from lab3 import emoji

pygame.init()

FPS = 30
X = 750
Y = 400
clock = pygame.time.Clock()
finished = False


def _birds(n, screen):
    for i in range(n):
        a = randint(50, 100)
        b = randint(50, 150)
        x = randint(0, X - 2 * a)
        y = randint(0, Y - 2 * b)
        arc(screen, (0, 0, 0), (x, y, a, b), 0, pi/2, width=3)
        arc(screen, (0, 0, 0), (x + a, y, a, b), pi/2, pi, width=3)


def _curve(y_0, color, screen):  # функция, рисующая кривые гор
    graph = [lambda x: 10 * x ** (1 / 3),  # графики, задающие кривые гор
             lambda x: 20 * math.sin(x/50),
             lambda x: 50 * math.sin(x/50) / (x + 1)]
    x_cords = [0]
    y_cords = [y_0]
    quantity_curv = randint(3, 10)  # генерация количества смен кривых
    for i in range(quantity_curv):
        # выбор начальных и конечных значений координат для данной кривой
        x_start = x_cords[-1]
        x_end = randint(10, (i + 1) * X // quantity_curv) if i != quantity_curv - 1 else X
        y_start = y_cords[-1]
        current_graph = choice(graph)  # выбор кривой
        for i in range(x_start + 1, x_end + 1):
            x_cords.append(i)
            y_cords.append(y_start - current_graph(i - x_start))
    cords = [(0, 400)] + [(x_cords[i], y_cords[i]) for i in range(len(x_cords))] + [(X, Y)]
    polygon(screen, color, tuple(cords))


def main_picture(need_birds):  # отрисовка
    screen = pygame.display.set_mode((X, Y))
    screen.fill((254, 213, 162))
    rect(screen, (254, 213, 196), (0, 75, X, Y - 75))
    _curve(180, (252, 152, 49), screen)
    polygon(screen, (254, 213, 196), ((0, 400), (0, 215), (X, 125), (X, Y)))
    rect(screen, (254, 213, 148), (0, 215, X, Y - 215))
    _curve(270, (172, 67, 52), screen)
    polygon(screen, (179, 134, 148), ((0, 400), (0, 285), (X, 260), (X, Y)))
    circle(screen, THECOLORS["yellow"], (X/2, 75), 50)
    if need_birds == 1:  # если пользователь хочет картину с птичками
        _curve(350, (48, 16, 38), screen)
        _birds(randint(3, 5), screen)
    pygame.display.update()
