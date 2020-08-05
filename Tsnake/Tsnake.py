import pygame
from pygame.locals import *
from time import sleep
from random import randint
import threading

DELAY = 0.1  # time before auto move(in sec, float)
# I suggest when you DEBUG, set the value to 0.5 or larger(depending on your speed :D), when release, set it back
WINDOW_WIDTH = 640  # must be BLOCK_SIZE*n
WINDOW_HEIGHT = 480  # same.
FOOD_AMOUNT = 3  # int >=1
POISON_AMOUNT = 3  # int >=0
BLOCK_SIZE = 20
MAX_X = WINDOW_HEIGHT // BLOCK_SIZE  #
MAX_Y = WINDOW_WIDTH // BLOCK_SIZE

# x\y 0 .. MAX_Y
# 0
# 1
# .
# .
# MAX_X
# WINDOW_WIDTH*WINDOW_HEIGHT pixels
background_image = pygame.image.load('pics/background.png')
dead_image=pygame.image.load('pics/dead.png')

# BLOCK_SIZE*BLOCK_SIZE pixel
body_image_1 = pygame.image.load('pics/body/1.png')
body_image_2 = pygame.image.load('pics/body/2.png')
body_image_3 = pygame.image.load('pics/body/3.png')
body_image_12 = pygame.image.load('pics/body/12.png')
body_image_13 = pygame.image.load('pics/body/13.png')
body_image_23 = pygame.image.load('pics/body/23.png')

head_image_0 = pygame.image.load('pics/head/0.png')
head_image_1 = pygame.image.load('pics/head/1.png')
head_image_2 = pygame.image.load('pics/head/2.png')
head_image_3 = pygame.image.load('pics/head/3.png')

food_image = pygame.image.load('pics/food.png')

poison_image = pygame.image.load('pics/poison.png')


def pattern(op, direction):
    direction_p = 3 - direction
    return min(op, direction_p) * 10 + max(op, direction_p)


# noinspection PyGlobalUndefined
class Snake:
    def __init__(self, body=None, head=None, directions=None, head_direction=None):
        self.run = False
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
        self.print()
        self.run = True

    def print(self):
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
            self.run = False
            main_task._stop()
            screen.blit(dead_image, (80, 0))
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
        while self.run:
            sleep(DELAY)
            self.move(self.head_direction)


class Game:
    def __init__(self):
        # noinspection PyGlobalUndefined
        global user, foods, poisons
        poisons = []
        screen.blit(background_image, (0, 0))
        user = Snake()
        threading.Thread(target=user.push).start()
        foods = []
        poisons = []
        for i in range(FOOD_AMOUNT):
            foods.append(generate())
        for i in range(POISON_AMOUNT):
            poisons.append(generate())

    @staticmethod
    def print():
        user.print()
        for food in foods:
            screen.blit(food_image, (food[1] * BLOCK_SIZE, food[0] * BLOCK_SIZE))
        for poison in poisons:
            screen.blit(poison_image, (poison[1] * BLOCK_SIZE, poison[0] * BLOCK_SIZE))
        screen.blit(font.render(str((len(user.body) + 1) * 5), False, (255, 200, 10)), (10, 10))

    def mainloop(self):
        while user.run:
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
            screen.fill((255, 255, 255))
            screen.blit(background_image, (0, 0))
            self.print()
            pygame.time.Clock().tick(60)
            pygame.display.update()


def generate():
    tmp = (randint(0, MAX_X - 1), randint(0, MAX_Y - 1))
    if tmp in user.body or tmp == user.head or tmp in foods or tmp in poisons:
        generate()
    return tmp


if __name__ == '__main__':
    if WINDOW_WIDTH % BLOCK_SIZE != 0:
        print('[Error]: Bad WINDOW_WIDTH WINDOW_HEIGHT')
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
    font = pygame.font.SysFont('microsoft Yahei', 30)
    pygame.display.set_caption('T_snake')
    game_p = Game()
    main_task = threading.Thread(target=game_p.mainloop)
    main_task.run()
