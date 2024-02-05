import pygame
import random
import math
 
# 初始化pygame
pygame.init()
 
# 设置窗口大小
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
 
# 定义颜色
black = (0, 0, 0)
 
# 定义烟花粒子
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # 随机颜色
        self.radius = random.randint(2, 4)
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(1, 3)
        self.gravity = 0.1
 
    def move(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed + self.gravity
        self.radius -= 0.1  # 粒子逐渐变小
 
    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.radius))
 
# 定义烟花
class Firework:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # 随机颜色
        self.particles = []
        self.exploded = False
        self.explode_height = random.randint(100, 400)  # 设置爆炸高度
 
        self.speed = random.randint(5, 10)  # 设置上升速度
        self.angle = math.pi / 2  # 设置上升角度为垂直向上
 
    def launch(self):
        if not self.exploded:
            self.y -= self.speed * math.sin(self.angle)
            if self.y <= self.explode_height:  # 到达设定高度后爆炸
                self.explode()
                self.exploded = True
 
    def explode(self):
        for _ in range(100):  # 爆炸产生的粒子数量
            self.particles.append(Particle(self.x, self.y))
 
    def draw(self):
        if not self.exploded:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 5)
        else:
            for particle in self.particles:
                particle.move()
                particle.draw()
 
# 主循环
fireworks = []
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(30)  # 控制帧率
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # 按键事件
            if event.key == pygame.K_ESCAPE:  # 按下Esc键退出
                running = False
            else:  # 按下其他键触发烟花
                fireworks.append(Firework(random.randint(0, width), height))
 
    screen.fill(black)
 
    # 发射烟花
    if random.randint(1, 20) == 1:  # 控制烟花发射频率
        fireworks.append(Firework(random.randint(0, width), height))
 
    # 更新烟花并绘制
    for firework in fireworks[:]:
        firework.launch()
        firework.draw()
        if firework.exploded and all(p.radius <= 0 for p in firework.particles):
            fireworks.remove(firework)
 
    pygame.display.flip()
 
pygame.quit()
