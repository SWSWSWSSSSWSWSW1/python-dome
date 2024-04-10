# 导入所需模块
import pygame
import sys
from pygame.locals import *
from random import randint
import random

# 定义一些常量和数据
SCREEN_WIDTH = 1366  # 屏幕宽度
SCREEN_HEIGHT = 768  # 屏幕高度
LOW_SPEED = 5  # 文字下落最低速度
HIGH_SPEED = 10  # 文字下落最高速度
LOW_SIZE = 5  # 文字最小尺寸
HIGH_SIZE = 30  # 文字最大尺寸
FONT_SIZE = 25  # 字体大小
FONT_NAME = "arial"  # 字体名称
FREQUENCE = 50  # 控制帧率
times = 0  # 计数器

# 随机生成颜色函数
def randomcolor():
    # 返回一个随机的颜色
    return (50, 205, 50)  # 固定颜色 (50, 205, 50) 用于显示文字

# 随机生成速度函数
def randomspeed():
    return randint(LOW_SPEED, HIGH_SPEED)  # 返回一个介于 LOW_SPEED 和 HIGH_SPEED 之间的随机数作为下落速度

# 随机生成初始位置函数
def randomposition():
    return (randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT))  # 返回一个随机的起始位置

# 随机生成文字大小函数
def randomsize():
    return randint(LOW_SIZE, HIGH_SIZE)  # 返回一个介于 LOW_SIZE 和 HIGH_SIZE 之间的随机数作为文字大小

# 随机生成文字值（这里是模拟生成的随机数）
def randomvalue():
    array = [1, 0, 2, 4]  # 模拟的随机数值
    return random.choice(array)  # 从数组中随机选择一个值作为文字显示

# 文字精灵类
class Word(pygame.sprite.Sprite):
    def __init__(self, bornposition):
        pygame.sprite.Sprite.__init__(self)
        self.value = randomvalue()  # 随机生成文字值
        self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)  # 使用指定字体和大小创建字体对象
        self.image = self.font.render(str(self.value), True, randomcolor())  # 创建渲染后的文字图像
        self.speed = randomspeed()  # 随机生成下落速度
        self.rect = self.image.get_rect()  # 获取文字图像的矩形区域
        self.rect.topleft = bornposition  # 设置文字初始位置

    def update(self):
        self.rect = self.rect.move(0, self.speed)  # 更新文字位置，使其向下移动
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()  # 如果文字超出屏幕下方，移除该文字精灵

# 初始化 Pygame
pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("HACKER EMPIRE CAPTION RAIN")  # 设置窗口标题

# 创建游戏时钟对象
clock = pygame.time.Clock()

# 创建精灵组
group = pygame.sprite.Group()

# 计算每行能容纳的文字数量
group_count = SCREEN_WIDTH // FONT_SIZE

# 游戏主循环
while True:
    time = clock.tick(FREQUENCE)  # 控制游戏帧率

    # 处理事件
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # 填充屏幕背景色
    screen.fill((0, 0, 0))

    # 在每行随机生成一个文字精灵，并添加到精灵组中
    for i in range(0, group_count):
        group.add(Word((i * FONT_SIZE, -FONT_SIZE)))

    # 更新精灵组中的所有文字精灵
    group.update()

    # 绘制精灵组中的所有文字精灵到屏幕上
    group.draw(screen)

    # 更新显示
    pygame.display.update()
