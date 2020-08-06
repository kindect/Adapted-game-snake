# Author kindect@github/gitee
# Mail kindect@163.com
# Copyright 2020. All rights reserved.
# Using MulanPSL-2 as license, which can be seen here:https://license.coscl.org.cn/MulanPSL2
# devoted to zxx.

# official repo address:https://gitee.com/kindect/Adapted-game-snake

# if you want to make a project using this file, keep the author notice here

# (x,y) definition
# x\y 0 .. MAX_Y
# 0
# 1
# .
# .
# MAX_X

# direction notice(int)

# 0 means left
# 3 means right
# 1 means up
# 2 means down

# so up+down=left+right=3


# import part
import pygame
from pygame.locals import *
from time import sleep
# from time import time
from random import randint
import threading

pygame.mixer.pre_init(48000, 16, 2, 4096)
pygame.init()
pygame.font.init()
pygame.mixer.init()

# Global variable
DELAY = 0.1  # time before auto move(in sec, float)
# I suggest when you DEBUG, set the value to 0.5 or larger(depending on your speed :D), when release, set it back
WINDOW_WIDTH = 640  # must be BLOCK_SIZE*n
WINDOW_HEIGHT = 480  # same.
FOOD_AMOUNT = 3  # int >=1
POISON_AMOUNT = 3  # int >=0
BLOCK_SIZE = 20  # other size is OK, but not recommended(unless you have a extremely low resolution screen)
MAX_X = WINDOW_HEIGHT // BLOCK_SIZE  # MAX of x the program can reach
MAX_Y = WINDOW_WIDTH // BLOCK_SIZE  # same.
FONT_SIZE = 30
FRAME_RATE = 60

# WINDOW_WIDTH*WINDOW_HEIGHT pixels
background_image = pygame.image.load('resource/background.png')

# 3/4 WINDOW_WIDTH * 1/4 WIDOW_HEIGHT
# not enabled due to Bug#3
# dead_image=pygame.image.load('resource/dead.png')

# BLOCK_SIZE*BLOCK_SIZE pixel
body_image_1 = pygame.image.load('resource/body/1.png')
body_image_2 = pygame.image.load('resource/body/2.png')
body_image_3 = pygame.image.load('resource/body/3.png')
body_image_12 = pygame.image.load('resource/body/12.png')
body_image_13 = pygame.image.load('resource/body/13.png')
body_image_23 = pygame.image.load('resource/body/23.png')

# BLOCK_SIZE*BLOCK_SIZE pixel
head_image_0 = pygame.image.load('resource/head/0.png')
head_image_1 = pygame.image.load('resource/head/1.png')
head_image_2 = pygame.image.load('resource/head/2.png')
head_image_3 = pygame.image.load('resource/head/3.png')

# BLOCK_SIZE*BLOCK_SIZE pixel
food_image = pygame.image.load('resource/food.png')

# BLOCK_SIZE*BLOCK_SIZE pixel
poison_image = pygame.image.load('resource/poison.png')

font = pygame.font.SysFont('resource/Chalkboard.ttc', FONT_SIZE)

if WINDOW_WIDTH % BLOCK_SIZE != 0:
    print('[Error]: Bad WINDOW_WIDTH WINDOW_HEIGHT')

# for pygame to init itself
screen = pygame.display.set_mode((1, 1), 0)
# noinspection PyRedeclaration
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('T_snake')

background_music = pygame.mixer.Sound('resource/background.wav')
dead_music = pygame.mixer.Sound('resource/dead.wav')


def pattern(op, direction):
    # this is a function to return how the snake should look like
    # op means the direction head was heading, direction means the head is now heading
    direction_p = 3 - direction
    # return should be direction_p(PEP regulations), op return statement is only to find the smallest and the biggest
    # and put them in order(since we don't have body_image_30, we only have body_image_3)
    return min(op, direction_p) * 10 + max(op, direction_p)


