import pygame
from settings import *

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WINDOW_X // 2), (WINDOW_Y // 2))]
        self.direction = pygame.Vector2(1, 0)

    def move(self):
        current_head = self.positions[0]
        new_head = ((current_head[0] + self.direction[0] * GRID_SIZE) % WINDOW_X,
                    (current_head[1] + self.direction[1] * GRID_SIZE) % WINDOW_Y)
        self.positions.insert(0, new_head)

        if len(self.positions) > self.length:
            self.positions.pop()

    def draw(self, surface):
        for pos in self.positions:
            pygame.draw.rect(surface, white, (pos[0], pos[1], GRID_SIZE, GRID_SIZE))
