import pygame
from pygame.locals import *
from sys import exit
from time import sleep
from random import randint
import threading

DELAY=0.1 # time before auto move(in sec, float)
WINDOW_WIDTH=640 # must be BLOCK_SIZE*n
WINDOW_HEIGHT=480 # same.
FOOD_AMOUNT=3 # int >=1
POISON_AMOUNT=3 # int >=0
BLOCK_SIZE=20
MAX_X=WINDOW_HEIGHT//BLOCK_SIZE #
MAX_Y=WINDOW_WIDTH//BLOCK_SIZE

# x\y 0 .. MAX_Y
# 0
# 1
# .
# .
# MAX_X
# WINDOW_WIDTH*WINDOW_HEIGHT pixels
background_image=pygame.image.load('pics/background.png')

# BLOCK_SIZE*BLOCK_SIZE pixel
body_image_1=pygame.image.load(B'pics/body/1.png')
body_image_2=pygame.image.load('pics/body/2.png')
body_image_3=pygame.image.load('pics/body/3.png')
body_image_12=pygame.image.load('pics/body/12.png')
body_image_13=pygame.image.load('pics/body/13.png')
body_image_23=pygame.image.load'pics/body/23.png')

head_image_0=pygame.image.load('pics/head/0.png')
head_image_1=pygame.image.load('pics/head/1.png')
head_image_2=pygame.image.load('pics/head/2.png')
head_image_3=pygame.image.load('pics/head/3.png')

food_image=pygame.image.load('pics/food.png')

poison_image=pygame.image.load('pics/poison.png')

def print_snake():
    exec('screen.blit(head_image_'+str(direction)+',(head[1]*BLOCK_SIZE,head[0]*BLOCK_SIZE))')
    for food in foods:
        screen.blit(food_image,(food[1]*BLOCK_SIZE,food[0]*BLOCK_SIZE))
    for posion in poisons:
        screen.blit(poison_image,(posion[1]*BLOCK_SIZE,posion[0]*BLOCK_SIZE))
    for i in range(len(snake)):
        exec('screen.blit(body_image_'+str(list_direction[i])+',(snake[i][1]*BLOCK_SIZE,snake[i][0]*BLOCK_SIZE))')

def generate():
    tmp=(randint(0,MAX_X-1),randint(0,MAX_Y-1))
    if(tmp in snake or tmp==head or tmp in foods or tmp in poisons):
        generate()
    return tmp

def build():
    global snake,list_direction,head,direction,foods,poisons
    screen.blit(background_image,(0,0))
    snake,list_direction,head,direction,foods,poisons=[(0,0),(0,1),(0,2),(0,3)],[3]*4,(0,4),3,[],[]
    for i in range(FOOD_AMOUNT):
        foods.append(generate())
    for i in range(POISON_AMOUNT):
        poisons.append(generate())

def pattern(op,dir):
    dirp=3-dir
    return min(op,dirp)*10+max(op,dirp)

def move(op):
    global direction
    if(op+direction==3):
        return
    global head
    snake.append(head)
    list_direction.append(pattern(op,direction))
    next=[(0,-1),(-1,0),(1,0),(0,1)]
    tmp=(head[0]+next[op][0],head[1]+next[op][1])
    if(tmp[0]>=MAX_X or tmp[0]<0 or tmp[1]>=MAX_Y or tmp[1]<0 or tmp in snake or tmp in poisons):
        print('[INFO]: dead')
        build()
        return
    head=tmp
    direction=op
    global foods
    if(tmp in foods):
        print('[INFO]: eat food')
        foods[foods.index(tmp)]=generate()
    else:
        del(snake[0])
        del(list_direction[0])

def push():
    while True:
        sleep(DELAY)
        move(direction)

def mainloop():
     while(True):
        key_list=pygame.key.get_pressed()
        for event in pygame.event.get():
            # event queue
            if(event.type==QUIT):
                print('[INFO]: exit requested')
                pygame.quit()
            if(event.type==KEYDOWN):
                if(event.key==K_LEFT or key_list[K_LEFT]):
                    print('[INFO]: left pressed')
                    move(0)
                if(event.key==K_RIGHT or key_list[K_RIGHT]):
                    print('[INFO]: right pressed')
                    move(3)
                if(event.key==K_UP or key_list[K_UP]):
                    print('[INFO]: up pressed')
                    move(1)
                if(event.key==K_DOWN or key_list[K_DOWN]):
                    print('[INFO]: down pressed')
                    move(2)
        screen.fill((255,255,255))
        screen.blit(background_image,(0,0))
        print_snake()
        pygame.time.Clock().tick(60)
        pygame.display.update()

if __name__=='__main__':
    if(WINDOW_WIDTH%BLOCK_SIZE!=0):
        print('[Error]: Bad WINDOW_WIDTH WINDWO_HEIGHT')
    maintask=threading.Thread(target=mainloop)
    pushtask=threading.Thread(target=push)
    pygame.init()
    pygame.font.init()
    screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),0,32)
    pygame.display.set_caption('Tsnake')
    build()
    pushtask.start()
    maintask.run()