class Snake:
    def __init__(self, body=None, head=None, directions=None, head_direction=None):
        # vars explained: body is list[tuple] from tail to head(not included)->(tail,head], tuple in (x,y),
        # mentioned above body_direction is used for the program to print the snake boy in a beautiful way,
        # direction is smallest number in direction with biggest, like 03(3), 23, 31->13 PEP regulations
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

    def print_p(self):
        # only print the snake itself might have security issues, but it is a game for fun, test security issues as
        # you want.(without modifying the const string)
        exec('screen.blit(head_image_' + str(
            self.head_direction) + ',(self.head[1]*BLOCK_SIZE,self.head[0]*BLOCK_SIZE))')
        for i in range(len(self.body)):
            exec('screen.blit(body_image_' + str(
                self.directions[i]) + ',(self.body[i][1]*BLOCK_SIZE,self.body[i][0]*BLOCK_SIZE))')

    def move(self, direction):
        # noinspection PyGlobalUndefined
        global run, exit_p
        if direction + self.head_direction == 3:
            # if the user want to head the opposite direction, kill the process
            return
        next_p = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        tmp = (self.head[0] + next_p[direction][0], self.head[1] + next_p[direction][1])
        if tmp[0] >= MAX_X or tmp[0] < 0 or tmp[1] >= MAX_Y or tmp[1] < 0 or tmp in self.body or tmp in poisons:
            # it should be dead by now
            print('[INFO]: dead')
            run = False
            background_music.stop()
            dead_music.play()
            # currently solution to Bug#3
            sleep(10)
            dead_music.stop()
            background_music.play()
            run = True
            self.__init__()
            return
        # only do these when it is not dead
        self.body.append(self.head)
        self.directions.append(pattern(direction, self.head_direction))
        self.head = tmp
        self.head_direction = direction
        # noinspection PyGlobalUndefined
        global foods
        if self.head in foods:
            if len(foods) <= FOOD_AMOUNT:
                # generate food only when there's not enough food(required for robots, which is not code currently)
                foods[foods.index(self.head)] = generate()
            else:
                del (foods[foods.index(self.head)])
        else:
            # if the snake didn't eat any food, delete the tail of the snake(at [0])
            del (self.directions[0])
            del (self.body[0])

    def push(self):
        # this function is used to push the snake in DELAY seconds.
        # run in a thread
        while True:
            # make sure the thread is always alive and therefore only need to start once
            if run:
                sleep(DELAY)
                self.move(self.head_direction)


class Game:
    @staticmethod
    def print_p():
        # print the whole window
        screen.fill((255, 255, 255))
        screen.blit(background_image, (0, 0))
        user.print_p()
        # switch x y, see definition of x y
        for food in foods:
            screen.blit(food_image, (food[1] * BLOCK_SIZE, food[0] * BLOCK_SIZE))
        for poison in poisons:
            screen.blit(poison_image, (poison[1] * BLOCK_SIZE, poison[0] * BLOCK_SIZE))
        screen.blit(font.render(str((len(user.body) + 1) * 5), False, (255, 200, 10)), (10, 10))

    # noinspection PyGlobalUndefined
    def mainloop(self):
        # actually fully static
        while True:
            # make sure the thread is always alive and therefore only need to start once
            if run:
                key_list = pygame.key.get_pressed()
                for event in pygame.event.get():
                    # event queue
                    if event.type == QUIT:
                        print('[INFO]: exit requested')
                        pygame.quit()
                        global exit_p
                        exit_p = True
                        return
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
            # this is the part where README.md says running with a error, currently no solution, so wait
            # else:
            #
            #    #target=int(time())+120
            #    #screen.blit(dead_image, (WINDOW_WIDTH/8, 0))    
            #    #while(time()<target):
            #    #    for event in pygame.event.get():
            #    #        # event queue
            #    #        if event.type == QUIT:
            #    #            dead_music.stop()
            #    #            print('[INFO]: exit requested')
            #    #            pygame.quit()
            #    #            exit=True
            #    #            return
            #    #        if event.type == KEYDOWN:
            #    #            if event.key == K_y or key_list[K_y]:
            #    #                dead_music.stop()
            #    #                print('[INFO]: restart game')
            #    #                init()
            #    #                return
            #    #            if event.key == K_RIGHT or key_list[K_RIGHT]:
            #    #                dead_music.stop()
            #    #                print('[INFO]: exit requested')
            #    #                pygame.quit()
            #    #                exit=True
            #    #                return
            pygame.time.Clock().tick(FRAME_RATE)
            pygame.display.update()


def generate():
    # generate new food or poison, they are actually the same
    tmp = (randint(0, MAX_X - 1), randint(0, MAX_Y - 1))
    if tmp in user.body or tmp == user.head or tmp in foods or tmp in poisons or tmp[0] == 0:
        # if it is in the body, or is the head, or already in foods ir poisons
        # or it is in the first row
        # self call to generate a new one
        tmp = generate()
    return tmp


# noinspection PyGlobalUndefined
def init():
    # variables for the whole program
    global foods, poisons, run, user, game_p, exit_p
    background_music.play()
    exit_p = False
    foods = []
    poisons = []
    run = False
    user = Snake()
    game_p = Game()
    for i in range(FOOD_AMOUNT):
        foods.append(generate())
    for i in range(POISON_AMOUNT):
        poisons.append(generate())
    run = True


if __name__ == '__main__':
    init()
    # noinspection PyUnboundLocalVariable
    threading.Thread(target=user.push).start()
    # noinspection PyUnboundLocalVariable
    threading.Thread(target=game_p.mainloop).run()
