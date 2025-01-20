import pygame
import pygame_widgets
from pygame_widgets.button import Button

# Настройка Pygame
pygame.init()
win = pygame.display.set_mode((600, 600))
FPS = 60
clock = pygame.time.Clock()
running = True

# Создание кнопки с опциональными параметрами
button = Button(
    # Обязательные параметры
    win,  # Поверхность для размещения кнопки
    100,  # X-координата верхнего левого угла
    100,  # Y-координата верхнего левого угла
    300,  # Ширина
    150,  # Высота

    # Опциональные параметры
    text='Hello',  # Текст для отображения
    fontSize=50,  # Размер шрифта
    margin=20,  # Минимальное расстояние между текстом/изображением и краем кнопки
    inactiveColour=(200, 50, 0),  # Цвет кнопки, когда с ней не взаимодействуют
    hoverColour=(150, 0, 0),  # Цвет кнопки при наведении на неё мыши
    pressedColour=(0, 200, 20),  # Цвет кнопки при нажатии на неё
    radius=20,  # Радиус углов границы (можно оставить пустым для некруглых)
    onClick=lambda: print('Click')  # Функция, которая будет вызываться при нажатии на кнопку
)

while running:
    # Обновление экрана
    win.fill((0, 0, 0))  # Заполнение экрана черным цветом

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.button

    # Обновление дисплея
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
