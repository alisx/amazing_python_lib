import sys
import pygame

# 初始化 Pygame
pygame.init()

size = width, height = 500, 500
speed = [1, 1]
black = 0, 0, 0

# 设置显示窗口的大小 
screen = pygame.display.set_mode(size)

# 加载一个要显示的球形图像 
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()

# 游戏主循环 
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()