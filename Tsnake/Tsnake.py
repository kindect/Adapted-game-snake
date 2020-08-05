# Author kindect@github/gitee
# Mail kindect@163.com
# Copyright 2020. All rights reserved.
# Using MulanPSL-2 as lisence, which can be seen here:https://license.coscl.org.cn/MulanPSL2

# offical repo address:https://gitee.com/kindect/Adapted-game-snake

# if you want to make a project using this file, keep the author notice here

# import part
import pygame
from pygame.locals import *
from time import sleep
from random import randint
import threading

pygame.init()
pygame.font.init()

# Global variable
DELAY = 0.1  # time before auto move(in sec, float)
# I suggest when you DEBUG, set the value to 0.5 or larger(depending on your speed :D), when release, set it back
WINDOW_WIDTH = 640  # must be BLOCK_SIZE*n
WINDOW_HEIGHT = 480  # same.
FOOD_AMOUNT = 3  # int >=1
POISON_AMOUNT = 3  # int >=0
BLOCK_SIZE = 20 # other size is OK, but not recommended(unless you have a extremely low resolution screen)
MAX_X = WINDOW_HEIGHT // BLOCK_SIZE # MAX of x the program can reach
MAX_Y = WINDOW_WIDTH // BLOCK_SIZE # same.

# x\y 0 .. MAX_Y
# 0
# 1
# .
# .
# MAX_X

# WINDOW_WIDTH*WINDOW_HEIGHT pixels
background_image = pygame.image.load('resource/background.png')

# 3/4 WINDOW_WIDTH * 1/4 WIDOW_HIGHT
dead_image=pygame.image.load('resource/dead.png')

# BLOCK_SIZE*BLOCK_SIZE pixel
body_image_1 = pygame.image.load('resource/body/1.png')
body_image_2 = pygame.image.load('resource/body/2.png')
body_image_3 = pygame.image.load('resource/body/3.png')
body_image_12 = pygame.image.load('resource/body/12.png')
body_image_13 = pygame.image.load('resource/body/13.png')
body_image_23 = pygame.image.load('resource/body/23.png')

head_image_0 = pygame.image.load('resource/head/0.png')
head_image_1 = pygame.image.load('resource/head/1.png')
head_image_2 = pygame.image.load('resource/head/2.png')
head_image_3 = pygame.image.load('resource/head/3.png')

food_image = pygame.image.load('resource/food.png')

poison_image = pygame.image.load('resource/poison.png')

font = pygame.font.SysFont('resource/Chalkboard.ttc', 30)


def pattern(op, direction):
    direction_p = 3 - direction
    return min(op, direction_p) * 10 + max(op, direction_p)


# noinspection PyGlobalUndefined
class Snake:
    def __init__(self, body=None, head=None, directions=None, head_direction=None):
        if directions is None:
            directions = [3] * 4
        if head is None:
            head = (0, 4)
        if body is None:
            body = [(0, 0), (0, 1), (0, 2), (0, 3)]
        if head_direction is None:
            head_direction = 3
        self.body = body
        self.head = head
        self.directions = directions
        self.head_direction = head_direction
        self.run = True
        threading.Thread(target=self.push).start()

    def print_p(self):
        exec('screen.blit(head_image_' + str(
            self.head_direction) + ',(self.head[1]*BLOCK_SIZE,self.head[0]*BLOCK_SIZE))')
        for i in range(len(self.body)):
            exec('screen.blit(body_image_' + str(
                self.directions[i]) + ',(self.body[i][1]*BLOCK_SIZE,self.body[i][0]*BLOCK_SIZE))')

    def move(self, direction):
        if direction + self.head_direction == 3:
            return
        next_p = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        tmp = (self.head[0] + next_p[direction][0], self.head[1] + next_p[direction][1])
        if tmp[0] >= MAX_X or tmp[0] < 0 or tmp[1] >= MAX_Y or tmp[1] < 0 or tmp in self.body or tmp in poisons:
            print('[INFO]: dead')
            run = False
            screen.blit(dead_image, (WINDOW_WIDTH/8, 0))
            sleep(1)
            for event in pygame.event.get():
                if event.key==K_y:
                    game_p.__init__()
                    return
                if event.key==K_n:
                    pygame.quit()
                    return
        self.body.append(self.head)
        self.directions.append(pattern(direction, self.head_direction))
        self.head = tmp
        self.head_direction = direction
        global foods
        if self.head in foods:
            if len(foods) <= 3:
                foods[foods.index(self.head)] = generate()
            else:
                del (foods[foods.index(self.head)])
        else:
            del (self.directions[0])
            del (self.body[0])

    def push(self):
        while run:
            sleep(DELAY)
            self.move(self.head_direction)


class Game:
    def print_p(self):
        screen.fill((255, 255, 255))
        screen.blit(background_image, (0, 0))
        user.print_p()
        for food in foods:
            screen.blit(food_image, (food[1] * BLOCK_SIZE, food[0] * BLOCK_SIZE))
        for poison in poisons:
            screen.blit(poison_image, (poison[1] * BLOCK_SIZE, poison[0] * BLOCK_SIZE))
        screen.blit(font.render(str((len(user.body) + 1) * 5), False, (255, 200, 10)), (10, 10))
        pygame.time.Clock().tick(60)
        pygame.display.update()
    def mainloop(self):
        while run:
            key_list = pygame.key.get_pressed()
            for event in pygame.event.get():
                # event queue
                if event.type == QUIT:
                    print('[INFO]: exit requested')
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT or key_list[K_LEFT]:
                        print('[INFO]: left pressed')
                        user.move(0)
                    if event.key == K_RIGHT or key_list[K_RIGHT]:
                        print('[INFO]: right pressed')
                        user.move(3)
                    if event.key == K_UP or key_list[K_UP]:
                        print('[INFO]: up pressed')
                        user.move(1)
                    if event.key == K_DOWN or key_list[K_DOWN]:
                        print('[INFO]: down pressed')
                        user.move(2)
            self.print_p()

def generate():
    tmp = (randint(0, MAX_X - 1), randint(0, MAX_Y - 1))
    if tmp in user.body or tmp == user.head or tmp in foods or tmp in poisons:
        generate()
    return tmp


if __name__ == '__main__':
    # perform a check
    if WINDOW_WIDTH % BLOCK_SIZE != 0:
        print('[Error]: Bad WINDOW_WIDTH WINDOW_HEIGHT')
    
    # for pygame to init itself
    screen = pygame.display.set_mode((1,1),0)
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
    pygame.display.set_caption('T_snake')
    
    # variables for the whole program
    foods = []
    poisons = []
    run=True
    user=Snake()
    game_p = Game()
    for i in range(FOOD_AMOUNT):
        foods.append(generate())
    for i in range(POISON_AMOUNT):
        poisons.append(generate())
    game_p.mainloop()
