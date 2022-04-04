import pygame
from math import pi
from emoji import emoji
from picture import main_picture

pygame.init()

FPS = 30
X = 750
Y = 400
clock = pygame.time.Clock()
finished = False


if __name__ == "__main__":
    print("""Привет!
Я РИСОВАТОР2000
Нарисую Вам целых три картинки!
Введите 1, чтобы я нарисовал злой смайлик
Введите 2, чтобы я нарисовал горы
Введите 3, чтобы я нарисовал горы с птичками""")
    while not finished:
        clock.tick(FPS)
        a = input("Введите 1, 2 или 3\n")
        if a == '1':  # обработка выбора пользователя и вызов соответствующих функций
            emoji()
        elif a == '2':
            main_picture(0)
        elif a == '3':
            main_picture(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()