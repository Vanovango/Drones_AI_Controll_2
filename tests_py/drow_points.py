import pygame


# Настройка игры
pygame.init()
gameScreen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pygame Mouse Click - Test Game')
FPS = 60
clock = pygame.time.Clock()

# Создание объекта
point = pygame.image.load("C:/Code/pythonProjects/Drones_AI_Controll_2/images/point.png")
line_color = (255, 0, 0)
font = pygame.font.Font(None, 36)
counter = 0

points = []


# Основной цикл игры
running = True
while running:
    # Обновление экрана
    gameScreen.fill((0, 0, 0))  # Заполнение экрана черным цветом

    # Рисуем имеющиеся точки
    if len(points) > 0:
        for point, x, y in points:
            gameScreen.blit(point, (x, y))

    # Рисуем надпись и пунктирную линию в зависимости от количества точек на экране
    if counter < 2:
        text = font.render(f"Осталось точек - {2 - counter}", True, (255, 255, 255))
        gameScreen.blit(text, (0, 0))
    else:
        text = font.render(f"Точки нанесены", True, (255, 0, 0))
        gameScreen.blit(text, (0, 0))
        # Рисование пунктирной линии
        pygame.draw.line(gameScreen, line_color,
                         (points[0][1] + 13, points[0][2] + 26),
                         (points[1][1] + 13, points[1][2] + 26),
                         1)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Если нажата кнопка мыши и точек меньше чем 2
        if event.type == pygame.MOUSEBUTTONDOWN and counter < 2:
            x, y = pygame.mouse.get_pos()  # Получение координат нажатия
            points.append([point, x - 13, y - 26])
            counter += 1

    # Обновление дисплея
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
