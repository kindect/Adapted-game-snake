# this is the main program of the snake
import pygame
from pygame.locals import *
from sys import exit
from time import sleep
from random import randint
import threading

DELAY=0.1
delay=DELAY/10
WINDOW_WIDTH=640
WINDOW_HEIGHT=480
BLOCK_SIZE=20
# notice WINDOW_WIDTH%BLOCK_SIZE and WINDOW_HEIGHT must be 0
if(WINDOW_WIDTH%BLOCK_SIZE!=0):
    print('[Error]: Bad WINDOW_WIDTH WINDWO_HEIGHT or BLOCK_SIZE')
MAX_X=WINDOW_HEIGHT//BLOCK_SIZE
MAX_Y=WINDOW_WIDTH//BLOCK_SIZE

BACKGROUND_IMAGE='pics/background.png'
background_image=pygame.image.load(BACKGROUND_IMAGE)
# size notice: WINDOWS_WIDTH*WINDOWS_HEIGHT


# size notice BLOCK_SIZE*BLOCK_SIZE
BODY_IMAGE_01='pics/body/01.png'
BODY_IMAGE_02='pics/body/02.png'
BODY_IMAGE_03='pics/body/03.png'
BODY_IMAGE_12='pics/body/12.png'
BODY_IMAGE_13='pics/body/13.png'
BODY_IMAGE_23='pics/body/23.png'
body_image_01=pygame.image.load(BODY_IMAGE_01)
body_image_02=pygame.image.load(BODY_IMAGE_02)
body_image_03=pygame.image.load(BODY_IMAGE_03)
body_image_12=pygame.image.load(BODY_IMAGE_12)
body_image_13=pygame.image.load(BODY_IMAGE_13)
body_image_23=pygame.image.load(BODY_IMAGE_23)

HEAD_IMAGE_0='pics/head/0.png'
HEAD_IMAGE_1='pics/head/1.png'
HEAD_IMAGE_2='pics/head/2.png'
HEAD_IMAGE_3='pics/head/3.png'
head_image_0=pygame.image.load(HEAD_IMAGE_0)
head_image_1=pygame.image.load(HEAD_IMAGE_1)
head_image_2=pygame.image.load(HEAD_IMAGE_2)
head_image_3=pygame.image.load(HEAD_IMAGE_3)

FOOD_IMAGE='pics/food.png'
food_image=pygame.image.load(FOOD_IMAGE)
# x\y 0 1 2 3 4
# 0
# 1
# 2
# 3
# 4

# storage: snake list[truple](eg. [(0,0),(1,0),(2,0),(3,0)]) no head
#          head: (5,0)
# init when start:
def print_snake():
    exec('screen.blit(head_image_'+str(direction)+',(head[1]*20,head[0]*20))')
    for food in foods:
        screen.blit(food_image,(food[1]*20,food[0]*20))
    for i in range(len(snake)):
        exec('screen.blit(body_image_'+list_direction[i]+',(snake[i][1]*20,snake[i][0]*20))')
        # screen.blit(body_image_01,(snake[i][1]*20,snake[i][0]*20))

def generate_food():
    tmp=(randint(0,MAX_X-1),randint(0,MAX_Y-1))
    if(tmp in snake or tmp==head):
        generate_food()
        return
    print('[INFO]: generate food at',tmp)
    return tmp

def build():
    global snake,list_direction,head,direction,foods
    screen.blit(background_image,(0,0))
    snake=[(0,0),(0,1),(0,2),(0,3)]
    list_direction=['03']*4
    head=(0,4)
    direction=3
    generate_food()
    foods=[generate_food(),generate_food(),generate_food()]

def pattern(op,dir):
    dirp=3-dir # the opposite of dir
    return str(min(op,dirp))+str(max(op,dirp))
def move(op):
    global direction
    if(op+direction==3):
        # oppsite the direction of moving
        return
    # left(0), up(1), down(2), right(3)
    global head
    snake.append(head)
    list_direction.append(pattern(op,direction))
    next=[(0,-1),(-1,0),(1,0),(0,1)]
    tmp=(head[0]+next[op][0],head[1]+next[op][1])
    if(tmp[0]>=MAX_X or tmp[0]<0 or tmp[1]>=MAX_Y or tmp[1]<0 or tmp in snake):
        print('[INFO]: dead')
        build()
        return
    head=tmp
    direction=op
    global foods
    if(tmp in foods):
        print('[INFO]: eat food')
        foods[foods.index(tmp)]=generate_food()
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
    maintask=threading.Thread(target=mainloop)
    pushtask=threading.Thread(target=push)
    pygame.init()
    pygame.font.init()
    screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),0,32)
    pygame.display.set_caption('Tsnake')
    build()
    pushtask.start()
    maintask.run()