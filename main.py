import pygame

#Initialising the window
pygame.init()
dis=pygame.display.set_mode((800,600))
pygame.display.update()
pygame.display.set_caption('PySnake')

game_over=False

blue=(0,0,255)
red=(255,0,0)
white=(0,0,0)
black=(255,255,255)

#Position Variables
x1=300
y1=300
x1_change=0
y1_change=0

clock = pygame.time.Clock()

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

        clock.tick(30)

pygame.quit()
quit()