import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Размер окна
WIDTH, HEIGHT = 500, 500
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
defeat_colour = (255, 0, 0)

# Настройки змейки
SPEED = 5
BLOCK_SIZE = 20

clock = pygame.time.Clock()

# Класс змейки
class Snake:
    def __init__(self):
        self.history = [[100, 100]]  # Начальная позиция головы
        self.direction = "RIGHT"
        self.grow_next = False  # Флаг роста змейки

    def move(self):
        x, y = self.history[0]  # Текущая голова змейки

        # Движение в зависимости от направления
        if self.direction == "UP":
            y -= BLOCK_SIZE
        elif self.direction == "DOWN":
            y += BLOCK_SIZE
        elif self.direction == "LEFT":
            x -= BLOCK_SIZE
        elif self.direction == "RIGHT":
            x += BLOCK_SIZE

        # Добавляем новую голову
        self.history.insert(0, [x, y])

        # Если не надо расти — удаляем последний элемент
        if not self.grow_next:
            self.history.pop()
        else:
            self.grow_next = False  # Сбрасываем флаг

    def grow(self):
        self.grow_next = True  # Активируем рост

    def death(self):
        # Проверка столкновения с собой
        return self.history[0] in self.history[1:]

    def reset(self):
        # Сброс змейки
        self.__init__()

# Класс еды
class Food:
    def __init__(self):
        self.position = [random.randint(0, (WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE,
                         random.randint(0, (HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE]
        self.weight = random.randint(1, 3)  # Вес еды (1-3)
        self.spawn_time = time.time()  # Время появления

    def draw(self):
        # Цвет еды зависит от веса
        color = RED if self.weight == 1 else BLUE if self.weight == 2 else GREEN
        pygame.draw.rect(display, color, (*self.position, BLOCK_SIZE, BLOCK_SIZE))

    def expired(self):
        # Еда исчезает через 5 секунд
        return time.time() - self.spawn_time > 5

def gameLoop():
    global SPEED

    snake = Snake()
    food = Food()
    score = 0
    level = 1
    running = True

    while running:
        display.fill(WHITE)  # Очистка экрана

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != "DOWN":
                    snake.direction = "UP"
                elif event.key == pygame.K_DOWN and snake.direction != "UP":
                    snake.direction = "DOWN"
                elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                    snake.direction = "LEFT"
                elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                    snake.direction = "RIGHT"

        # Движение змейки
        snake.move()

        # Отрисовка змейки
        for block in snake.history:
            pygame.draw.rect(display, GREEN, (*block, BLOCK_SIZE, BLOCK_SIZE))

        # Проверка поедания еды
        if snake.history[0] == food.position:
            score += food.weight  # Увеличиваем счет на вес еды
            level += 1  # Увеличиваем уровень
            SPEED += 1  # Ускоряем змейку
            snake.grow()  # Увеличиваем длину змейки
            food = Food()  # Создаем новую еду

        # Проверка истечения времени еды
        if food.expired():
            food = Food()

        # Отрисовка еды
        food.draw()

        # Проверка столкновения с собой
        if snake.death():
            score = 0
            level = 1
            SPEED = 5
            font = pygame.font.SysFont(None, 100)
            text = font.render("Game Over!", True, defeat_colour)
            display.blit(text, (50, 200))
            pygame.display.update()
            time.sleep(3)
            snake.reset()
            # Проверка выхода за границы (телепортация на противоположную сторону)
        if snake.history[0][0] >= WIDTH:
            snake.history[0][0] = 0
        elif snake.history[0][0] < 0:
            snake.history[0][0] = WIDTH - BLOCK_SIZE
        if snake.history[0][1] >= HEIGHT:
            snake.history[0][1] = 0
        elif snake.history[0][1] < 0:
            snake.history[0][1] = HEIGHT - BLOCK_SIZE

        pygame.display.update()
        clock.tick(SPEED)  # Управление скоростью игры

gameLoop()
pygame.quit()