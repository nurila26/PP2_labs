import pygame 
import time
import math
pygame.init()

#размеры экрана
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

#название экрана
pygame.display.set_caption("Mickey clock")

#добавляем изоброжения на экран
leftarm = pygame.image.load("lab_7/images/sec_hand.png")
rightarm = pygame.image.load("lab_7/images/min_hand.png")
mainclock = pygame.transform.scale(pygame.image.load("lab_7/images/clock.png"), (800, 600))

done = False

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # через localtime определяем секунды и минуты
    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec
    
    #определяем угол минуты и секунды 
    #минута * 360 градус / 60 минут + секунда
    minute_angle = minute * 6    + (second / 60) * 6   
    second_angle = second * 6  
    
    #вывести на экран с фоном
    screen.blit(mainclock, (0,0))
    
    #добавление правой руки(минута)
    rotated_rightarm = pygame.transform.rotate(pygame.transform.scale(rightarm, (800, 600)), -minute_angle)
    rightarmrect = rotated_rightarm.get_rect(center=(800 // 2, 600 // 2 + 12))
    screen.blit(rotated_rightarm, rightarmrect)
    
    #добовление левой руки(секунда)
    rotated_leftarm = pygame.transform.rotate(pygame.transform.scale(leftarm, (40.95, 682.5)), -second_angle)
    leftarmrect = rotated_leftarm.get_rect(center=(800 // 2, 600 // 2 + 10))
    screen.blit(rotated_leftarm, leftarmrect)
    
    pygame.display.flip() #обновление окна
    clock.tick(60) #fps
    
pygame.quit()