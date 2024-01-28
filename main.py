import pygame
import time
import random
from settings import *
from snake import Snake, CPUPlayer
from fruit import Fruit, SuperFruit

#Initialising the window
pygame.init()
dis=pygame.display.set_mode((WINDOW_X,WINDOW_Y))
pygame.display.update()
pygame.display.set_caption('PySnake')

#Creating a snake
snake=Snake()
snake_speed = pygame.time.Clock()
speed=10

power=random.randint(1,10)
powerc=random.randint(1,10)
if power==powerc:
    fruit=SuperFruit()
else:
    fruit=Fruit()
game_over=False

cpu_player = CPUPlayer(snake, fruit)

#Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over=True
        #Allows user to control the snake checks for keypresses and ignores if already travelling in that direction
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not snake.direction.y:
                snake.direction = pygame.Vector2(0, -1)
            elif event.key == pygame.K_DOWN and not snake.direction.y:
                snake.direction = pygame.Vector2(0, 1)
            elif event.key == pygame.K_LEFT and not snake.direction.x:
                snake.direction = pygame.Vector2(-1, 0)
            elif event.key == pygame.K_RIGHT and not snake.direction.x:
                snake.direction = pygame.Vector2(1, 0)
        
    snake.move()

    dis.fill(black)

    snake.draw(dis)

    fruit.draw(dis)

    if snake.collisionCheck():
        game_over=True

    if snake.eatCheck(fruit):
        if isinstance(fruit, SuperFruit):
            speed += 1
        power=random.randint(1,10)
        powerc=random.randint(1,10)
        if power==powerc:
            fruit=SuperFruit()
        else:
            fruit=Fruit()
        fruit.position = fruit.positionChanger()
        snake.eat()
            
            
    cpu_move = cpu_player.decide_next_move()
    snake.direction = cpu_move


    pygame.display.flip()

    snake_speed.tick(speed)

pygame.quit()
quit()