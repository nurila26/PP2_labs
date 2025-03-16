import pygame
import os

pygame.init()

# Путь к папке с музыкой
music_folder = r"C:\Users\nuril\PP2_labs\lab_7\music"
allmusic = os.listdir(music_folder)

# Плейлист, добавляем только .mp3 файлы
playlist = []
for song in allmusic:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(music_folder, song))

# Инициализация экрана и фона
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Darkhan-Juzz")
clock = pygame.time.Clock()

# Фон экрана
background = pygame.image.load(os.path.join("lab_7", "music-elements", "background.jpg"))

# Панель с кнопками
bg = pygame.Surface((500, 200))
bg.fill((255, 255, 255))

# Шрифт для вывода названия трека
font2 = pygame.font.SysFont(None, 20)

# Кнопки (используем изображения)
playb = pygame.image.load(os.path.join("lab_7", "music-elements", "play.jpg"))
pausb = pygame.image.load(os.path.join("lab_7", "music-elements", "pause.jpg"))
nextb = pygame.image.load(os.path.join("lab_7", "music-elements", "next.jpg"))
prevb = pygame.image.load(os.path.join("lab_7", "music-elements", "back.jpg"))

# Инициализация воспроизведения
index = 0
aplay = False
pygame.mixer.music.load(playlist[index])
pygame.mixer.music.play(loops=0, start=0.0)
aplay = True

# Функции для обработки нажатия на кнопки
def check_button_click(pos):
    global aplay, index
    # Проверка для кнопки Play/Pause
    if 370 <= pos[0] <= 440 and 590 <= pos[1] <= 660:
        if aplay:
            aplay = False
            pygame.mixer.music.pause()
        else:
            aplay = True
            pygame.mixer.music.unpause()

    # Проверка для кнопки Next
    elif 460 <= pos[0] <= 530 and 587 <= pos[1] <= 657:
        index = (index + 1) % len(playlist)
        pygame.mixer.music.load(playlist[index])
        pygame.mixer.music.play()

    # Проверка для кнопки Prev
    elif 273 <= pos[0] <= 348 and 585 <= pos[1] <= 660:
        index = (index - 1) % len(playlist)
        pygame.mixer.music.load(playlist[index])
        pygame.mixer.music.play()

# Главный цикл
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()

        # Обработка кликов мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                check_button_click(event.pos)

    # Отображение информации на экране
    text2 = font2.render(os.path.basename(playlist[index]), True, (20, 20, 50))

    # Центрируем фон, но смещаем его немного вверх
    bg_width, bg_height = background.get_size()
    screen_width, screen_height = screen.get_size()

    # Позиция для фона, чтобы он был в центре, но смещен немного вверх
    x_pos = (screen_width - bg_width) // 2
    y_pos = (screen_height - bg_height) // 2 - 100  # Сдвигаем фон вверх на 100 пикселей

    # Отображаем фон и панель с кнопками
    screen.blit(background, (x_pos, y_pos))  # Фон теперь в центре, но сдвинут вверх
    screen.blit(bg, (155, 500))
    screen.blit(text2, (365, 520))

    # Изменяем размер кнопок
    playb = pygame.transform.scale(playb, (70, 70))
    pausb = pygame.transform.scale(pausb, (70, 70))

    # Кнопка "Пауза/Играть"
    if aplay:
        screen.blit(pausb, (370, 590))
    else:
        screen.blit(playb, (370, 590))

    # Кнопка "Следующий трек"
    nextb = pygame.transform.scale(nextb, (70, 70))
    screen.blit(nextb, (460, 587))

    # Кнопка "Предыдущий трек"
    prevb = pygame.transform.scale(prevb, (75, 75))
    screen.blit(prevb, (273, 585))

    clock.tick(24)
    pygame.display.update()