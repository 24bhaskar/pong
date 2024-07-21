import pygame
pygame.init()

class Ball():

    def __init__(self, color, x, y, size, velocity_x, velocity_y):
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        self.velocity = [velocity_x, velocity_y]

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)

class Paddle():

    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])

    def move_up(self, speed):
        if self.y > 0:
            self.y -= speed
    
    def move_down(self, speed):
        if self.y < 600 - self.height:
            self.y += speed