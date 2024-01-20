import pygame
import time
import random
from settings import window_x, window_y

#Initialising the window
pygame.init()
dis=pygame.display.set_mode((window_x,window_y))
pygame.display.update()
pygame.display.set_caption('PySnake')

#colours to be used in the game
red=(255,0,0)
blue=(0,0,255)
black=(255,255,255)
white=(0,0,0)

#Position Variables
x1=300
y1=300
x1_change=0
y1_change=0

framerate=60
game_over=False

fps = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True

        #Allows user to control the snake
        if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -10
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = 10
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -10
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = 10
                        x1_change = 0

        
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, black, [x1, y1, 10, 10])

        pygame.display.update()

        fps.tick(framerate)

pygame.quit()
quit()

