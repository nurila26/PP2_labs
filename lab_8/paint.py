import pygame 
 
WIDTH, HEIGHT = 1200, 800  # Определяет ширину и высоту игрового окна.
FPS = 90  # Частота обновления экрана

# Переменные для рисования
draw = False   # Указывает, нужно ли рисовать на экране            
radius = 2    # Радиус кисти
color = 'blue'           
mode = 'pen'  # Текущий режим рисования

pygame.init() 
screen = pygame.display.set_mode([WIDTH, HEIGHT])  # Создание окна заданных размеров
pygame.display.set_caption('Paint')  # Название окна
clock = pygame.time.Clock()  # Для управления временем
screen.fill(pygame.Color('white'))  # Заполняет экран белым цветом.
font = pygame.font.SysFont('None', 60)  # Создание шрифта для отображения текста

def drawLine(screen, start, end, width, color): 
    # Извлекаем координаты начальной и конечной точек
    x1, y1 = start
    x2, y2 = end
    
    # Вычисляем абсолютные разницы по осям
    dx = abs(x1 - x2) 
    dy = abs(y1 - y2) 
    
    # Коэффициенты уравнения прямой Ax + By + C = 0
    A = y2 - y1  # Вертикально
    B = x1 - x2  # Горизонтально
    C = x2 * y1 - x1 * y2 
    
    # Если линия больше горизонтальная, чем вертикальная
    if dx > dy: 
        if x1 > x2:  # Переставляем точки местами, если нужно
            x1, x2 = x2, x1 
            y1, y2 = y2, y1 
        for x in range(x1, x2): 
            y = (-C - A * x) / B  # Вычисляем y
            pygame.draw.circle(screen, pygame.Color(color), (x, int(y)), width) 
    else:  # Если линия больше вертикальная
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2): 
            x = (-C - B * y) / A  # Вычисляем x
            pygame.draw.circle(screen, pygame.Color(color), (int(x), y), width)

# Остальные функции аналогично, только переведены комментарии.

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            exit()  # Выход из программы при закрытии окна

        # Обработка событий клавиатуры
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_r: 
                mode = 'rectangle'  # Режим рисования прямоугольника
            if event.key == pygame.K_c: 
                mode = 'circle'  # Режим рисования круга
            if event.key == pygame.K_p: 
                mode = 'pen'  # Режим рисования карандашом
            if event.key == pygame.K_e: 
                mode = 'erase'  # Режим стирания
            if event.key == pygame.K_s: 
                mode = 'square'  # Режим рисования квадрата
            if event.key == pygame.K_q: 
                screen.fill(pygame.Color('white'))  # Очистка экрана

            # Изменение цвета
            if event.key == pygame.K_1: 
                color = 'black'  # Чёрный
            if event.key == pygame.K_2: 
                color = 'green'  # Зелёный
            if event.key == pygame.K_3: 
                color = 'red'  # Красный
            if event.key == pygame.K_4: 
                color = 'blue'  # Синий
            if event.key == pygame.K_5: 
                color = 'yellow'  # Жёлтый

        # Обработка событий мыши
        if event.type == pygame.MOUSEBUTTONDOWN:  
            draw = True  # Включение режима рисования
            if mode == 'pen': 
                pygame.draw.circle(screen, pygame.Color(color), event.pos, radius)  # Рисование точки
            prevPos = event.pos  # Сохранение позиции

        if event.type == pygame.MOUSEBUTTONUP:  
            draw = False  # Отключение рисования

        if event.type == pygame.MOUSEMOTION:  
            if draw and mode == 'pen': 
                drawLine(screen, lastPos, event.pos, radius, color)  # Рисование линии
            elif draw and mode == 'erase': 
                drawLine(screen, lastPos, event.pos, radius, 'white')  # Стирание
            lastPos = event.pos  # Обновление последней позиции

    pygame.display.flip()  # Обновление экрана
    clock.tick(FPS)  # Контроль частоты кадров


