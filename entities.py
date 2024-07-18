import pygame

class Ball():

    def __init__(self, color, size):
        self.color = color
        self.size = size

    def draw(self, screen, x, y):
        pygame.draw.circle(surface=screen, color=self.color, center=[x, y], radius=self.size)


class Paddle():

    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height
    
    def draw(self, screen, x, y):
        pygame.draw.rect(surface=screen, color=self.color, rect=[x, y, self.width, self.height])