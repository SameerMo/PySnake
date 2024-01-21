import pygame
import random
from settings import *

class Fruit():
    def __init__(self):
        pass
    
    def draw(self, surface):
        fruit_x = random.randint(0, WINDOW_X - GRID_SIZE)
        fruit_y = random.randint(0, WINDOW_Y - GRID_SIZE) 
        pygame.draw.rect(surface, red, (fruit_x, fruit_y, GRID_SIZE, GRID_SIZE))
