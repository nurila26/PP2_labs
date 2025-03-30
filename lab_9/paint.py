import pygame

# Определение ширины и высоты окна игры
WIDTH, HEIGHT = 1200, 800
# Частота обновления экрана
FPS = 90
# Флаг, указывающий, рисуем ли на экране
draw = False
# Радиус кисти
radius = 2
# Цвет по умолчанию
color = 'blue'
# Режим инструмента по умолчанию
mode = 'pen'

# Инициализация Pygame
pygame.init()
# Создание окна заданного размера
screen = pygame.display.set_mode([WIDTH, HEIGHT])
# Установка заголовка окна
pygame.display.set_caption('Paint')
# Создание объекта Clock для управления временем
clock = pygame.time.Clock()
# Заполнение экрана белым цветом
screen.fill(pygame.Color('white'))
# Создание шрифта для отображения текста
font = pygame.font.SysFont('None', 60)

def drawLine(screen, start, end, width, color):
    # Извлечение координат x и y начальной и конечной точек
    x1, y1 = start
    x2, y2 = end

    # Вычисление абсолютных разностей координат
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    # Коэффициенты для уравнения прямой Ax + By + C = 0
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    # Если линия более горизонтальная, чем вертикальная
    if dx > dy:
        # Гарантируем, что x1 находится левее x2
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        # Итерация по координатам x
        for x in range(x1, x2):
            # Вычисление координаты y с использованием уравнения прямой
            y = (-C - A * x) / B
            # Рисование круга (пикселя) в позиции (x, y)
            pygame.draw.circle(screen, pygame.Color(color), (int(x), int(y)), width)
    # Если линия более вертикальная, чем горизонтальная
    else:
        # Гарантируем, что y1 ниже y2
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        # Итерация по координатам y
        for y in range(y1, y2):
            # Вычисление координаты x с использованием уравнения прямой
            x = (-C - B * y) / A
            # Рисование круга (пикселя) в позиции (x, y)
            pygame.draw.circle(screen, pygame.Color(color), (int(x), int(y)), width)

def drawCircle(screen, start, end, width, color):
    # Извлечение координат x и y начальной и конечной точек
    x1, y1 = start
    x2, y2 = end

    # Вычисление центра круга
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2

    # Вычисление радиуса круга
    radius = abs(x1 - x2) / 2

    # Рисование круга на экране
    pygame.draw.circle(screen, pygame.Color(color), (int(x), int(y)), int(radius), width)

def drawRectangle(screen, start, end, width, color):
    # Извлечение координат x и y начальной и конечной точек
    x1, y1 = start
    x2, y2 = end

    # Вычисление ширины и высоты прямоугольника
    widthr = abs(x1 - x2)
    height = abs(y1 - y2)

    # Определение верхнего левого угла прямоугольника
    top_left_x = min(x1, x2)
    top_left_y = min(y1, y2)

    # Рисование прямоугольника на экране
    pygame.draw.rect(screen, pygame.Color(color), (top_left_x, top_left_y, widthr, height), width)

def drawSquare(screen, start, end, color):
    # Извлечение координат x и y начальной и конечной точек
    x1, y1 = start
    x2, y2 = end

    # Вычисление стороны квадрата как минимального расстояния между точками по осям x и y
    side_length = min(abs(x2 - x1), abs(y2 - y1))

    # Определение верхнего левого угла квадрата
    top_left_x = min(x1, x2)
    top_left_y = min(y1, y2)

    # Рисование квадрата на экране
    pygame.draw.rect(screen, pygame.Color(color), (top_left_x, top_left_y, side_length, side_length))

def drawRightTriangle(screen, start, end, color):
    # Извлечение координат x и y начальной и конечной точек
    x1, y1 = start
    x2, y2 = end

    # Определение третьей точки прямоугольного треугольника
    if x2 > x1 and y2 > y1:
        third_point = (x1, y2)
    elif y2 > y1 and x1 > x2:
        third_point = (x1, y2)
    elif x1 > x2 and y1 > y2:
        third_point = (x2, y1)
    else:  # x2 > x1 and y1 > y2
        third_point = (x2, y1)

    # Рисование прямоугольного треугольника на экране
    pygame.draw.polygon(screen, pygame.Color(color), [start, end, third_point])
    def drawEquilateralTriangle(screen, start, end, width, color):
    # Извлечение координат x и y начальной и конечной точек
    x1, y1 = start
    x2, y2 = end

    # Вычисление длины стороны треугольника
    side_length = abs(x2 - x1)

    # Вычисление высоты равностороннего треугольника
    height = (3**0.5) * side_length / 2

    # Определение координат третьей вершины треугольника
    if y2 > y1:
        third_point = ((x1 + x2) / 2, y2 - height)
    else:
        third_point = ((x1 + x2) / 2, y1 - height