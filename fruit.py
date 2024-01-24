import pygame
import random
from settings import *

class Fruit():
    def __init__(self):
        self.position = self.positionChanger()

    def positionChanger(self):
        x = random.randint(0, (WINDOW_X // GRID_SIZE - 1)) * GRID_SIZE
        y = random.randint(0, (WINDOW_Y // GRID_SIZE - 1)) * GRID_SIZE
        return x, y

    def draw(self, surface):
        pygame.draw.rect(surface, red, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))

class SuperFruit(Fruit):
    def draw(self, surface):
        pygame.draw.rect(surface, blue, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))

