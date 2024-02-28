import pygame
pygame.init()

# 创建窗口 
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))  # 填充白色

# 设置标题 
pygame.display.set_caption('Hello World!')

# 绘制文本 
font = pygame.font.Font(None, 36)
text = font.render('Hello, pygame!', 1, (10, 10, 10))
screen.blit(text, (200, 200))
pygame.display.flip()  # 更新屏幕内容

# 保持窗口 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()